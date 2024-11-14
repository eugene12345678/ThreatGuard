# ThreatGuard

ThreatGuard is a real-time threat detection system that leverages machine learning and behavioral analysis to monitor network activities and identify potential security threats. The system processes log data, trains a machine learning model for threat detection, and uses it in a real-time monitoring pipeline to alert about suspicious activities. 

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Configuration](#configuration)
- [Technologies Used](#technologies-used)
- [License](#license)

## Features
- **Data Preprocessing**: Cleans and prepares log data for training.
- **Machine Learning Model**: Trains a model to classify normal and suspicious activities.
- **Real-Time Monitoring**: Continuously monitors network logs and flags potential threats.
- **Web Dashboard** (Optional): Displays logs and alerts for easy monitoring.
- **Alert Notifications**: Generates alerts for suspicious activities.

## Installation

### Prerequisites
- Python 3.8 or higher
- Recommended: Virtual environment tool (e.g., `venv` or `conda`)

### Steps
1. **Clone the Repository**
```bash
https://github.com/eugene12345678/ThreatGuard.git
cd ThreatGuard
```
2. **Create a Virtual Environment**

```bash
python3 -m venv env
source env/bin/activate   # For Windows: env\Scripts\activate
```
3. **Install Dependencies**

```bash
pip install -r requirements.txt
```
4. **Set Up Sample Data**

Ensure data/sample_logs.csv exists with the correct format, or create it as described in Data Setup

## Usage

### 1. Preprocess Data
Clean and prepare your log data for machine learning model training.

```bash
python src/data_preprocessing.py
```
### 2. Train the Model
Train a machine learning model using the preprocessed data.
```bash
python src/model_training.py
```
### 3. Start Real-Time Monitoring
Run this script to start monitoring logs for suspicious activity.
```bash
python src/real_time_monitor.py
```
### 4. (Optional) Launch the Web Dashboard
For a GUI interface, start the Flask application:
```bash
python src/app.py
```
Then, open http://127.0.0.1:5000/alerts to view alerts.

## Configuration
- **Data Path:** Modify data_preprocessing.py to point to your data file if it’s not located at data/sample_logs.csv.
- **Model Save Path:** Adjust model_training.py if you want to save the model in a different directory.
- **Log File:** You can customize the log file path in - real_time_monitor.py to monitor a specific log file.

## Technologies Used
- **Python:** Core language for development
- **pandas:** Data manipulation and analysis
scikit-learn: Machine learning model building
- **Flask:** Web dashboard for displaying alerts
- **unittest:** Python's built-in testing framework for unit tests

## License
MIT License