import boto3

s3_client = boto3.client("s3", 
    aws_access_key_id="AKIAWKOI3B6OY4WUIZWX", 
    aws_secret_access_key="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",
    )
    
bucket_location = s3_client.get_bucket_location(
            Bucket="pbl5-vy"
        )    