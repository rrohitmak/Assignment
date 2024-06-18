from typing import List
import logging
from datetime import datetime
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from models.model import SumModel

router = APIRouter()

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

sum_model = SumModel()


class BatchRequest(BaseModel):
    """Batch Request"""
    batchid: str
    payload: List[List[int]]


class BatchResponse(BaseModel):
    """Batch Response"""
    batchid: str
    response: List[int]
    status: str
    started_at: datetime
    completed_at: datetime


@ router.post("/get-sum", response_model=BatchResponse)
async def generate_sum(request: BatchRequest):
    """Generates a random OTP of the given length"""
    start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        logger.debug(f"Received request with batchid: {
            request.batchid} and payload: {request.payload}")
        num_list = request.payload
        sum_list = sum_model.sum_list(num_list)
        response = {"batchid": request.batchid, "response": sum_list,
                    "status": "complete", "started_at": start_time, "completed_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        logger.debug(f"Response prepared: {response}")
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    return JSONResponse(response)
