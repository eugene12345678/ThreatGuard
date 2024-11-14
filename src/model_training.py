import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model(data_path):
    """Train the machine learning model."""
    df = pd.read_csv(data_path)
    X = df[['hour', 'day_of_week']]
    y = df['status'].apply(lambda x: 1 if x == 'failure' else 0)  # Binary labels for threat detection

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Save the model
    joblib.dump(model, '../models/threat_detection_model.pkl')
    
    # Print the accuracy
    accuracy = model.score(X_test, y_test)
    print(f'Model accuracy: {accuracy:.2f}')

if __name__ == "__main__":
    train_model('../data/processed_data.csv')
