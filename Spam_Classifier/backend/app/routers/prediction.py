from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import desc
from typing import Optional
from ..database import get_db
from ..models.prediction import Prediction
from ..models.user import User
from ..schemas.prediction import PredictRequest, PredictResponse, PredictionHistory, PredictionList, BulkPredictRequest, BulkPredictResponse
from ..utils.security import get_current_user
from ..ml.predict import predict_message, predict_batch

router = APIRouter(tags=["Prediction"])


@router.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    result = predict_message(request.message)

    top_keywords_str = ", ".join(result["top_keywords"])

    prediction_record = Prediction(
        user_id=current_user.id,
        message=request.message,
        prediction=result["prediction"],
        confidence=result["confidence"],
        spam_probability=result["spam_probability"],
        ham_probability=result["ham_probability"],
        processing_time=result["processing_time"],
        top_keywords=top_keywords_str,
        explanation=result["explanation"],
    )
    db.add(prediction_record)
    db.commit()

    return PredictResponse(**result)


@router.post("/predict/bulk", response_model=BulkPredictResponse)
def predict_bulk(request: BulkPredictRequest, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    results = predict_batch(request.messages)

    for msg, res in zip(request.messages, results):
        top_keywords_str = ", ".join(res["top_keywords"])
        prediction_record = Prediction(
            user_id=current_user.id,
            message=msg,
            prediction=res["prediction"],
            confidence=res["confidence"],
            spam_probability=res["spam_probability"],
            ham_probability=res["ham_probability"],
            processing_time=res["processing_time"],
            top_keywords=top_keywords_str,
            explanation=res["explanation"],
        )
        db.add(prediction_record)
    db.commit()

    return BulkPredictResponse(results=results)


@router.get("/history", response_model=PredictionList)
def get_history(
    search: Optional[str] = None,
    page: int = 1,
    limit: int = 20,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    query = db.query(Prediction).filter(Prediction.user_id == current_user.id)

    if search:
        query = query.filter(Prediction.message.ilike(f"%{search}%"))

    total = query.count()
    predictions = (
        query.order_by(desc(Prediction.created_at))
        .offset((page - 1) * limit)
        .limit(limit)
        .all()
    )

    return PredictionList(total=total, predictions=predictions)


@router.delete("/history/{prediction_id}", status_code=204)
def delete_prediction(prediction_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    prediction = db.query(Prediction).filter(
        Prediction.id == prediction_id,
        Prediction.user_id == current_user.id,
    ).first()
    if not prediction:
        raise HTTPException(status_code=404, detail="Prediction not found")
    db.delete(prediction)
    db.commit()
    return None


@router.get("/history/export")
def export_history(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    predictions = db.query(Prediction).filter(Prediction.user_id == current_user.id).all()
    data = [
        {
            "message": p.message,
            "prediction": p.prediction,
            "confidence": p.confidence,
            "created_at": str(p.created_at),
        }
        for p in predictions
    ]
    return {"data": data}
