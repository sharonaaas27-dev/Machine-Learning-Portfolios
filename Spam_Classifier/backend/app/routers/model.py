from fastapi import APIRouter, HTTPException, BackgroundTasks
from ..ml.metrics import load_metrics, get_best_model_name, get_model_comparison, get_confusion_matrix
from ..ml.train import train_model
from ..ml.model_loader import is_model_trained
from ..ml.data_loader import download_dataset
from ..schemas.prediction import PredictResponse
from ..ml.predict import predict_message

router = APIRouter(tags=["Model"])


@router.get("/health")
def health_check():
    return {
        "status": "healthy",
        "model_trained": is_model_trained(),
    }


@router.get("/metrics")
def get_metrics():
    metrics = load_metrics()
    if metrics is None:
        raise HTTPException(status_code=404, detail="Metrics not available. Train the model first.")
    return metrics


@router.post("/retrain")
def retrain_model(background_tasks: BackgroundTasks):
    try:
        metrics = train_model()
        return {"message": "Model retrained successfully", "metrics": {
            "best_model": metrics["best_model"],
            "accuracy": metrics["accuracy"],
            "precision": metrics["precision"],
            "recall": metrics["recall"],
            "f1_score": metrics["f1_score"],
        }}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Training failed: {str(e)}")


@router.get("/model/info")
def model_info():
    if not is_model_trained():
        raise HTTPException(status_code=404, detail="No model trained yet")
    metrics = load_metrics()
    return {
        "best_model": get_best_model_name(),
        "is_trained": True,
        "training_samples": metrics.get("training_samples", 0) if metrics else 0,
        "feature_count": metrics.get("feature_count", 0) if metrics else 0,
        "accuracy": metrics.get("accuracy", 0) if metrics else 0,
    }
