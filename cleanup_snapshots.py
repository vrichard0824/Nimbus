import boto3
from operator import itemgetter # built in module operator
# Gets ec2 information from the region where you have your snapshots
ec2_client = boto3.client('ec2' , region_name='us-east-1')
# Fetches all the snapshots only you created, AWS takes snapshots behind the scenes you can't see
snapshots = ec2_client.describe_snapshots(
    OwnerIds=['self'] # You can also use your account number.
)
# Sorts the snapshots by StartTime, reverse=True puts them in descending order.
sorted_by_date = sorted(snapshots['Snapshots'], key = itemgetter('StartTime'), reverse=True)
# I added to show the existing snapshots in  terminal before they are delete.
for snap in snapshots['Snapshots']:
    print(snap['StartTime'])
    print('###########')

# Deletes the last SnapShot
for snap in sorted_by_date[0:]:  # list in python start with 0
   response = ec2_client.delete_snapshot(
        SnapshotId=snap['SnapshotId']
    )
print(response)

# lookup what is iterating, dictionaries, and how list work in python