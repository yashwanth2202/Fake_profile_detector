import pandas as pd
from sklearn.metrics import accuracy_score, classification_report

def evaluate_model(model, X_test: pd.DataFrame, y_test: pd.Series):
    """
    Evaluates the trained model on the unseen test data.
    
    Args:
        model: The trained machine learning model.
        X_test: The exam questions (features).
        y_test: The real answers (target).
    """
    print("Evaluating the model on the test data...")
    
    # Make the model predict the answers for the test questions
    predictions = model.predict(X_test)
    
    # Compare the model's predictions to the real answers (y_test)
    accuracy = accuracy_score(y_test, predictions)
    
    print(f"Model Accuracy: {accuracy * 100:.2f}%")
    print("\nDetailed Report:")
    print(classification_report(y_test, predictions))
    
    return accuracy
