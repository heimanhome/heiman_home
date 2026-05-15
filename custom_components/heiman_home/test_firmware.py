#!/usr/bin/env python3
"""Test script to check firmware upgrade info."""

import json

# Simulate the firmware list response from API
firmware_response = {
    'message': 'success',
    'result': [{
        'id': '1972646416676724736',
        'photoUrl': 'https://api.heiman.cn/api-saas/file/870bb4798ce7ad17086775195e260e4c.jpg?accessKey=c22d26782ab650bdca89db83d32ac41e',
        'name': '405548f0f9ac',
        'deviceName': 'Smart Gateway',
        'productName': '无线级联网关WS3GW-R（868MHz）',
        'state': {'text': 'Online', 'value': 'online'},
        'currentVersion': '1.1.6',
        'currentProperties': {'MCU': '1.1.4'},
        'upgradeTasks': [{
            'upgradeVersion': '1.1.7',
            'upgradeProperties': [],
            'taskId': '2052324208243363840',
            'upgradeHistoryId': '6f1d20dea9781305176ed88e317f0bbf',
            'upgradeTaskState': {'text': '等待升级', 'value': 'waiting'}
        }]
    }],
    'status': 200,
    'timestamp': 1778147936268
}

# Check what the coordinator extracts
for device_info in firmware_response['result']:
    device_id = device_info.get("deviceId") or device_info.get("id")
    latest_version = (
        device_info.get("latestVersion")
        or device_info.get("newVersion")
        or device_info.get("targetVersion")
    )
    
    print(f"Device ID: {device_id}")
    print(f"Latest version from direct fields: {latest_version}")
    
    # Check upgradeTasks
    upgrade_tasks = device_info.get("upgradeTasks", [])
    if upgrade_tasks:
        for task in upgrade_tasks:
            upgrade_version = task.get("upgradeVersion")
            print(f"Upgrade version from upgradeTasks: {upgrade_version}")
    
    print("-" * 50)
