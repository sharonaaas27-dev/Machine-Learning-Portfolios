from app.ml.content_based import ContentBasedFiltering
from app.ml.collaborative import CollaborativeFiltering
from app.ml.hybrid import HybridRecommender

_model_cache = {}


def get_content_model() -> ContentBasedFiltering:
    if "content" not in _model_cache:
        model = ContentBasedFiltering()
        if not model.load():
            from app.ml.data_loader import load_movies
            model.fit(load_movies())
            model.save()
        _model_cache["content"] = model
    return _model_cache["content"]


def get_collaborative_model() -> CollaborativeFiltering:
    if "collaborative" not in _model_cache:
        model = CollaborativeFiltering()
        if not model.load():
            from app.ml.data_loader import load_ratings
            model.fit(load_ratings())
            model.save()
        _model_cache["collaborative"] = model
    return _model_cache["collaborative"]


def get_hybrid_model() -> HybridRecommender:
    if "hybrid" not in _model_cache:
        model = HybridRecommender()
        cb = get_content_model()
        col = get_collaborative_model()
        model.content_based = cb
        model.collaborative = col
        _model_cache["hybrid"] = model
    return _model_cache["hybrid"]