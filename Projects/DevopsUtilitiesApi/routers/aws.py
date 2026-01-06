from service.aws_service import get_buckets_info
from fastapi import APIRouter,HTTPException

router = APIRouter()

@router.get("/s3Info",status_code=200)
def get_s3_info():
    try:
        buckets_info = get_buckets_info()
        return buckets_info
    except Exception as e:
        raise HTTPException(status_code=500, detail="INTERNAL SERVER ERROR")

