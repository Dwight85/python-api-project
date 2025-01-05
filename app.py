print("Flask app is starting...")
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace with your actual API key
API_KEY = "665cddf9d45cdca1bb29ad3fe263e972"

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    if request.method == "POST":
        city = request.form.get("city")
        if city:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                temp_kelvin = data["main"]["temp"]
                temp_celsius = temp_kelvin - 273.15
                temp_fahrenheit = (temp_kelvin - 273.15) * 9/5 + 32
                weather_data = {
                    "city": city,
                    "temperature_c": round(temp_celsius, 2),
                    "temperature_f": round(temp_fahrenheit, 2),
                    "humidity": data["main"]["humidity"],
                    "description": data["weather"][0]["description"].capitalize(),
                }
            else:
                weather_data = {"error": "City not found!"}
    return render_template("index.html", weather_data=weather_data)

if __name__ == "__main__":
    print("Starting Flask app...")  # Debug print
    app.run(debug=True)