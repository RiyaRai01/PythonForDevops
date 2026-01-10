from http.client import HTTPException
import boto3
from datetime import datetime, timezone, timedelta
from config import AWS_REGION
from botocore.exceptions import ClientError, NoCredentialsError, EndpointConnectionError


def get_buckets_info():
    """
    This function retrieves the list of S3 buckets in the AWS account.
    Returns:
        list: A list of bucket names.
    """
    try:
        s3 = boto3.client('s3')
        buckets = s3.list_buckets()["Buckets"]

        new_buckets = []
        old_buckets = []
        
        for bucket in buckets:
            
            bucket_name = bucket["Name"]   
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
    except NoCredentialsError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="AWS credentials not configured"
        )

    except ClientError as e:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=e.response["Error"]["Message"]
        )

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

        
def get_ec2_client():
    return boto3.client("ec2", region_name=AWS_REGION)        
        
def get_ec2_instances_info():
    """
    This function retrieves count and list of EC2 instances in the AWS account.
    Returns
        list: Count and list of EC2 instance IDs.
    """
  
    ec2 = get_ec2_client()
    response = ec2.describe_instances()
    instances = []
    total_instances = 0
    for reservation in response.get("Reservations",[]):
        for instance in reservation.get("Instances",[]):
            total_instances += 1
            instance_data ={
                "instance_id": instance.get("InstanceId"),
                "instance_type": instance.get("InstanceType"),
                "instance_state": instance.get("State",{}).get("Name"),
                "instance_avbility_zone": instance.get("Placement",{}).get("AvailabilityZone"),
                "instance_name": None
            }
            for tag in instance.get("Tags",[]):
                if tag["Key"] == "Name":
                    instance_data["instance_name"] = tag["Value"]
      
            instances.append(instance_data)

    return{
        "total_instances": total_instances,
        "instances": instances
    }
    
def start_instance(instance_id:str):
    """
    This function starts an EC2 instance given its instance ID.
    Args:
        instance_id (str): The ID of the EC2 instance to start.
    Returns:
        dict: Response from the start_instances call.
    """
    ec2 = get_ec2_client()
    ec2.start_instances(InstanceIds=[instance_id])
    return {"message": f"Instance {instance_id} has been started."}

def stop_instance(instance_id:str):
    """
    This function stops an EC2 instance given its instance ID.
    Args:
        instance_id (str): The ID of the EC2 instance to stop.
    Returns:
        dict: Response from the stop_instances call.
    """
    ec2 = get_ec2_client()
    ec2.stop_instances(InstanceIds=[instance_id])
    return {"message": f"Instance {instance_id} has been stopped."}

def reboot_instance(instance_id:str):
    """
    This function reboots an EC2 instance given its instance ID.
    Args:
        instance_id (str): The ID of the EC2 instance to reboot.
    Returns:
        dict: Response from the reboot_instances call.
    """
    ec2 = get_ec2_client()
    ec2.reboot_instances(InstanceIds=[instance_id])
    return {"message": f"Instance {instance_id} has been rebooted."}

def monitor_instance(instance_id:str):
    """
    This function enables detailed monitoring for an EC2 instance given its instance ID.
    Args:
        instance_id (str): The ID of the EC2 instance to monitor.
    Returns:
        dict: Response from the monitor_instances call.
    """
    ec2 = get_ec2_client()
    ec2.monitor_instances(InstanceIds=[instance_id])
    return {"message": f"Detailed monitoring enabled for instance {instance_id}."}

def unmonitor_instance(instance_id:str):
    """
    This function disables detailed monitoring for an EC2 instance given its instance ID.
    Args:
        instance_id (str): The ID of the EC2 instance to unmonitor.
    Returns:
        dict: Response from the unmonitor_instances call.
    """
    ec2 = get_ec2_client()
    ec2.unmonitor_instances(InstanceIds=[instance_id])
    return {"message": f"Detailed monitoring disabled for instance {instance_id}."}
    
    
    
    
    
