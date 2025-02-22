from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import SystemMessage, HumanMessage
import requests

API_KEY = "65251b49046ee1e357ca8ea2a53e0b37"  # Replace with your OpenWeatherMap API Key
BASE_URL = "http://api.openweathermap.org/data/2.5/"

def get_country_city_uv(city: str, country: str = ""):
    """
    Get the names of the country, city, and the country's UV index.
    """
    location_url = f"{BASE_URL}weather?q={city},{country}&appid={API_KEY}"
    response = requests.get(location_url)
    if response.status_code != 200:
        return {"error": "City not found"}
    
    data = response.json()
    lat, lon = data['coord']['lat'], data['coord']['lon']
    
    uv_url = f"{BASE_URL}uvi?lat={lat}&lon={lon}&appid={API_KEY}"
    uv_response = requests.get(uv_url)
    if uv_response.status_code != 200:
        return {"error": "UV index data not available"}
    
    uv_data = uv_response.json()
    uv_index = uv_data.get("value", "N/A")
    
    return {
        "country": country,
        "city": city,
        "uv_index": uv_index
    }
