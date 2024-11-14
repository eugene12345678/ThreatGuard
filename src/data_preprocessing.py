import pandas as pd

def load_data(file_path):
    """Load log data from a CSV file."""
    df = pd.read_csv(file_path)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df

def preprocess_data(df):
    """Clean and preprocess the data."""
    df['action'] = df['action'].astype('category')
    df['user_id'] = df['user_id'].astype('category')
    df['hour'] = df['timestamp'].dt.hour
    df['day_of_week'] = df['timestamp'].dt.dayofweek
    return df

if __name__ == "__main__":
    df = load_data('../data/sample_logs.csv')
    processed_df = preprocess_data(df)
    processed_df.to_csv('../data/processed_data.csv', index=False)
