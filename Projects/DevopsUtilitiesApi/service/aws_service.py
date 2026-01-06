import boto3
from datetime import datetime, timezone, timedelta

def get_buckets_info():
    """
    This function retrieves the list of S3 buckets in the AWS account.
    Returns:
        list: A list of bucket names.
    """
    s3 = boto3.client('s3')
    buckets = s3.list_buckets()["Buckets"]

    new_buckets = []
    for bucket in buckets:
        bucket_name = bucket["Name"]   
        old_buckets = []
        bucket_creation_date = bucket["CreationDate"]
        current_time = datetime.now(timezone.utc).astimezone()
        ninty_days_ago= current_time - timedelta(days=90)
        if bucket_creation_date < ninty_days_ago:
            old_buckets.append(bucket_name)
        else:
            new_buckets.append(bucket_name)
       
        return{
            "total_buckets":len(buckets),
            "new_buckets":len(new_buckets),
            "old_buckets":len(old_buckets),
            "new_buckets_name":new_buckets,
            "old_buckets_name":old_buckets
        }
        