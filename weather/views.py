from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .utils import get_weather_data, check_extreme_weather, \
    get_average_temperature, get_average_humidity
from weather.models import WeatherData


def home_view(request, *args, **kwargs):
    city= request.GET.get('city') or 'bangalore'
    data = get_weather_data(city)
    weather_data = {
        'city': data['location']['name'],
        'region': data['location']['region'],
        'country': data['location']['country'],
        'lat': data['location']['lat'],
        'lon': data['location']['lon'],
        'localtime': data['location']['localtime'],
        'temperature': data['current']['temp_c'],
        'humidity': data['current']['humidity'],
        'condition': data['current']['condition']['text'],
        'wind_speed': data['current']['wind_kph'],
        'pressure': data['current']['pressure_mb']
    }
    WeatherData.objects.create(**weather_data)
    extreme_alert = check_extreme_weather(data)
    avg_temp = get_average_temperature(city)
    avg_humidity = get_average_humidity(city)
    context = {
        'city': city,
        'current_temperature': data['current']['temp_c'],
        'current_humidity': data['current']['humidity'],
        'wind_speed': data['current']['wind_kph'], 
        'average_temperature_last_24h': avg_temp,
        'average_humidity_last_24h': avg_humidity,
        'extreme_alert': extreme_alert
    }
    return render(request, 'home.html', context)
    # return JsonResponse()


