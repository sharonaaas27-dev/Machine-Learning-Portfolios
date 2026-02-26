from sklearn.metrics import classification_report, confusion_matrix
from train import y_test, y_pred
from preprocess import clean_text
from features import vectorizer
from train import model

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))


def predict_news(text):
    text = clean_text(text)
    text_vec = vectorizer.transform([text])
    prediction = model.predict(text_vec)
    
    if prediction[0] == 1:
        return "Fake News"
    else:
        return "Real News"
    
# Example usage
new_article = "Breaking: New study shows that drinking water can cure all diseases!"
result = predict_news(new_article)
print(f"The article is predicted to be: {result}")
