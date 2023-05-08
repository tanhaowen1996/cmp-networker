from requests.auth import HTTPBasicAuth
import requests
from requests import exceptions
import json
import urllib3
from urllib3.exceptions import InsecureRequestWarning

session = HTTPBasicAuth("administrator", "ad#adMdaE1d31Da$a")
print(session)
urllib3.disable_warnings(InsecureRequestWarning)

# payload = json.dumps({
#   "authoritative": "mode",
#   "mode": "777",
# })
# url = 'https://10.208.0.172:9090/nwrestapi/v3/global/vmware/vcenters/yhcmpvc7.yonghui.cn/protectedvms/da1bb976-ddf2-47d8-b0a8-a872d45016d7/backups/'
# try:
#     r = requests.get(url=url, auth=session, verify=False)
# except exceptions.Timeout as e:
#     print(e)
# except exceptions.HTTPError as e:
#     print(e)
# if r.status_code == 404:
#     print("sssss")
# s = r.json()
# print(s)
# import pdb
# pdb.set_trace()
# print(r.status_code)
# # r = requests.get(url, auth=rw_session, verify=False)
# response_dict = r.json()
#     try:
#         VServers = response_dict.get("SlbNewCfgEnhVirtServerTable")
policy_name = "thw7-test-policy"
url = "https://10.208.0.172:9090/nwrestapi/v3/global/protectionpolicies/thw7-test-policy/workflows/thw7"
# payload = json.dumps(
#     {
#         "name": "thw7",
#         "autoStartEnabled": True,
#         "enabled": True,
#         "comment": "",
#         "completionNotification": {
#             "command": "",
#             "executeOn": "Ignore"
#         },
#         "description": "Empty workflow;",
#         "restartTimeWindow": "24:00",
#         "startInterval": "24:00",
#         "startTime": "00:00",
#         "protectionGroups": [],
#     }
# )
headers = {
    'Content-Type': 'application/json'
}
# re = requests.get(
#     url="https://10.208.0.172:9090/nwrestapi/v3/global/protectionpolicies/thw7-test-policy/workflows/thw7",
#     auth=session, headers=headers, verify=False)
# list_actions = re.json().get("actions")
# print(list_actions)
# response = requests.post(url=url, auth=session, headers=headers, data=payload, verify=False)

# print(response.status_code)
# 'actionSpecificData': {'retentionPeriod': '1 Weeks', 'successThreshold': 'Success'}}}]

