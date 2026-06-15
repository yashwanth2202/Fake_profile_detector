import pandas as pd
from xgboost import XGBClassifier
import pickle
import os
def train_model(X_train: pd.DataFrame, y_train: pd.Series, model_save_path: str, xgb_params: dict):
    """
    Trains an XGBoost classifier and saves it to disk.
    Args:
        X_train: The practice questions (features for training).
        y_train: The answers for the practice questions (target for training).
        model_save_path: Where to save the trained model.
        xgb_params: Dictionary of hyperparameters for the XGBoost model.
    """
    print("Training the XGBoost model...")
    # Initialize the model with parameters from config
    model = XGBClassifier(**xgb_params)
    # Train the model (teach it the patterns)
    model.fit(X_train, y_train)
    print("Model training complete!")
    # Ensure the models directory exists
    os.makedirs(os.path.dirname(model_save_path), exist_ok=True)
    # Save the trained model to a file so we can use it later without retraining
    with open(model_save_path, 'wb') as f:
        pickle.dump(model, f)
    print(f"Model saved successfully to: {model_save_path}")
    return model
