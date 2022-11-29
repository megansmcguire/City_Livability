#Pull weather data for a location and a time period from Open Meteo API
import pandas as pd
import requests

def get_weather(latitude, longitude, start_date, end_date):
    request_url = f'''
https://archive-api.open-meteo.com/v1/era5?latitude={latitude}&longitude={longitude}&start_date={start_date}&end_date={end_date}&hourly=temperature_2m,relativehumidity_2m,precipitation,windspeed_10m&timezone=auto&temperature_unit=fahrenheit&windspeed_unit=mph&precipitation_unit=inch
'''
    x = requests.get(request_url.strip())
    data = x.json()
    df = pd.DataFrame.from_dict(data['hourly'])
    return df
