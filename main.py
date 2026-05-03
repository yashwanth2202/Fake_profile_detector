import config
from src.data_loader import load_data
from src.feature_engineer import engineer_features
from src.preprocessor import preprocess_data
from src.model_trainer import train_model

print("--- Step 2: Loading Data ---")
df = load_data(config.RAW_DATA_PATH)
print("----------------------------\n")

print("--- Step 2.5: Feature Engineering ---")
df = engineer_features(df)
print("-------------------------------------\n")

print("--- Step 3: Preprocessing Data ---")
X_train, X_test, y_train, y_test = preprocess_data(
    df, 
    test_size=config.TEST_SIZE, 
    random_state=config.RANDOM_STATE
)
print("----------------------------------\n")

print("--- Step 4: Training the Model ---")
model = train_model(
    X_train, 
    y_train, 
    model_save_path=config.MODEL_SAVE_PATH, 
    xgb_params=config.XGB_PARAMS
)
print("----------------------------------\n")

print("--- Step 5: Testing and Evaluating ---")
from src.visualiser import evaluate_model
evaluate_model(model, X_test, y_test)
print("--------------------------------------\n")