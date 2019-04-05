#!/usr/bin/env python3

import boto3
import os

ALARM_PREFIX = None
MAX_RECORDS = 50

CLOUDWATCH_BASE_URL = ('https://console.aws.amazon.com/cloudwatch/home#'
                       'alarm:alarmFilter=inAlarm;name')

request = {
    'StateValue': 'ALARM',
    'MaxRecords': MAX_RECORDS,
}

if ALARM_PREFIX:
    request['AlarmNamePrefix'] = ALARM_PREFIX

client = boto3.client('cloudwatch')

response = client.describe_alarms(**request)

fired_alarms = [alarm['AlarmName'] for alarm in response['MetricAlarms']]

if fired_alarms:
    print('Cloudwatch  •  %s' % len(fired_alarms))
else:
    print('Cloudwatch  •  OK')
print('---')

for alarm in fired_alarms:
    print('{0} | href={1}={0}'.format(alarm, CLOUDWATCH_BASE_URL))
