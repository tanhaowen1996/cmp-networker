import json
import requests

from .settings import OS_REGION_MAWEI, NETWORKER_MW_URL, VCENTER_MW, NETWORKER_CK_URL, VCENTER_CK


def get_url(region):
    if region == OS_REGION_MAWEI:
        network_url = NETWORKER_MW_URL
        vcenter = VCENTER_MW
    else:
        network_url = NETWORKER_CK_URL
        vcenter = VCENTER_CK
    return network_url, vcenter


def _split_vm_name_uuid(vm_dir_name):
    """
    vm_dir_name: "asdfghjk (8429558a-4606-48b7-80c4-982e59b82c1d)"
    return: ("asdfghjk", "8429558a-4606-48b7-80c4-982e59b82c1d")
    """
    try:
        return vm_dir_name[:-39], vm_dir_name[-37:-1]
    except Exception as e:
        raise Exception("split vm_dir: %s failed: %s" % (vm_dir_name, e))


def create_policy(session, region, policy_name):
    network_url, vcenter = get_url(region=region)
    url = network_url + "/nwrestapi/v3/global/protectionpolicies"
    payload = json.dumps({
        "name": policy_name,
        "summaryNotification": {
            "command": "nsrlog -f policy_notifications.log",
            "executeOn": "Completion"
        }
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(url=url, auth=session, headers=headers, data=payload, verify=False)


def create_workflow(session, region, policy_name, workflow_name, start_time, Interval, description, schedule_activities,
                    schedule_period):
    network_url, vcenter = get_url(region=region)
    url = network_url + "/nwrestapi/v3/global/protectionpolicies/" + policy_name + "/workflows"
    group_name = policy_name + "_" + workflow_name
    create_group(session, region, group_name)
    payload = json.dumps(
        {
            "name": workflow_name,
            "autoStartEnabled": True,
            "enabled": True,
            "comment": "",
            "completionNotification": {
                "command": "",
                "executeOn": "Ignore"
            },
            "description": description,
            "restartTimeWindow": "24:00",
            "startInterval": Interval,
            "startTime": start_time,
            "protectionGroups": [group_name],
            "actions": [
                {
                    "name": workflow_name + "_action",
                    "scheduleActivities": schedule_activities,
                    "schedulePeriod": schedule_period,
                    "actionSpecificData": {
                        "backup": {
                            "backupSpecificData": {
                                "vmwareVProxy": {
                                    "destinationPool": "Data Domain Default"
                                }
                            },
                            "destinationStorageNodes": [
                                "nsrserverhost"
                            ],
                            "retentionPeriod": "1 Weeks",
                            "successThreshold": "Success"
                        }
                    }
                }
            ]
        }
    )
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(url=url, auth=session, headers=headers, data=payload, verify=False)
    return payload


def start_workflow(session, region, policy_name, workflow_name, start_time, Interval, description):
    network_url, vcenter = get_url(region=region)
    url = network_url + "/nwrestapi/v3/global/protectionpolicies/" + policy_name + "/workflows/" + workflow_name + "/op/backup"
    payload = json.dumps(
        {
            "actionOverrides": [
                {
                    "action": "clone",
                    "commadLineArguments": "-y 3 years"
                }
            ],
            "restart": True,
        }
    )
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(url=url, auth=session, headers=headers, data=payload, verify=False)


def create_group(session, region, group_name):
    network_url, vcenter = get_url(region=region)
    url = network_url + "/nwrestapi/v3/global/protectiongroups"
    payload = json.dumps(
        {
            "name": group_name,
            "backupOptimization": "Capacity",
            "dynamicAssociation": True,
            "vmwareWorkItemSelection": {
                "vCenterHostname": vcenter,
            },
            "workItemSource": "Static",
            "workItemSubType": "All",
            "workItemType": "VMware",
        }
    )
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(url=url, auth=session, headers=headers, data=payload, verify=False)


def get_policy(session, region):
    network_url, vcenter = get_url(region=region)
    url = network_url + "/nwrestapi/v3/global/protectionpolicies"
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.get(url=url, auth=session, headers=headers, verify=False)
    policy_list = response.json()
    return policy_list.get("protectionPolicies")


def get_backups(session, region, server_id):
    network_url, vcenter = get_url(region=region)
    url = network_url + "/nwrestapi/v3/global/vmware/vcenters/" + vcenter + "/protectedvms/" + server_id + "/backups"
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.get(url=url, auth=session, headers=headers, verify=False)
    backup_list = response.json().get("backups")
    backups = []
    for backup in backup_list:
        vm_name, vm_id = _split_vm_name_uuid(backup.get('vmInformation').get('vmName'))
        bu = {
            "id": backup.get("id"),
            "region": region,
            "vm_info": backup.get('vmInformation'),
            "type": backup.get('type'),
            "unit": backup.get('size').get('unit'),
            "size": backup.get('size').get('value'),
            "server_name": vm_name,
            "server_id": vm_id,
            "create_time": backup.get('creationTime'),
            "project_id": ""
        }
        backups.append(bu)

    return backups


def backup_recover(session, region, server_id, backup_id):
    network_url, vcenter = get_url(region=region)
    url = network_url + "/nwrestapi/v3/global/vmware/vcenters/" + vcenter + "/protectedvms/" + server_id + "/backups/" + backup_id + "/op/recover"
    headers = {
        'Content-Type': 'application/json'
    }
    payload = json.dumps(
        {
            "recoverMode": "Revert",
            "powerOn": True,
            "reconnectNic": False
        }
    )
    response = requests.post(url=url, auth=session, headers=headers, data=payload, verify=False)
