from django.shortcuts import render
from django.http import HttpRequest
from .weather import get_weather_data

# Create your views here.
def homeview(request: HttpRequest, city_name: str = "Indore"):
    # Get city from URL parameter or use default
    city = city_name if city_name else "Indore"
    
    # Handle city parameter from GET request (for search functionality)
    if request.GET.get('city'):
        city = request.GET.get('city')
    
    data = get_weather_data(city)
    
    # Check if there's an error in the weather data
    if 'error' in data:
        context = {
            'error': data['error'],
            'location': city
        }
    else:
        context = {
            'location': city,
            'temp_celsius': round(data["temp_celsius"], 2),
            'feels_like_celsius': round(data["feels_like_celsius"], 2),
            'min_celsius': round(data["min_celsius"], 2),
            'max_celsius': round(data["max_celsius"], 2),
            'humidity': data["humidity"],
            'pressure': data["pressure"],
            'visibility': data["visibility"],
            'wind_speed': data["wind_speed"],
            'sea_level': data.get("sea_level", "N/A"),  # Use get() for optional fields
            'sunrise_time': data["sunrise_time"],
            'sunset_time': data["sunset_time"],
            'description': data["description"].title()  # Capitalize description
        }
    
    return render(request, "index.html", context)