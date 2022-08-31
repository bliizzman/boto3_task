import boto3
import time

ec2 = boto3.client(
    'ec2',
    'eu-central-1',
    aws_secret_access_key='********',
    aws_access_key_id='***********'
)

resp = ec2.create_key_pair(KeyName = 'boto')
print(resp)

file = open('boto.pem', 'w')
file.write(resp['KeyMaterial'])
file.close

ec2_resource = boto3.resource(
    'ec2',
    'eu-central-1',
    aws_secret_access_key='********',
    aws_access_key_id='*********'
    )
print(ec2_resource)

instances = ec2_resource.create_instances(
    ImageId = 'ami-065deacbcaac64cf2',
        MinCount = 1,
        MaxCount = 1,
        InstanceType = 't2.micro',
        KeyName = 'boto'
)
print(instances)

id = instances[0].id
print(id)

time.sleep(10)

response = ec2.describe_instances(InstanceIds=[id])
print(response)

inst_info = response['Reservations'][0]['Instances'][0]
print(inst_info)

time.sleep(10)

term = ec2.terminate_instances(InstanceIds=[id])
print(term)

del_key = ec2.delete_key_pair(KeyName='boto')
print(del_key)
