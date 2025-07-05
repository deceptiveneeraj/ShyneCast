import requests
import datetime as dt
import os
from dotenv import load_dotenv

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

def get_weather_data(city='Indore'):
    try:
        load_dotenv()
        getdata = os.getenv('hi')
        
        if not getdata:
            return {'error': 'API key not found. Please check your .env file.'}
        
        def data(longStr):
            mid_index = (len(longStr) - 28) // 2
            str = longStr[mid_index:mid_index + 32]
            return str

        restring = data(getdata)
        retext = restring[::-1]

        url = BASE_URL + "appid=" + retext + "&q=" + city
        response = requests.get(url)
        
        # Check if request was successful
        if response.status_code != 200:
            return {'error': f'API request failed with status code: {response.status_code}'}
        
        response_data = response.json()

        # Check if city was found
        if 'main' not in response_data:
            return {'error': f'Weather information not available for {city}. Please check the city name.'}

        def kelvin_celsius(kelvin):
            return kelvin - 273.15

        temp_kelvin = response_data['main']['temp']
        temp_celsius = kelvin_celsius(temp_kelvin)
        feels_like_kelvin = response_data['main']['feels_like']
        feels_like_celsius = kelvin_celsius(feels_like_kelvin)
        min_kelvin = response_data['main']['temp_min']
        min_celsius = kelvin_celsius(min_kelvin)
        max_kelvin = response_data['main']['temp_max']
        max_celsius = kelvin_celsius(max_kelvin)
        humidity = response_data['main']['humidity']
        pressure = response_data['main']['pressure']
        visibility = response_data.get('visibility', 0) / 1000  # Convert to km
        wind_speed = response_data.get('wind', {}).get('speed', 0)
        description = response_data['weather'][0]['description']

        # Handle timezone and sunrise/sunset
        timezone_offset = response_data.get('timezone', 0)
        sunrise_time = dt.datetime.utcfromtimestamp(
            response_data['sys']['sunrise'] + timezone_offset
        )
        sunset_time = dt.datetime.utcfromtimestamp(
            response_data['sys']['sunset'] + timezone_offset
        )

        sunrise_time_formatted = sunrise_time.strftime('%I:%M %p')
        sunset_time_formatted = sunset_time.strftime('%I:%M %p')

        # Sea level might not always be available
        sea_level = response_data['main'].get('sea_level', response_data['main'].get('grnd_level', 0))

        return {
            'location': city,
            'temp_celsius': temp_celsius,
            'feels_like_celsius': feels_like_celsius,
            'min_celsius': min_celsius,
            'max_celsius': max_celsius,
            'humidity': humidity,
            'pressure': pressure,
            'visibility': visibility,
            'wind_speed': wind_speed,
            'description': description,
            'sunrise_time': sunrise_time_formatted,
            'sunset_time': sunset_time_formatted,
            'sea_level': sea_level
        }
    except requests.exceptions.RequestException as e:
        return {'error': f'Network error: {str(e)}'}
    except KeyError as e:
        return {'error': f'Missing data in API response: {str(e)}'}
    except Exception as e:
        return {'error': f'An unexpected error occurred: {str(e)}'}

# Call the function and print the result
# if __name__ == "__main__":
#     weather_data = get_weather_data()
#     print(weather_data)