import pickle
import pandas as pd

def load_model(model_path: str):
    """Loads the trained model from disk."""
    with open(model_path, 'rb') as f:
        return pickle.load(f)

def predict_profile(model, features: dict) -> str:
    """
    Predicts if a profile is real or fake based on its features.
    
    Args:
        model: The trained model.
        features: Dictionary containing the 11 required features.
        
    Returns:
        "Fake" or "Real"
    """
    # Create a DataFrame with a single row
    # The columns must match exactly what the model was trained on
    expected_columns = [
        'profile pic', 'nums/length username', 'fullname words',
        'nums/length fullname', 'name==username', 'description length',
        'external URL', 'private', '#posts', '#followers', '#follows'
    ]
    
    # Construct DataFrame
    df = pd.DataFrame([features], columns=expected_columns)
    
    # Apply the same feature engineering we used during training!
    from src.feature_engineer import engineer_features
    df = engineer_features(df)
    
    # Predict (returns an array, we take the first element)
    prediction = model.predict(df)[0]
    
    # 1 typically means Fake, 0 means Real based on our dataset target column 'fake'
    return "Fake" if prediction == 1 else "Real"
