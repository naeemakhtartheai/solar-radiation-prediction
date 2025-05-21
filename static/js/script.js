document.getElementById('prediction-form').addEventListener('submit', async function (event) {
    event.preventDefault();

    const UNIXTime = document.getElementById('UNIXTime').value;
    const Temperature = document.getElementById('Temperature').value;
    const Pressure = document.getElementById('Pressure').value;
    const Humidity = document.getElementById('Humidity').value;
    const WindDirection = document.getElementById('WindDirection').value;
    const Speed = document.getElementById('Speed').value;

    const data = {
        UNIXTime: parseFloat(UNIXTime),
        Temperature: parseFloat(Temperature),
        Pressure: parseFloat(Pressure),
        Humidity: parseFloat(Humidity),
        'WindDirection(Degrees)': parseFloat(WindDirection),
        Speed: parseFloat(Speed)
    };

    const response = await fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });
    const result = await response.json();
    document.getElementById('result').innerText = 'Predicted Solar Radiation: ' + result.prediction;
});
