import requests
import os
API_KEY = os.environ.get("OWM_API_KEY")

def get_weather_data(lat_lon):
    lat = lat_lon[0]
    lon = lat_lon[1]

    param = {
        "lat": lat,
        "lon": lon,
        "exclude": "current,minutely,daily",
        "appid": API_KEY
    }

    response = requests.get(url='https://api.openweathermap.org/data/3.0/onecall', params=param)
    response.raise_for_status()
    data = response.json()
    return data
