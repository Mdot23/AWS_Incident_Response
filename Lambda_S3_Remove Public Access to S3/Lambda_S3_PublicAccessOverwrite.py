# https://forums.aws.amazon.com/thread.jspa?threadID=174199  - info on temporary file in Lambda system 
import boto3
import json
import os
import fileinput
import configparser
import logging
from pprint import pprint 

logger = logging.getLogger()
logger.setLevel(logging.INFO)

print("Loading Function...")


def lambda_handler(event, context):
    logger.info('event{}'.format(event))
    s3 = boto3.client('s3')
    RequestParams = event['requestParameters']['bucketPolicy']
    Bucketname = event['requestParameters']['bucketName']
    PolicyEvent = event['requestParameters']['bucketPolicy']['Statement'][0]['Effect'] 
    PolicyStatus = print("Policy Status is currently " + PolicyEvent)
    print(PolicyStatus)
    # Save JSON_Policy to path to this on Linux/Unix based filesystem for Lambda and change current directory to /var/tmp
    os.chdir("/var/tmp")
    Dir = os.getcwd()
    save_path = "/var/task"
    full_name = os.path.join(save_path,"JSON_Policy.JSON")
    # Performs the operation of configuring the JSON policy based on the input in the JSON formatted event, change to 'Deny' if 'Allow' in event
    with open(full_name,"r") as JSONfile:
        # Writes user changes or attempted changes to file 
        f = open('/tmp/OldPolicy.JSON','w+')
        f.write('%s' % RequestParams)
        s3.upload_file('/tmp/OldPolicy.JSON','test93','%s' %Bucketname)
        JSONDoc = json.load(JSONfile)
        JSONDoc = RequestParams 
        for i in JSONDoc['Statement']:
            if ['Effect'] == 'Allow' and ['Principal'] == '*': 
                JSONDoc['Effect'] = 'Deny' 
            # Convert the convereted JSON > python back into python > JSON 
                JSONDoc = json.dumps(JSONDoc)
                ModifyPolicy = s3.put_bucket_policy(Policy= JSONDoc, Bucket='%s' %Bucketname)
                print('Modifying policy...')
                print(JSONDoc)
                return ModifyPolicy
            else:
                print('Bucket not policy public')
    
   
    
   


"""logger = logging.getLogger()
logger.setLevel(logging.INFO)


print("Loading Function...")


def lambda_handler(event, context):
    logger.info('event{}'.format(event))
    s3 = boto3.client('s3')
    RequestParams = event['requestParameters']['bucketPolicy']
    Bucketname = event['requestParameters']['bucketName']
    PolicyEvent = event['requestParameters']['bucketPolicy']['Statement'][0]['Effect'] 
    PolicyStatus = print("Policy Status is currently " + PolicyEvent)
    print(PolicyStatus)
    # Save JSON_Policy to path to this on Linux/Unix based filesystem for Lambda and change current directory to /var/tmp
    os.chdir("/var/tmp")
    Dir = os.getcwd()
    save_path = "/var/task"
    full_name = os.path.join(save_path,"JSON_Policy.JSON")
    # Performs the operation of configuring the JSON policy based on the input in the JSON formatted event, change to 'Deny' if 'Allow' in event
    with open(full_name,"r") as JSONfile:
        JSONDoc = json.load(JSONfile)
        JSONDoc = RequestParams 
        s3.upload_file('/var/task/JSON_Policy.JSON','test93','%s' %Bucketname)
        if JSONDoc['Statement'][0]['Effect'] == 'Allow' and JSONDoc['Statement'][0]['Principal'] == '*':
            JSONDoc['Statement'][0]['Effect'] = 'Deny' 
            # Convert the convereted JSON > python back into python > JSON 
            JSONDoc = json.dumps(JSONDoc)
            ModifyPolicy = s3.put_bucket_policy(Policy= JSONDoc, Bucket='%s' %Bucketname)
            print('Modifying policy...')
            print(JSONDoc)
            return ModifyPolicy
        else:
            print('Bucket not policy public') """



"""import boto3
import json
import os
import fileinput
import configparser
import logging
from pprint import pprint 

logger = logging.getLogger()
logger.setLevel(logging.INFO)

print("Loading Function...")


def lambda_handler(event, context):
    logger.info('event{}'.format(event))
    s3 = boto3.client('s3')
    RequestParams = event['requestParameters']['bucketPolicy']
    Bucketname = event['requestParameters']['bucketName']
    PolicyEvent = event['requestParameters']['bucketPolicy']['Statement'][0]['Effect'] 
    PolicyStatus = print("Policy Status is currently " + PolicyEvent)
    print(PolicyStatus)
    # Save JSON_Policy to path to this on Linux/Unix based filesystem for Lambda and change current directory to /var/tmp
    os.chdir("/var/tmp")
    Dir = os.getcwd()
    save_path = "/var/task"
    full_name = os.path.join(save_path,"JSON_Policy.JSON")
    # Performs the operation of configuring the JSON policy based on the input in the JSON formatted event, change to 'Deny' if 'Allow' in event
    with open(full_name,"r") as JSONfile:
        JSONDoc = json.load(JSONfile)
        JSONDoc = RequestParams 
        if JSONDoc['Statement'][0]['Effect'] == 'Allow' and JSONDoc['Statement'][0]['Principal'] == '*':
            JSONDoc['Statement'][0]['Effect'] = 'Deny' 
            # Convert the convereted JSON > python back into python > JSON 
            JSONDoc = json.dumps(JSONDoc)
            ModifyPolicy = s3.put_bucket_policy(Policy= JSONDoc, Bucket='%s' %Bucketname)
            print('Modifying policy...')
            print(JSONDoc)
            return ModifyPolicy
        else:
            print('Bucket not policy public')"""
    
   
        
        
        
        
