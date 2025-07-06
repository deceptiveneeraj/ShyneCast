import requests
import datetime as dt
import os
from dotenv import load_dotenv

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

def get_weather_data(city='Indore'):
    try:
        # Load environment variables
        load_dotenv()
        raw_key = os.getenv('hi')

        if not raw_key:
            return {'error': 'API key not found. Please check your .env file.'}

        # Extract and decode API key from hidden string
        def extract_key(encoded):
            mid_index = (len(encoded) - 28) // 2
            sub_str = encoded[mid_index:mid_index + 32]
            return sub_str[::-1]

        api_key = extract_key(raw_key)

        # Prepare request URL with metric units
        url = BASE_URL + f"appid={api_key}&q={city.strip()}&units=metric"
        response = requests.get(url)

        # Handle bad HTTP response
        if response.status_code != 200:
            return {'error': f'API request failed with status code: {response.status_code}'}

        response_data = response.json()

        # Check for presence of main weather info
        if 'main' not in response_data:
            return {'error': f'Weather information not available for {city}. Please check the city name.'}

        # Extract and process weather data
        main = response_data['main']
        wind = response_data.get('wind', {})
        sys_info = response_data.get('sys', {})

        weather_info = {
            'location': city,
            'temp_celsius': main.get('temp'),
            'feels_like_celsius': main.get('feels_like'),
            'min_celsius': main.get('temp_min'),
            'max_celsius': main.get('temp_max'),
            'humidity': main.get('humidity'),
            'pressure': main.get('pressure'),
            'visibility': response_data.get('visibility', 0) / 1000,  # in km
            'wind_speed': wind.get('speed', 0) * 3.6,  # Convert m/s to km/h
            'description': response_data['weather'][0]['description'].capitalize(),
            'sunrise_time': dt.datetime.utcfromtimestamp(sys_info.get('sunrise', 0) + response_data.get('timezone', 0)).strftime('%I:%M %p'),
            'sunset_time': dt.datetime.utcfromtimestamp(sys_info.get('sunset', 0) + response_data.get('timezone', 0)).strftime('%I:%M %p'),
            'sea_level': main.get('sea_level', main.get('grnd_level', 0)),
        }

        return weather_info

    except requests.exceptions.RequestException as e:
        return {'error': f'Network error: {str(e)}'}
    except KeyError as e:
        return {'error': f'Missing data in API response: {str(e)}'}
    except Exception as e:
        return {'error': f'An unexpected error occurred: {str(e)}'}

# Uncomment to test
# if __name__ == "__main__":
#     print(get_weather_data())
