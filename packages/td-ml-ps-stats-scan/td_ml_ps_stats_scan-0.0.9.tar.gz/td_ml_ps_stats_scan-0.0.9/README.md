# td-ml-ps-stats-scan

## Introduction

This Python Library allows you to extract Parent Segment, Folder, Audiences info and store it in a table in TD for reporting purposes and mapping audiences to segments and metrics.


## Input Params

`config.yml`: The workflow `YAML` file contains the params that are required by this library to extract the neded information. See below:

- **apikey** = TD APIKEY  
- **tdserver** = TD ENDPOINT
- **sink_database** = Database where outout tables will be written
- **output_table** = name of output table
- **folder_depth** = how many nested folders in Audience Studio to look into for segments (default = `10`)
- **v5_flag** = `1` - scans PSs that are in V5 version, `0` - scans PSs in V4, and `1, 0` scans PS is in both V4 and V5.


`Copyright © 2022 Treasure Data, Inc. (or its affiliates). All rights reserved`


