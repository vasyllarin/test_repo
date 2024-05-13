import requests
import openmeteo_requests
import requests_cache
from retry_requests import retry


GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search?name="


def weather(city):
    # Extract city latitude and longitude by city name:
    try:
        geo_url = f"{GEOCODING_URL}{city}"
        geo_data = requests.get(geo_url).json()
        lat = geo_data["results"][0]['latitude']
        lon = geo_data["results"][0]['longitude']
    except KeyError as e:
        print("There is no such city. Please update your input.")
        return None
    # Setup the Open-Meteo API client with cache and retry on error:
    cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
    retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
    openmeteo = openmeteo_requests.Client(session=retry_session)
    # Obtain responses from openmeteo based on city latitude and longitude:
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lat,
        "current": "temperature_2m"
    }
    responses = openmeteo.weather_api(url, params=params)
    response = responses[0]
    # Extract current temperature from the response:
    current = response.Current()
    current_temperature_2m = current.Variables(0).Value()
    return current_temperature_2m


# Usage example
city_example = "Berlin"
print(weather(city_example))
