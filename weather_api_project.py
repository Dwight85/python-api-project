import requests

# Your API Key
api_key = "665cddf9d45cdca1bb29ad3fe263e972"

def get_weather_data(city):
    # Construct the API URL
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print_weather_data(data)
        elif response.status_code == 401:
            print("Error: 401 - Unauthorized. Please check your API key.")
        elif response.status_code == 404:
            print("Error: 404 - City not found. Please check the city name.")
        else:
            print(f"Error: {response.status_code} - {response.reason}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def print_weather_data(data):
    # Extract and print weather details
    city_name = data.get("name", "Unknown")
    country = data["sys"].get("country", "Unknown")
    temp = data["main"]["temp"] - 273.15  # Convert from Kelvin to Celsius
    weather = data["weather"][0]["description"]
    print(f"\nWeather in {city_name}, {country}:")
    print(f"Temperature: {temp:.2f}°C")
    print(f"Condition: {weather.capitalize()}")

# Get user input for the city
city = input("Enter city name (e.g., Dover,US): ")
get_weather_data(city)