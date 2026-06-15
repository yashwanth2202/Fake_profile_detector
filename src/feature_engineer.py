import pandas as pd
def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds new calculated features to the dataset to help the model learn better.
    Args:
        df: The input DataFrame containing raw profile statistics.
    Returns:
        A new DataFrame with the engineered features added.
    """
    print("Engineering new features...")
    # Create a copy so we don't modify the original dataframe directly
    df_engineered = df.copy()
    # Feature 1: Follower-to-Following Ratio
    # We add 1 to the denominator to avoid dividing by zero if they follow 0 people.
    df_engineered['follower_following_ratio'] = df_engineered['#followers'] / (df_engineered['#follows'] + 1)
    # Feature 2: Has Bio
    # 1 if they have a description, 0 if it's empty
    df_engineered['has_bio'] = (df_engineered['description length'] > 0).astype(int)
    # Feature 3: Has Full Name
    # 1 if they have words in their full name, 0 if empty
    df_engineered['has_fullname'] = (df_engineered['fullname words'] > 0).astype(int)
    
    # Feature 4: Posts-to-Following Ratio
    # High follows but 0 posts is a strong bot indicator
    df_engineered['posts_following_ratio'] = df_engineered['#posts'] / (df_engineered['#follows'] + 1)
    print(f"Successfully added 4 new engineered features!")
    return df_engineered
