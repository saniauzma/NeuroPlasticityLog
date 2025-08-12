import random
import threading
import time
from mcp.server import Server

server = Server("Mock Weather Server")

# In-memory storage for latest weather
latest_weather_data = {}

# Tool: Generate mock weather for a city
@server.tool("get_weather")
def get_weather(city: str):
    data = generate_mock_weather(city)
    latest_weather_data[city.lower()] = data
    return data

# Resource: Latest stored weather
@server.resource("latest_weather")
def latest_weather():
    if not latest_weather_data:
        return "No weather data yet. Call get_weather(city) first."
    return latest_weather_data

def generate_mock_weather(city):
    return {
        "city": city,
        "temp": round(random.uniform(20, 35), 1),  # °C
        "description": random.choice(["sunny", "cloudy", "light rain", "thunderstorm"])
    }

# Push updates every 10 seconds (for demo)
def push_updates():
    while True:
        time.sleep(10)
        for city in list(latest_weather_data.keys()):
            updated_data = generate_mock_weather(city)
            latest_weather_data[city] = updated_data
            server.push_resource_update("latest_weather", updated_data)

# Background thread for pushing updates
threading.Thread(target=push_updates, daemon=True).start()

if __name__ == "__main__":
    server.run_stdio()
