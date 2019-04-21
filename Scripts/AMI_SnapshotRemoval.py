import boto3
import json
import pprint
import itertools # itertools.count() 
# counter = itertools.count()
# data(itertools.count(range(4)))
# data[0:None]

# block device mappings for image id
def image_snapshots():
    pp = pprint
    ec2 = boto3.resource('ec2')
    image = ec2.Image('ami-0b06c51f991216d9a') #ami needed for this to work
#   image.block_device_mappings # List snapshotId associated with the image
    data = image.block_device_mappings
    pp.pprint(data)
    # Create temporary list for return statement to work properly
    snapshots = []
    # For loop will to itterate over each dictionariy within the list
    for i, i in enumerate(d['Ebs']['SnapshotId'] for d in data):
        snapshots.append(i)
  # snapshot_ids = ','.join(snapshots)
    snapshot_ids = snapshots
 #  print(snapshot_ids)
    return snapshot_ids

snapshot_findings = image_snapshots()


def remove_snapshots(snapshot_findings):
    ec2 = boto3.resource('ec2')
    image = ec2.Image('ami-0b06c51f991216d9a')
    image.deregister()
    ec2 = boto3.resource('ec2')
    # For loop for snapshot findings
    for snap_id in snapshot_findings:
      snapshot = ec2.Snapshot('%s' %snap_id)
      snapshot.delete
      snapshot.delete()


      
