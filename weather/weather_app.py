import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    print(data)  # Print the API response for troubleshooting

    if response.status_code == 200:
        return data
    else:
        return None

def display_weather(weather_data):
    if weather_data:
        print(f"Weather in {weather_data['name']}:")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Description: {weather_data['weather'][0]['description']}")
    else:
        print("Failed to fetch weather data.")

if __name__ == "__main__":
    api_key = "f55fab8a312441d07d81429420640c48"
    city = input("Enter city name: ")

    weather_data = get_weather(api_key, city)

    display_weather(weather_data)
