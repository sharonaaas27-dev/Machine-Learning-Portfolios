from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
import os
from sklearn.metrics import classification_report, confusion_matrix
from features import X, y, vectorizer


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = LogisticRegression(max_iter=1000, class_weight='balanced')
model.fit(X_train, y_train)

# evaluate on test set and print classification report
y_test_pred = model.predict(X_test)
print("Confusion matrix (test):")
print(confusion_matrix(y_test, y_test_pred))
print("\nClassification report (test):")
print(classification_report(y_test, y_test_pred, digits=4))

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"Accuracy: {accuracy:.4f}")

# save into project-level models/ directory
models_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "models")
os.makedirs(models_dir, exist_ok=True)

joblib.dump(model, os.path.join(models_dir, "model.pkl"))
joblib.dump(vectorizer, os.path.join(models_dir, "vectorizer.pkl"))