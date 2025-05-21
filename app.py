from flask import Flask, request, jsonify, render_template
import numpy as np
import pickle
import pandas as pd

# Load the trained model
with open('newmodel.pkl', 'rb') as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the request
    data = request.get_json(force=True)
    
    # Extract features from data
    features = [data['UNIXTime'], data['Temperature'], data['Pressure'],
                data['Humidity'], data['WindDirection(Degrees)'], data['Speed']]
    
    # features = [ data['Temperature'], data['Pressure'],
    #             data['Humidity'], data['WindDirection(Degrees)'], data['Speed']]
    
    
    # Convert features into DataFrame for prediction
    feature_array = np.array(features).reshape(1, -1)
    feature_df = pd.DataFrame(feature_array, columns=['UNIXTime', 'Temperature', 'Pressure', 'Humidity', 'WindDirection(Degrees)', 'Speed'])
    # feature_df = pd.DataFrame(feature_array, columns=[ 'Temperature', 'Pressure', 'Humidity', 'WindDirection(Degrees)', 'Speed'])
    
    # Make prediction
    prediction = model.predict(feature_df)
    
    # Return the prediction as a JSON response
    return jsonify({'prediction': prediction[0]})


###

import pandas as pd
from flask import Flask, render_template, request, redirect, url_for
from prophet import Prophet
import pickle
import matplotlib.pyplot as plt
import io
import base64
from datetime import datetime




@app.route('/forecast', methods=['POST'])
def forecast_view():
    # Get the start and end dates from the form
    start_date_str = request.form.get('start_date')
    end_date_str = request.form.get('end_date')
    
    # Parse the dates
    date_format = '%Y-%m-%d'
    # date_format = '%m/%d/%Y %H:%M'
    start_date = datetime.strptime(start_date_str, date_format)
    end_date = datetime.strptime(end_date_str, date_format)
    
    # Calculate the number of days for the forecast
    days = (end_date - start_date).days
    
    if days <= 0:
        return "The end date must be after the start date."

    # Load the saved Prophet model
    with open('prophet_model.pkl', 'rb') as f:
        p = pickle.load(f)

    # Create a future dataframe
    # future = p.make_future_dataframe(periods=days, freq='D')
    future = p.make_future_dataframe(periods=1825)
    
    future = future[future['ds'] >= start_date]
    future = future[future['ds'] <= end_date]

    # Check if future dataframe has rows
    if future.empty:
        return "The future dataframe has no rows. Please check the dates."



    # Generate the forecast
    forecast = p.predict(future)

    # Plot the forecast components
    
    fig = p.plot_components(forecast)
    
    # Convert plot to PNG image
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    image_png = buf.getvalue()
    buf.close()

    # Encode PNG image to base64 string
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')

    return render_template('forecast.html', graph=graph)

if __name__ == '__main__':
    app.run(debug=True)



###







