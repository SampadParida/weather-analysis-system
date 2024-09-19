import requests
from django.http import JsonResponse
from django.conf import settings

from datetime import datetime, timedelta
from .models import WeatherData



def get_weather_data(city):
    api_key = settings.WEATHER_API_KEY
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    return response.json()

def check_extreme_weather(data):
    temp = data['current']['temp_c']
    wind_speed = data['current']['wind_kph']

    # Check for extreme temperature
    if temp > 35 or temp < 0:
        return True
    
    # Check for extreme wind speed
    if wind_speed > 70:  # Example threshold for extreme wind
        return True

    return False

def get_average_temperature(city):
    end_time = datetime.now()
    start_time = end_time - timedelta(hours=24)
    
    temperature_data = WeatherData.objects.filter(
        city=city,
        timestamp__range=(start_time, end_time)
    ).values_list('temperature', flat=True)  
    
    if temperature_data:
        avg_temperature = sum(temperature_data) / len(temperature_data)
        return avg_temperature
    return None

def get_average_humidity(city):
    end_time = datetime.now()
    start_time = end_time - timedelta(hours=24)
    
    humidity_data = WeatherData.objects.filter(
        city=city,
        timestamp__range=(start_time, end_time)
    ).values_list('humidity', flat=True)
    
    if humidity_data:
        avg_humidity = sum(humidity_data) / len(humidity_data)
        return avg_humidity
    return None