# actions = []
# for action in list_actions:
#     actions.append(
#         {
#             "name": action.get("name"),
#             "scheduleActivities": action.get("scheduleActivities"),
#             "schedulePeriod": action.get("schedulePeriod"),
#             "actionSpecificData": {
#                 "backup": {
#                     "backupSpecificData": {
#                         "vmwareVProxy": {
#                             "destinationPool": action.get("actionSpecificData").get("backup").get(
#                                 "backupSpecificData").get("vmwareVProxy").get("destinationPool"),
#                         }
#                     },
#                     "destinationStorageNodes": action.get("actionSpecificData").get("backup").get(
#                         "destinationStorageNodes"),
#                     "retentionPeriod": action.get("actionSpecificData").get("backup").get("retentionPeriod"),
#                     "successThreshold": action.get("actionSpecificData").get("backup").get("successThreshold"),
#                 }
#             }
#         }
#     )
# action = {
#     "name": "backup2",
#     "scheduleActivities": [
#         "full",
#         "full",
#         "incr",
#         "incr",
#         "incr",
#         "incr",
#         "incr"
#     ],
#     "schedulePeriod": "Week",
#     "actionSpecificData": {
#         "backup": {
#             "backupSpecificData": {
#                 "vmwareVProxy": {
#                     "destinationPool": "Data Domain Default"
#                 }
#             },
#             "destinationStorageNodes": [
#                 "nsrserverhost"
#             ],
#             "retentionPeriod": "1 Weeks",
#             "successThreshold": "Success"
#         }
#     }
# }
# actions.append(action)
# print(actions)
# payload = json.dumps(
#     {
#         "actions":
#             [
#                 {
#                     "name": "backup",
#                     "scheduleActivities": [
#                         "full",
#                         "incr",
#                         "incr",
#                         "incr",
#                         "incr",
#                         "incr",
#                         "incr"
#                     ],
#                     "schedulePeriod": "Week",
#                     "actionSpecificData":
#                         {
#                             "backup": {
#                                 "backupSpecificData": {
#                                     "vmwareVProxy": {
#                                         "destinationPool": "Data Domain Default"
#                                     }
#                                 },
#                                 "destinationStorageNodes": ["nsrserverhost"],
#                                 "retentionPeriod": "1 Weeks",
#                                 "successThreshold": "Success"
#                             }
#                         }
#                 },
#                 {
#                     "name": "backup2",
#                     "scheduleActivities": [
#                         "full",
#                         "full",
#                         "incr",
#                         "incr",
#                         "incr",
#                         "incr",
#                         "incr"
#                     ],
#                     "schedulePeriod": "Week",
#                     "actionSpecificData": {
#                         "backup": {
#                             "backupSpecificData": {
#                                 "vmwareVProxy": {
#                                     "destinationPool": "Data Domain Default"
#                                 }
#                             },
#                             "destinationStorageNodes": ["nsrserverhost"],
#                             "retentionPeriod": "1 Weeks",
#                             "successThreshold": "Success"
#                         }
#                     }
#                 }
#             ]
#     }
# )
# payload = json.dumps(
#     {
#         "actions": actions
#     {
#         "name": "backup2",
#         "scheduleActivities": [
#             "full",
#             "incr",
#             "incr",
#             "incr",
#             "incr",
#             "incr",
#             "incr"
#         ],
#         "schedulePeriod": "Week",
#         "actionSpecificData": {
#             "backup": {
#                 "backupSpecificData": {
#                     "vmwareVProxy": {
#                         "destinationPool": "Data Domain Default"
#                     }
#                 },
#                 "destinationStorageNodes": [
#                     "nsrserverhost"
#                 ],
#                 "retentionPeriod": "1 Weeks",
#                 "successThreshold": "Success"
#             }
#         }
#     }
# ]
#     }
# )
# print(payload)

# response = requests.put(url=url, auth=session, headers=headers, data=payload, verify=False)
# print(response.status_code)
#
# s = [{'name': 'backup', 'scheduleActivities': ['full', 'incr', 'incr', 'incr', 'incr', 'incr', 'incr'], 'schedulePeriod': 'Week', 'actionSpecificData': {'backup': {'backupSpecificData': {'vmwareVProxy': {'destinationPool': 'Data Domain Default'}}, 'destinationStorageNodes': ['nsrserverhost'], 'retentionPeriod': '1 Weeks', 'successThreshold': 'Success'}}},
#      {'name': 'backup2', 'scheduleActivities': ['full', 'incr', 'incr', 'incr', 'incr', 'incr', 'incr'], 'schedulePeriod': 'Week', 'actionSpecificData': {'backup': {'backupSpecificData': {'vmwareVProxy': {'destinationPool': 'Data Domain Default'}}, 'destinationStorageNodes': ['nsrserverhost'], 'retentionPeriod': '1 Weeks', 'successThreshold': 'Success'}}}]


url = "https://10.208.0.172:9090/nwrestapi/v3/global/vmware/vcenters/yhcmpvc7.yonghui.cn/protectedvms/da1bb976-ddf2-47d8-b0a8-a872d45016d7/backups"

response = requests.get(url=url, auth=session, headers=headers, verify=False)
backups = response.json().get("backups")
for backup in backups:
    for at in backup.get('attributes'):
        if at.get('key') == '*vm_info':
            import pdb
            pdb.set_trace()
    import pdb

    pdb.set_trace()
    print(backup)
import pdb

