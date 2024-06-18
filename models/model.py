from typing import List
from datetime import datetime
from pydantic import BaseModel


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
