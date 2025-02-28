# Using the OpenWeatherMap API with Python

## Overview
This repository contains a Jupyter Notebook demonstrating how to access weather data using the [OpenWeatherMap API](https://openweathermap.org/api). The notebook walks through the process of retrieving weather data for London and provides exercises to explore additional API functionalities.

## Author
**Dr. Renju Mathew**  
**Version:** 1.2 (2023-05-04)

## Features
- Retrieve current weather data for a given city
- Extract latitude and longitude using the Geocoding API
- Convert temperature from Kelvin to Celsius
- Store weather data for multiple cities in a DataFrame
- Retrieve air pollution data
- Investigate historical weather data

## Questions Explored
The notebook provides a full solution for checking the current weather in London and includes prompts for further exploration:
1. How do you check the current weather data in London?
2. How would you find the temperature in different cities and store them in a DataFrame?
3. What else can you find out about the weather in different cities (e.g., air quality data)?
4. What happens if you try to get historical weather data?
5. What other features does the API offer?
6. How can you analyze and utilize the collected weather data?

## Getting Started

### Prerequisites
- Python 3.x
- Jupyter Notebook
- `requests` library

Install the required package using:
```bash
pip install requests
```

### API Key
To use the OpenWeatherMap API, you need an API key:
1. Sign up at [OpenWeatherMap](https://home.openweathermap.org/users/sign_up) and obtain an API key.
2. Save your API key in a file named `API_key.txt` or manually enter it in the notebook.

## Example Usage
### Checking the Current Weather in London
1. Retrieve latitude and longitude using the Geocoding API:
    ```python
    city_name = 'London'
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={API_key}"
    response = requests.get(url)
    lat, lon = response.json()[0]['lat'], response.json()[0]['lon']
    ```
2. Fetch the weather data:
    ```python
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}"
    weather_data = requests.get(url).json()
    ```
3. Convert temperature to Celsius:
    ```python
    kelvin_conversion = -273.15
    temp_celsius = weather_data["main"]["temp"] + kelvin_conversion
    ```

## Additional Functionality
- Modify the API call to include temperature units in Celsius:
    ```python
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric"
    ```
- Retrieve air pollution data:
    ```python
    url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_key}"
    response = requests.get(url).json()
    ```
- Attempt to access historical weather data:
    ```python
    url = f"https://api.openweathermap.org/data/3.0/onecall/timemachine?lat={lat}&lon={lon}&dt=1643803200&appid={API_key}"
    response = requests.get(url).json()
    ```

## License
This project is licensed under the MIT License.

## Acknowledgements
Thanks to OpenWeatherMap for providing the API used in this project.

