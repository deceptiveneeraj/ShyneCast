# ShyneCast - Beautiful Weather Forecast App

A modern, responsive weather forecast web application built with Django that provides real-time weather information with an elegant user interface.

## Features

- **Real-time Weather Data**: Get current weather conditions for any city worldwide
- **Beautiful UI**: Modern, responsive design with animated particles and smooth transitions
- **Mobile-Friendly**: Fully responsive design that works perfectly on all devices
- **Search Functionality**: Search for weather in any city with auto-suggestions
- **Detailed Weather Information**: 
  - Current temperature and "feels like" temperature
  - Min/Max temperatures
  - Humidity and pressure
  - Wind speed and visibility
  - Sunrise and sunset times
  - Sea level information
- **Dynamic Weather Icons**: Icons change based on weather conditions
- **Live Date/Time**: Real-time date and time display
- **Quick City Access**: Pre-configured buttons for popular Indian cities

## Tech Stack

- **Backend**: Django 5.2
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Styling**: Custom CSS with modern design principles
- **Icons**: Font Awesome 6.4.0
- **Fonts**: Google Fonts (Inter)
- **Deployment**: WhiteNoise for static file serving

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd shynecast
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv weather_env
   source weather_env/bin/activate  # On Windows: weather_env\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install django whitenoise
   ```

4. **Set up the weather API**
   - Create a `weather.py` file in the `weather` app directory
   - Implement the `get_weather_data()` function to fetch weather data from your preferred API
   - You'll need to sign up for a weather API service (like OpenWeatherMap, WeatherAPI, etc.)

5. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

6. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

7. **Start the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Open your browser and go to `http://127.0.0.1:8000/`

## Project Structure

```
shynecast/
├── shynecast/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── weather/
│   ├── templates/
│       └── index.html
│   ├── views.py
│   ├── weather.py      # Weather API integration (to be implemented)
│   ├── apps.py
│   ├── admin.py
│   ├── models.py
│   └── tests.py
├── static/
│   ├── css/
│   │   └── main.css    # Custom styles (to be added)
│   └── img/
│       └── cloudy.png  # Favicon
├── manage.py
├── requirements.txt
└── README.md
```

## Configuration

### Settings

The application is configured with:
- **DEBUG**: Set to `True` for development (change to `False` for production)
- **ALLOWED_HOSTS**: Set to `["*"]` for development
- **Static Files**: Configured with WhiteNoise for production deployment
- **Database**: SQLite for development (can be changed for production)

### Weather API Integration

Create a `weather.py` file in the `weather` app with the following structure:

```python
import requests
from datetime import datetime

def get_weather_data(city):
    """
    Fetch weather data for a given city.
    Returns a dictionary with weather information or error message.
    """
    try:
        # Your weather API integration here
        # Return dictionary with required keys:
        return {
            'temp_celsius': temperature,
            'feels_like_celsius': feels_like,
            'min_celsius': min_temp,
            'max_celsius': max_temp,
            'humidity': humidity,
            'pressure': pressure,
            'visibility': visibility,
            'wind_speed': wind_speed,
            'sea_level': sea_level,
            'sunrise_time': sunrise,
            'sunset_time': sunset,
            'description': description
        }
    except Exception as e:
        return {'error': f'Unable to fetch weather data: {str(e)}'}
```

## Features in Detail

### Responsive Design
- Desktop: Full sidebar with weather details
- Mobile: Collapsible search with optimized layout
- Tablet: Adaptive layout for medium screens

### Weather Icons
Dynamic icons that change based on weather conditions:
- ☀️ Clear/Sunny
- ☁️ Cloudy/Overcast
- 🌧️ Rain/Drizzle
- ❄️ Snow/Sleet
- ⛈️ Thunderstorm
- 🌫️ Mist/Fog/Haze

### Interactive Elements
- Animated particle background
- Smooth hover effects on buttons
- Mobile-friendly search toggle
- Real-time date/time updates

## Deployment

### Production Deployment

1. **Update settings for production**:
   ```python
   DEBUG = False
   ALLOWED_HOSTS = ['your-domain.com', 'www.your-domain.com']
   ```

2. **Configure static files**:
   ```bash
   python manage.py collectstatic --noinput
   ```

3. **Set up environment variables**:
   - `SECRET_KEY`
   - `DEBUG`
   - Weather API keys

### Deployment Platforms
- **Heroku**: Ready for Heroku deployment with WhiteNoise
- **Railway**: Compatible with Railway deployment
- **DigitalOcean**: Can be deployed on DigitalOcean App Platform
- **AWS**: Compatible with AWS Elastic Beanstalk

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Font Awesome for the beautiful icons
- Google Fonts for the Inter font family
- Weather API providers for real-time data
- Django community for the excellent framework

## Support

If you encounter any issues or have questions:
1. Check the existing issues on GitHub
2. Create a new issue with detailed information
3. Provide steps to reproduce any bugs

---

**ShyneCast** - Making weather beautiful, one forecast at a time! 🌤️