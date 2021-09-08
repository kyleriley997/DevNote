import boto3
import re

ecs_client = boto3.client('ecs', 'us-east-1')

clusters = ecs_client.list_clusters()['clusterArns']

for cluster in clusters:
    clusterName = cluster.split('/')[1]
    services = ecs_client.list_services(cluster=clusterName)['serviceArns']
    if services:
        service_description =     ecs_client.describe_services(cluster=cluster, services=services)
        print(service_description)


if services:
    service_names = ecs_client.describe_services(cluster=cluster, services=services)
    for service in service_names:
        print(service['desiredCount'])
        print(service['runningCount'])
    
for service in service_names:
    desired_count = service['desiredCount']
    running_count = service['runningCount']
    if desired_count != running_count:
        print(f'SERVICES RUNNING: {running_count}/{desired_count}')    
    
events = ecs_client.describe_services(cluster = cluster, services=services)['services'][0]['events']

for event in events:
    message = event['message']
    healthy = re.search('has reached a steady state', message)
    if healthy is None:
        print('###FAILED###')
        print('------------------')
        print(message)
        print('------------------')
        print('###FAILED###')
        print('                  ')
        print('                  ')
     
