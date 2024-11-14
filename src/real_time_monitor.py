import pandas as pd
import joblib
import time
from alerts import alert_admin

def fetch_new_logs():
    """Simulate fetching new logs; in reality, replace this with actual log fetching."""
    return pd.read_csv('../data/sample_logs.csv')  # Replace with real-time log fetching logic

def monitor_system(model):
    """Monitor system for real-time threats."""
    while True:
        new_data = fetch_new_logs()
        features = new_data[['hour', 'day_of_week']]
        predictions = model.predict(features)
        
        for i, pred in enumerate(predictions):
            if pred == 1:  # Assuming 1 indicates a threat
                alert_admin(new_data.iloc[i])  # Alert with the relevant log entry
        
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    model = joblib.load('../models/threat_detection_model.pkl')
    monitor_system(model)
