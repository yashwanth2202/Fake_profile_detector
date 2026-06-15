import pandas as pd
from sklearn.model_selection import train_test_split
from typing import Tuple
def preprocess_data(df: pd.DataFrame, target_column: str = 'fake', test_size: float = 0.2, random_state: int = 42) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """
    Preprocesses the data by separating features and target, and splitting into train/test sets.
    Args:
        df: The pandas DataFrame containing our loaded data.
        target_column: The name of the column we are trying to predict.
        test_size: The percentage of data to keep hidden for testing (e.g., 0.2 means 20%).
        random_state: A seed to ensure we get the same random split every time we run the code.
    Returns:
        X_train: The practice questions (80% of data).
        X_test: The exam questions (20% of data).
        y_train: The answers for the practice questions.
        y_test: The answers for the exam questions.
    """
    print("Preprocessing data...")
    # 1. Separate Features (X) and Target (y)
    X = df.drop(columns=[target_column])
    y = df[target_column]
    # 2. Split the data into Training and Testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    print(f"Data split successful!")
    print(f"Training set has {len(X_train)} rows.")
    print(f"Testing set has {len(X_test)} rows.")
    return X_train, X_test, y_train, y_test
