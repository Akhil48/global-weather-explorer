from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        return data
    else:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        api_key = "f55fab8a312441d07d81429420640c48"  # Replace with your OpenWeatherMap API key
        city = request.form['city']
        weather_data = get_weather(api_key, city)
        return render_template('index.html', weather_data=weather_data)

    return render_template('index.html', weather_data=None)

if __name__ == "__main__":
    app.run(debug=True)
