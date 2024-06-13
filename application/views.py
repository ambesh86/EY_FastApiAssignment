# views.py
from fastapi import APIRouter, HTTPException, logger
from controllers import parallel_addition
from models import InputData, OutputData
from datetime import datetime

router = APIRouter()

@router.post("/addition/", response_model=OutputData)
def perform_addition(data: InputData):
    try:
        start_time = datetime.now()
        result = parallel_addition(data.payload)
        end_time = datetime.now()
        return OutputData(
            Batched=data.Batched,
            response=result,
            Status="completed",
            started_at=start_time,
            completed_at=end_time,
        )
    except Exception as e:
        logger.error(f"Error in perform_addition: {e}")
        raise HTTPException(status_code=500, detail="Error occurred during addition")
