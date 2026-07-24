from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class PredictRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=10000)


class PredictResponse(BaseModel):
    prediction: str
    confidence: float
    spam_probability: float
    ham_probability: float
    processing_time: float
    top_keywords: List[str]
    explanation: str


class PredictionHistory(BaseModel):
    id: int
    message: str
    prediction: str
    confidence: float
    spam_probability: float
    ham_probability: float
    processing_time: float
    top_keywords: str
    explanation: str
    created_at: datetime

    class Config:
        from_attributes = True


class PredictionList(BaseModel):
    total: int
    predictions: List[PredictionHistory]


class BulkPredictRequest(BaseModel):
    messages: List[str] = Field(..., min_length=1, max_length=1000)


class BulkPredictResponse(BaseModel):
    results: List[PredictResponse]
