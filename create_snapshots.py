#BOTO# SDK software devlopment kit a library of code to work with another program
import boto3
# Initializes the ec2 client and specifies the region
ec2_client = boto3.client('ec2' , region_name='us-east-1')
# calls ec2 client and calls the builtin function in BOTO3, contacts AWS and list the information
volumes = ec2_client.describe_volumes()
for volume in volumes['Volumes']:
    new_snapshot = ec2_client.create_snapshot(
        VolumeId=volume['VolumeId'],
    )
    print(new_snapshot)