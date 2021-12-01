Seed data for fmrc download cronjob, needs to be added via console to prevent distribution to multiple tags
'''json
{
    "id" : "download-fmrc-cron",
    "name" : "download-fmrc-cron",
    "description" : "update HycomFMRCs and download files",
    "action" : {
      "typeName" : "HycomDataset",
      "actionName" : "updateFMRCData"
    },
    "inputs": {
        "hycomDatasetId": "GOMu0.04/expt_90.1m000",
        "hycomSubsetOptions": {
            "type": "HycomSubsetOptions",
            "vars": "water_u,water_v",
            "disableLLSubset": "on",
            "vertCoord": 4
        },
        "hycomDownloadOptions": {
            "type": "HycomDownloadOptions",
            "externalDir": "hycom-data",
            "maxTimesPerFile": -1
        },
        "fmrcDownloadJobOptions": {
            "type": "FMRCDownloadJobOptions",
            "batchSize": 5,
            "limit": -1
        }
    },
    "concurrent": false,
    "inactive": false,
    "scheduleDef" : {
      "startTime": null,
      "endTime": null,
      "cronExpression" : "0 0 4,12 * * ?"
    }
  }
  '''