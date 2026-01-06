from fastapi import APIRouter,HTTPException
from service.metrics_service import get_system_metrics

router = APIRouter()

@router.get("/metrics",status_code=200)
def get_matrics():
    
    try:
        metrics = get_system_metrics()
        return metrics
    except Exception as e:
        raise HTTPException(status_code=500, detail="INTERNAL SERVER ERROR")