import boto3, json 

def Input_Operation():
    s3 = boto3.client('s3')
    BucketName = input("Bucket Name: ")

# JSON_Policy to be implemented into the function
# To specify all resources in the JSON policy (Specify all buckets to apply the policy to) use arn:aws:s3:::* 
    JSON_Policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Deny",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::%s/*" %BucketName
        }
    ]
}

    # Must be changed to JSON string 
    JSON_Policy = json.dumps(JSON_Policy)
    ModifyPolicy = s3.put_bucket_policy(Policy= JSON_Policy, Bucket='%s' %BucketName)
    print("Finished")
    return ModifyPolicy
    
if __name__ == "__main__":
    Input_Operation()


# For abstraction and polyphormism  
#class Input_Operation:
    #def __init__(self, BucketName):
        #self.name = BucketName

    # Method 
    #def PolicyOperation(BucketName):
        #return

