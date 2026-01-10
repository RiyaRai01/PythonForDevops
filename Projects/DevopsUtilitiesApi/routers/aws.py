from service.aws_service import (
    get_buckets_info, 
    get_ec2_instances_info,
    start_instance,
    stop_instance,
    reboot_instance,
    monitor_instance,
    unmonitor_instance,)
from fastapi import APIRouter,HTTPException

router = APIRouter()

@router.get("/s3Info",status_code=200)
def get_s3_info():
    try:
        buckets_info = get_buckets_info()
        return buckets_info
    except Exception as e:
        raise HTTPException(status_code=500, detail="INTERNAL SERVER ERROR")

@router.get("/ec2Info",status_code=200)
def get_ec2_info():
    try:
        print(type(get_ec2_instances_info))
        ec2_info = get_ec2_instances_info()
        return ec2_info
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="INTERNAL SERVER ERROR")
 
@router.post("/ec2/startEc2/{instance_id}",status_code=200)    
def start_ec2(instance_id:str):
    try:
        start_instance(instance_id)
        return {"message":f"Instance {instance_id} started successfully"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="INTERNAL SERVER ERROR")

@router.post("/ec2/stopEc2/{instance_id}",status_code=200)
def stop_ec2(instance_id:str):    
    try:
        stop_instance(instance_id)
        return {"message":f"Instance {instance_id} stopped successfully"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="INTERNAL SERVER ERROR")
    

@router.post("/ec2/rebootEc2/{instance_id}",status_code=200)
def reboot_ec2(instance_id:str):    
    try:
        reboot_instance(instance_id)
        return {"message":f"Instance {instance_id} rebooted successfully"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="INTERNAL SERVER ERROR")
    
@router.post("/ec2/monitorEc2/{instance_id}",status_code=200)    
def monitor_ec2(instance_id:str):    
    try:
        monitor_instance(instance_id)
        return {"message":f"Instance {instance_id} monitoring enabled successfully"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="INTERNAL SERVER ERROR")     

@router.post("/ec2/unmonitorEc2/{instance_id}",status_code=200)
def unmonitor_ec2(instance_id:str):    
    try:
        unmonitor_instance(instance_id)
        return {"message":f"Instance {instance_id} monitoring disabled successfully"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="INTERNAL SERVER ERROR")       
    