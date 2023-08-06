import pandas as pd
import numpy as np
import sys
import os
import pytd
import requests
import json
import datetime

##-- Declare ENV Variables from YML file
apikey = os.environ['TD_API_KEY'] 
tdserver = os.environ['TD_API_SERVER']
sink_database = os.environ['SINK_DB']
output_table = os.environ['OUTPUT_TABLE']
folder_depth = os.environ['FOLDER_DEPTH']
v5_flag = os.environ['v5_flag']
segment_api = tdserver.replace('api', 'api-cdp')
headers= {"Authorization":'TD1 '+ apikey, "content-type": "application/json"}

############ Function to Read JSON #####################
def json_extract(url):
    #Get Segment Info JSON from Master Segment using TD API
    get_info = requests.get(url, headers=headers)

    return get_info.json()

##########Function to extract Parent Segment Info from V4 and V5 ###########
def get_ps_list():
    v4_segment_list = f'https://{segment_api}/audiences'
    v5_segments_list = f'https://{segment_api}/entities/parent_segments'
    v4_dic = dict(ps_id = [], ps_id_v4 = [], ps_name = [], ps_population = [], root_folder = [])
    v5_dic = dict(ps_id = [], ps_id_v4 = [], ps_name = [], ps_population = [], root_folder = [])
    
    if v5_flag=='0':
        v4_ps = json_extract(v4_segment_list)
        for item in v4_ps:
            v4_dic['ps_id'].append(item['id'])
            v4_dic['ps_id_v4'].append(item['id'])
            v4_dic['ps_name'].append(item['name'])
            v4_dic['ps_population'].append(item['population'])
            v4_dic['root_folder'].append(item['rootFolderId'])

        v4_df = pd.DataFrame(v4_dic)
        v4_df.fillna(0, inplace = True)
        v4_df['v5_flag'] = 0
        new_df = v4_df
        new_df.reset_index(drop = True, inplace = True)

    elif v5_flag=='1': 
        v5_ps = json_extract(v5_segments_list)
        v5_ps_data = v5_ps['data']
        for item in v5_ps_data:
            v5_dic['root_folder'].append(item['id'])
            v5_dic['ps_id_v4'].append(item['id'])
            v5_dic['ps_name'].append(item['attributes']['name'] + " Root")
            v5_dic['ps_population'].append(item['attributes']['population'])
            v5_dic['ps_id'].append(item['relationships']['parentSegmentFolder']['data']['id'])


        v5_df = pd.DataFrame(v5_dic)
        v5_df.fillna(0, inplace = True)
        v5_df['v5_flag'] = 1
        
        new_df = v5_df
        new_df.reset_index(drop = True, inplace = True)
        
    elif v5_flag=='1,0':
        v4_ps = json_extract(v4_segment_list)
        for item in v4_ps:
            v4_dic['ps_id'].append(item['id'])
            v4_dic['ps_id_v4'].append(item['id'])
            v4_dic['ps_name'].append(item['name'])
            v4_dic['ps_population'].append(item['population'])
            v4_dic['root_folder'].append(item['rootFolderId'])

        v4_df = pd.DataFrame(v4_dic)
        v4_df.fillna(0, inplace = True)
        v4_df['v5_flag'] = 0

        v5_ps = json_extract(v5_segments_list)
        v5_ps_data = v5_ps['data']
        for item in v5_ps_data:
            v5_dic['root_folder'].append(item['id'])
            v5_dic['ps_id_v4'].append(item['id'])
            v5_dic['ps_name'].append(item['attributes']['name'] + " Root")
            v5_dic['ps_population'].append(item['attributes']['population'])
            v5_dic['ps_id'].append(item['relationships']['parentSegmentFolder']['data']['id'])


        v5_df = pd.DataFrame(v5_dic)
        v5_df.fillna(0, inplace = True)
        v5_df['v5_flag'] = 1
        
        new_df = pd.concat([v4_df, v5_df])
        new_df.reset_index(drop = True, inplace = True)
    else:
        print("provide valid v5_flag")

    return new_df


