import boto3

ec2_client = boto3.client('ec2')

# describe_instances()
response = ec2_client.describe_instances()

instances = response['Reservations']

for instance in instances:
    print(instances['Instance'][0]['InstanceId'])

instance_ids = []

for instance in instances:
    instance_ids.append(instance['Instances'][0]['InstanceId'])

tag_creation = ec2_client.create_tags(
    Resources = 
    instance_ids,
    Tags = [
        {
            'Key': 'operatingHours', 
            'Value': 'start=(M-S,0); stop=(M-F,8); tz=et'
        }
    ]
)

response = ec2_client.describe_instances(
    Filters = [
        {
            'Name': 'group-name',
            'Values': [
                'security-test',
            ]
        },
    ]
)

