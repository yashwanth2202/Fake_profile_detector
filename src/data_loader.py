import pandas as pd
import os

def load_data(filepath: str) -> pd.DataFrame:
    """
    Loads a CSV file into a pandas DataFrame.
    
    Args:
        filepath: The path to the CSV file.
        
    Returns:
        A pandas DataFrame containing the data.
    """
    print(f"Loading data from: {filepath}")
    
    # Check if the file actually exists before trying to load it
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Oops! We couldn't find the data file at: {filepath}")
        
    # Read the CSV file into a DataFrame
    # Think of a DataFrame like an Excel spreadsheet but in Python
    df = pd.read_csv(filepath)
    
    print(f"Successfully loaded {len(df)} rows and {len(df.columns)} columns.")
    return df