######## Function to extract Folder Info from V4 and V5 ################
def get_folder_list(ps_df):
    v4_ps = list(ps_df[ps_df.v5_flag == 0].ps_id)
    v5_ps = list(zip(list(ps_df[ps_df.v5_flag == 1].root_folder), list(ps_df[ps_df.v5_flag == 1].ps_id)))
    
    combined_folders = []

    for master_id in v4_ps:
        try:
            v4_url_folders = f'https://{segment_api}/audiences/{master_id}/folders'
            v4_json = json_extract(v4_url_folders)

            folders = [{'ps_id': master_id, 'folder_id': item['id'], 'folder_name': item['name']} for item in v4_json]
            combined_folders.extend(folders)
        except:
            print(f"No Audience Segments built V4 for Parent Segment - {master_id}")

    if len(v5_ps) > 0:
        for id_list in v5_ps:
            v5_url_folders = f'https://{segment_api}/audiences/{id_list[0]}/folders'
            v5_json = json_extract(v5_url_folders)

            folders = [{'ps_id': id_list[1], 'folder_id': item['id'], 'folder_name': item['name']} for item in v5_json]
            combined_folders.extend(folders)
            
    return pd.DataFrame(combined_folders)


################## Function to extract Segment Info from V4 and V5 #############
def get_segment_list(ps_df):
    v4_ps = list(ps_df[ps_df.v5_flag == 0].ps_id)
    v5_ps = list(ps_df[ps_df.v5_flag == 1].ps_id)
    
    combined_segments = []

    for master_id in v4_ps:
        v4_url_segments = f'https://{segment_api}/audiences/{master_id}/segments'
        v4_json = json_extract(v4_url_segments)

        segments = [{'folder_id': item['segmentFolderId'], 'segment_id': item['id'], 'segment_name': item['name'],
                    'segment_population': item['population'], 'realtime': item['realtime'], 'rule': item['rule']} for item in v4_json]
        
        combined_segments.extend(segments)

    if len(v5_ps) > 0:
        for master_id in v5_ps:
            v5_url_segments = f'https://{segment_api}/entities/by-folder/{master_id}?depth=10'
            v5_json = json_extract(v5_url_segments)['data']
            segment_json = [item for item in v5_json if item['type'].startswith('segment-')]

            segments = [{'folder_id': item['relationships']['parentFolder']['data']['id'], 'segment_id': item['id'], 
                         'segment_name': item['attributes']['name'],'segment_population': item['attributes']['population'], 
                         'realtime': item['type'], 'rule': item['attributes']['rule']} for item in segment_json]
            
            combined_segments.extend(segments)
            
    segment_df = pd.DataFrame(combined_segments)
    segment_df.realtime = [1 if item == True or str(item).startswith('segment-re') else 0 for item in list(segment_df.realtime)]
    segment_df['funnel_flag'] = [0 for item in list(segment_df.segment_id)]
    
    return segment_df

################## Function to extract CJO Funnel Stages info from V5 #############
def get_funnel_list(ps_df):
    #get list of Parent Segment IDs
    ps_list = list(ps_df.root_folder)
    
    #create empty funnel dictionary
    funnel_info = dict(cdp_audience_id = [], funnel_id = [], funnel_name = [], funnel_population = [], folder_id = [], 
             stage_id = [], stage_name = [], segment_id = [], segment_name = [], segment_population = [], rule = [])
    
    #Loop through PS list and extract funnel info
    for master_id in ps_list:
        funnel_url = f'https://{segment_api}/entities/parent_segments/{master_id}/funnels'
        funnels_json = json_extract(funnel_url)['data']
        
        for funnel in funnels_json:
            
            for stage in funnel['attributes']['stages']:
                funnel_info['cdp_audience_id'].append(master_id)
                funnel_info['funnel_id'].append(funnel['id'])
                funnel_info['funnel_name'].append(funnel['attributes']['name'])
                funnel_info['funnel_population'].append(funnel['attributes']['population'])
                funnel_info['folder_id'].append(funnel['relationships']['parentFolder']['data']['id'])
                funnel_info['stage_id'].append(stage['id'])
                funnel_info['stage_name'].append(stage['name'])
                funnel_info['segment_id'].append(stage['segmentId'])
                funnel_info['segment_name'].append(stage['name'])
                funnel_info['segment_population'].append(stage['population'])
                
                #get query rule for creating stage segment
                segment_id = stage['segmentId']
                segment_url = f'https://{segment_api}/entities/segments/{segment_id}'
                segments_json = json_extract(segment_url)['data']
                funnel_info['rule'].append(segments_json['attributes']['rule'])  
                
    funnel_df = pd.DataFrame(funnel_info)
    funnel_df['funnel_flag'] = [1 for item in funnel_df.cdp_audience_id]
                
    return funnel_df

