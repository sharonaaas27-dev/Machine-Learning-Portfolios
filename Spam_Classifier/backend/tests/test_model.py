import pytest
import numpy as np
from ..app.ml.preprocessing import preprocess_text, clean_text
from ..app.ml.predict import predict_message


class TestPreprocessing:
    def test_lowercase(self):
        assert clean_text("HELLO WORLD") == "hello world"

    def test_remove_urls(self):
        assert "http" not in clean_text("Check this http://example.com")

    def test_remove_punctuation(self):
        assert clean_text("hello!!!") == "hello"

    def test_remove_numbers(self):
        assert clean_text("test123") == "test"

    def test_empty_string(self):
        assert clean_text("") == ""


class TestPrediction:
    def test_spam_detection(self):
        result = predict_message("FREE FREE FREE! Claim your prize now!")
        assert result["prediction"] == "spam"
        assert result["confidence"] >= 0.5

    def test_ham_detection(self):
        result = predict_message("Hi Mom, I'll be home for dinner tonight.")
        assert result["prediction"] == "ham"

    def test_confidence_range(self):
        result = predict_message("Test message")
        assert 0 <= result["confidence"] <= 1

    def test_top_keywords_not_empty_for_spam(self):
        result = predict_message("You won a free gift card! Claim now!")
        assert len(result["top_keywords"]) > 0

    def test_explanation_present(self):
        result = predict_message("Test message")
        assert len(result["explanation"]) > 0
