# main.py

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

# Load dataset
def load_data(path):
    df = pd.read_csv(path)
    df['date'] = pd.to_datetime(df['date'])
    df['day'] = df['date'].map(pd.Timestamp.toordinal)
    return df

# Train model
def train_model(df):
    X = df[['day']]
    y = df['temp']

    model = LinearRegression()
    model.fit(X, y)

    return model

# Save model
def save_model(model, filename='model.pkl'):
    joblib.dump(model, filename)

# Load model
def load_model(filename='model.pkl'):
    return joblib.load(filename)

# Predict temperature
def predict_temperature(model, date_input):
    date = pd.to_datetime(date_input)
    day = np.array([[date.toordinal()]])
    prediction = model.predict(day)
    return prediction[0]


# Run training when executed directly
if __name__ == "__main__":
    df = load_data("large_temperature_dataset.csv")
    model = train_model(df)
    save_model(model)
    print("Model trained and saved as model.pkl")