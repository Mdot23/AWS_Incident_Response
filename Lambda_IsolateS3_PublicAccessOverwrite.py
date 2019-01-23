# 1.) Create a script to remove Public Access to bucket = S#_PublicAccessDeny&JSON.py
# 2.) Implement logic to perform the operation in Lambda only if S3 Bucket is Public 
# 3.) Allow access to call, "GetBucketPolicyStatus" operation or else will generate "Access Denied" error message.
import boto3
import json
import os
import fileinput
import configparser
from pprint import pprint 



print("Loading Function...")


def lambda_handler(event, context):
    s3 = boto3.client('s3')
    Bucketname = event['requestParameters']['bucketName']
    PolicyEvent = event['requestParameters']['bucketPolicy']['Statement'][0]['Effect'] 
    PolicyStatus = print("Policy Status is currently " + PolicyEvent)
    print(PolicyStatus)
    JSON_Policy = open("JSON_Policy.JSON",'r')
    # Save JSON_Policy to path to this on Linux/Unix based filesystem for Lambda and change current directory to /var/tmp
    os.chdir("/var/tmp")
    Dir = os.getcwd()
    save_path = "/var/task"
    full_name = os.path.join(save_path,"JSON_Policy.JSON")
    with open(full_name,"r") as JSONfile:
        JSONDoc = json.load(JSONfile)
        JSONDoc['Statement'][0]["Resource"] = "arn:aws:s3:::%s/*" %Bucketname
        pprint(JSONDoc)
    # Convert the convereted JSON > python back into python > JSON 
    JSONDoc = json.dumps(JSONDoc)
    ModifyPolicy = s3.put_bucket_policy(Policy= JSONDoc, Bucket='%s' %Bucketname)
    if PolicyEvent == "Allow":
        print("Modifying Policy...")
        return ModifyPolicy
    else:
        print("Bucket policy not public")
    

   
  
    