pdb.set_trace()
print(response.status_code)
s = {
    'attributes':
        [{'key': '**backup start time', 'values': ['1683183614']},
         {'key': '*backup_device', 'values': ['Data Domain']},
         {'key': '*backup_mode', 'values': ['VSS']},
         {'key': '*policy action name', 'values': ['backup: 1683183615']},
         {'key': '*policy name', 'values': ['thw-test-policy: 1683183615']},
         {'key': '*policy workflow name', 'values': ['thw-test: 1683183615']},
         {'key': '*policy_workflow_action_path', 'values': ['/thw-test-policy/thw-test/backup']},
         {'key': '*proxy_hostname', 'values': ['cmp2vproxy216.yonghui.cn']},
         {'key': '*ss clone retention', 'values': ['          1683183615:          1683183615:   2710784']},
         {'key': '*ss data domain backup cloneid', 'values': ['1683183615']},
         {'key': '*ss data domain dedup statistics', 'values': ['v1:1683183615:179506611648:16079684:15150670']},
         {'key': '*SSID directory', 'values': ['Yes']},
         {'key': '*vcenter_hostname', 'values': ['yhcmpvc7.yonghui.cn']},
         {'key': '*vm_backup_level', 'values': ['incr']},
         {'key': '*vm_info', 'values':
             ['{\n  "name": "test-thw (da1bb976-ddf2-47d8-b0a8-a872d45016d7)",\n  '
              '"host-name": "test-thw",\n  '
              '"ip-address": "10.208.224.79",\n  '
              '"template": false,\n  '
              '"moref-id": "vm-45897",\n  '
              '"vcenter-name": "yhcmpvc7.yonghui.cn",\n  '
              '"path": "/MWDC/mw-overlay-cluster04/test-thw (da1bb976-ddf2-47d8-b0a8-a872d45016d7)",\n  '
              '"moref-path": "/datacenter-3/domain-c41025/vm-45897",\n  '
              '"vm-path": "/MWDC/OpenStack/Project (85a3c207c0fc4cdb8840351ba2907d2e)/Instances/test-thw (da1bb976-ddf2-47d8-b0a8-a872d45016d7)",\n  '
              '"moref-vm-path": "/datacenter-3/group-v35110/group-v35229/group-v35230/vm-45897",\n  '
              '"datastore": "mw_pmax2_0577_mwyhc_cl04_sysdisk_0055",\n  '
              '"datastore-moref": "datastore-41022",\n  '
              '"os-identifier": "ubuntu64Guest",\n  '
              '"os-name": "Ubuntu Linux (64-bit)",\n  '
              '"version": "vmx-19",\n  '
              '"change-version": "2023-04-23T07:38:26.238358Z",\n  '
              '"esxi-moref": "host-40935",\n  '
              '"esxi-name": "10.208.1.101",\n  '
              '"datacenter": "datacenter-3",\n  '
              '"compute-resource": "",\n  '
              '"cluster-compute-resource": "domain-c41025",\n  '
              '"networks": [\n    "vlan224"\n  ],\n  '
              '"disks": [\n    {\n      "display-name": "Hard disk 1",\n      "datastore": "mw_pmax2_0577_mwyhc_cl04_sysdisk_0055",\n      "datastore-moref": "datastore-41022",\n      "disk-key": 2000,\n      "size-kb": 52428800,\n      "thin": true,\n      "disk_mode": "persistent",\n      "disk_stats": {\n        "Statistics": {\n          "ProvisionedBytes": 53687091200,\n          "UsedBytes": 18410897408,\n          "ChangedBytes": 0,\n          "SecondsTaken": 0\n        },\n        "DDStatistics": {\n          "PreClientCompBytes": 0,\n          "PostClientCompBytes": 0,\n          "TotalSegments": 0,\n          "RedundantSegments": 0\n        },\n        '
              '"BaseFileName": "[mw_pmax2_0577_mwyhc_cl04_sysdisk_0055] volume-bdfa464b-51ff-4072-bbdd-5f64489ed32c/volume-bdfa464b-51ff-4072-bbdd-5f64489ed32c.vmdk"\n      }\n    },\n    {\n      "display-name": "Hard disk 2",\n      "datastore": "mw_pmax2_0577_mwyhc_cl04_data_0057",\n      "datastore-moref": "datastore-41024",\n      "disk-key": 2001,\n      "size-kb": 104857600,\n      "thin": true,\n      "disk_mode": "persistent",\n      "disk_stats": {\n        "Statistics": {\n          "ProvisionedBytes": 107374182400,\n          "UsedBytes": 71153025024,\n          "ChangedBytes": 548012032,\n          "SecondsTaken": 3\n        },\n        '
              '"DDStatistics": {\n          "PreClientCompBytes": 514744344,\n          "PostClientCompBytes": 45049582,\n          "TotalSegments": 62959,\n          "RedundantSegments": 5327\n        },\n        "BaseFileName": "[mw_pmax2_0577_mwyhc_cl04_data_0057] volume-5b8a6e63-0b9a-4136-908f-07f81b9165a5/volume-5b8a6e63-0b9a-4136-908f-07f81b9165a5.vmdk"\n      }\n    },\n    {\n      "display-name": "Hard disk 3",\n      "datastore": "mw_pmax2_0577_mwyhc_cl04_sysdisk_0055",\n      '
              '"datastore-moref": "datastore-41022",\n      "disk-key": 2002,\n      "size-kb": 52428800,\n      "thin": true,\n      "disk_mode": "persistent",\n      "disk_stats": {\n        "Statistics": {\n          "ProvisionedBytes": 53687091200,\n          "UsedBytes": 18477023232,\n          "ChangedBytes": 416088064,\n          "SecondsTaken": 3\n        },\n        "DDStatistics": {\n          "PreClientCompBytes": 149497463,\n          "PostClientCompBytes": 26921284,\n          "TotalSegments": 48889,\n          "RedundantSegments": 32074\n        },\n        "BaseFileName": "[mw_pmax2_0577_mwyhc_cl04_sysdisk_0055] test-thw (da1bb976-ddf2-47d8-b0a8-a872d45016d7)/Recovered_disk_1.vmdk"\n      }\n    }\n  ]\n}']},
         {'key': '*vm_name', 'values': ['test-thw (da1bb976-ddf2-47d8-b0a8-a872d45016d7)']},
         {'key': '*vm_uuid', 'values': ['da1bb976-ddf2-47d8-b0a8-a872d45016d7']},
         {'key': 'group', 'values': ['thw-test']},
         {'key': 'saveset features', 'values': ['CLIENT_SAVETIME']}
         ],
    'browseTime': '2023-06-04T15:00:11+08:00',
    'clientHostname': 'yhcmpvc7.yonghui.cn',
    'clientId': 'f390f445-00000004-61c327d8-61d7e3d6-004d5000-5cf8b056',
    'completionTime': '2023-05-04T15:00:33+08:00',
    'creationTime': '2023-05-04T15:00:15+08:00',
    'fileCount': 1,
    'id': '4fc5fe86-00000006-2f5357ff-645357ff-b3d35000-5cf8b056',
    'instances': [{'clone': False, 'id': '1683183615', 'status': 'Recoverable', 'volumeIds': ['4240655022']}],
    'level': 'Full',
    'links': [{
        'href': 'https://10.208.0.172:9090/nwrestapi/v3/global/vmware/vcenters/yhcmpvc7.yonghui.cn/protectedvms/da1bb976-ddf2-47d8-b0a8-a872d45016d7/backups/4fc5fe86-00000006-2f5357ff-645357ff-b3d35000-5cf8b056',
        'rel': 'item'}],
    'name': 'vm:da1bb976-ddf2-47d8-b0a8-a872d45016d7:yhcmpvc7.yonghui.cn',
    'retentionTime': '2023-06-04T23:59:58+08:00',
    'saveTime': '2023-05-04T15:00:14+08:00',
    'shortId': '793991167',
    'size': {'unit': 'Byte', 'value': 214958168740},
    'type': 'File',
}

vminfo = {
    "datastoreMoref": "datastore-181990",
    "hostMoref": "host-682",
    "disks": [
        {"datastoreMoref": "datastore-181990", "datastoreName": "ck_pmax2_0034_metro_systemdisk_0042", "key": "2000",
         "name": "Hard disk 1", "sizeInKb": 52428800}],
    "morefPath": "/datacenter-21/domain-c244/vm-219959",
    "vCenterHostname": "yhcmpvc6.yonghui.cn", "vmMoref": "vm-219959",
    "vmName": "arch-service-es-1 (83b25aef-0d20-48d5-891d-70c28499fe21)"}
