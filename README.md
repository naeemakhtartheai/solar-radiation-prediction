# Weather Forecast & Prediction Web App 🌦️

This is a Flask-based web application that provides two core functionalities:
1. **Prediction** using a trained machine learning model based on weather-related input features.
2. **Time-series forecasting** using Facebook's Prophet model to visualize trends over a selected future date range.

---

## 🚀 Features

- **Predict future outcomes** using weather input features.
- **Visualize time-series trends** (like temperature, humidity, etc.) using Prophet.
- Easy-to-use **HTML frontend** to submit data and view graphs.

---

## 🛠️ Tech Stack

- **Backend**: Flask, Python
- **Machine Learning**: scikit-learn, Prophet
- **Frontend**: HTML (Jinja2 templates)
- **Visualization**: Matplotlib

---

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/weather-forecast-app.git
   cd weather-forecast-app
Create and activate a virtual environment:


python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:


pip install -r requirements.txt
Ensure the following model files are present:

newmodel.pkl – your trained ML model for predictions

prophet_model.pkl – your trained Prophet time-series model

Run the app:


python app.py
Open your browser and go to:


http://127.0.0.1:5000/
📈 Predict API
Endpoint
POST /predict

Example Input (JSON)
json
Copy
Edit
{
  "UNIXTime": 1377986400,
  "Temperature": 73.5,
  "Pressure": 1015.1,
  "Humidity": 44,
  "WindDirection(Degrees)": 180,
  "Speed": 12.5
}
Example Output
json
Copy
Edit
{
  "prediction": 0.756
}
📅 Forecast Feature
Endpoint
POST /forecast

Form Input
Start Date: YYYY-MM-DD

End Date: YYYY-MM-DD

Output
Forecast trend graph rendered as an image

📁 Project Structure

weather-forecast-app/
│
├── templates/
│   ├── index.html
│   └── forecast.html
│
├── static/               # Optional: For CSS, JS, or images
├── app.py                # Main Flask app
├── newmodel.pkl          # ML model
├── prophet_model.pkl     # Prophet model
├── requirements.txt
└── README.md