################## Function to extract CJO Historic Funnel Population Stats #############
def get_funnel_stats(funnel_df):
    funnel_list = list(zip(funnel_df.cdp_audience_id, funnel_df.funnel_id, funnel_df.funnel_name))
    
    funnel_info = dict(time = [], tstamp = [], ps_id = [], funnel_id = [], funnel_name = [], 
                        stage_id = [],  population = [])
    
    for funnels in funnel_list:
        ps_id = funnels[0]
        funnel_id = funnels[1]
        funnel_stats = f'https://{segment_api}/audiences/{ps_id}/funnels/{funnel_id}/statistics'
        stats_json = json_extract(funnel_stats)
        
        for stage in stats_json['stages']:
            for date in stage['history']:
                funnel_info['time'].append(int(date[0]))
                timestamp = datetime.datetime.fromtimestamp(date[0])
                funnel_info['tstamp'].append(timestamp.strftime("%Y-%m-%d %H:%M:%S"))
                funnel_info['ps_id'].append(ps_id)
                funnel_info['funnel_id'].append(funnel_id)
                funnel_info['funnel_name'].append(funnels[2])
                funnel_info['stage_id'].append(stage['id'])
                funnel_info['population'].append(date[1])
    
    
    stats_df = pd.DataFrame(funnel_info)
    stages_df = funnel_df[['stage_id', 'stage_name']]
    stages_df['stage_id'] = stages_df['stage_id'].astype('int64')
    stats_final = pd.merge(stats_df, stages_df, on='stage_id', how = 'left')
    
    return stats_final

##################### FINAL FUNCTION THAT RUNS ALL CODE #####################################

def extract_segment_stats():

    #get Parent Segment DF
    ps_df = get_ps_list()

    #get Folder Info DF
    folders_df = get_folder_list(ps_df)

    #Merge both DFs on ps_id
    combined_df = pd.merge(ps_df, folders_df, on="ps_id", how = 'left')

    #Get Folder Segments Info
    segments_df = get_segment_list(ps_df)
    
    #Get CJO Funnels Info
    funnel_df = get_funnel_list(ps_df)
    
    #If CJO Funnels exist, combine segments and funnel DFs and get funnel stats
    if len(funnel_df) > 0:
        segments_df = pd.concat([segments_df, funnel_df])
#         segments_df.funnel_flag.fillna(0.0, inplace = True)

    #Merge Segments DF into combined on folder_id
    final_df = pd.merge(combined_df, segments_df, on="folder_id", how = 'left')

    #Replace NaN with 0 for numeric columns and drop duplicate columns caused by v4/v5 segment name overlap
    final_df.segment_population.fillna(0, inplace = True)
    final_df.realtime.fillna(0, inplace = True)
    final_df.dropna(subset = ['segment_id'], inplace = True)
    final_df.drop_duplicates(subset=['root_folder', 'folder_id', 'folder_name', 'segment_id', 'segment_name'], keep='first', inplace=True, ignore_index=False)

    final_df.info()
    final_df.head()

    #Write final_df to TD
    client = pytd.Client(apikey=apikey, endpoint=tdserver, database=sink_database)
    client.load_table_from_dataframe(final_df, output_table, writer='bulk_import', if_exists='overwrite')
    
    #If Funnels exist, write Journey Stats Tablew
    if len(funnel_df) > 0:
        funnel_stats_df = get_funnel_stats(funnel_df)
        client.load_table_from_dataframe(funnel_stats_df, 'segment_analytics_funnel_stats', writer='bulk_import', if_exists='overwrite')