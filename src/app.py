from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/alerts')
def get_alerts():
    """Return a list of alerts."""
    alerts = pd.read_csv('../data/sample_logs.csv')  # Replace with actual alerts data
    return jsonify(alerts.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
