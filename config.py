import os

# Base paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
MODELS_DIR = os.path.join(BASE_DIR, "models")

# Data files
RAW_DATA_PATH = os.path.join(DATA_DIR, "dataset.csv")
PROCESSED_DATA_PATH = os.path.join(DATA_DIR, "processed_dataset.csv")

# Model configuration
MODEL_SAVE_PATH = os.path.join(MODELS_DIR, "model.pkl")
RANDOM_STATE = 42
TEST_SIZE = 0.2

# Baseline Model Hyperparameters (XGBoost)
XGB_PARAMS = {
    "n_estimators": 100,
    "max_depth": 6,
    "random_state": RANDOM_STATE,
    "eval_metric": "logloss"
}
