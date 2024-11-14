import pandas as pd

def extract_features(df):
    """Extract features from the processed DataFrame."""
    return df[['hour', 'day_of_week']]
