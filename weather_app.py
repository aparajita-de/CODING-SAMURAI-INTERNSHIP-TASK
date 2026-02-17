import requests


def get_weather(city_name, api_key):
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city_name}&appid={api_key}&units=metric"
    )

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        temp_c = data["main"]["temp"]
        temp_f = (temp_c * 9 / 5) + 32

        weather_info = {
            "description": data["weather"][0]["description"].capitalize(),
            "temp_c": temp_c,
            "temp_f": temp_f,
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "pressure": data["main"]["pressure"],        # hPa
            "wind_speed": data["wind"]["speed"],         # m/s
        }

        return weather_info

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None


def display_weather(city_name, weather_info):
    if weather_info:
        print(f"\n📍 Weather in {city_name.title()}")
        print(f"🌤️ Condition    : {weather_info['description']}")
        print(
            f"🌡️ Temperature  : "
            f"{weather_info['temp_c']}°C / {weather_info['temp_f']:.2f}°F"
        )
        print(f"🤔 Feels Like   : {weather_info['feels_like']}°C")
        print(f"💧 Humidity     : {weather_info['humidity']}%")
        print(f"🌬️ Wind Speed   : {weather_info['wind_speed']} m/s")
        print(f"📈 Pressure     : {weather_info['pressure']} hPa")
    else:
        print(" Failed to retrieve weather data.")


def main():
    api_key = "8376e92f57da36b2572e586e2d6de366"
    city_name = input("\nEnter city name: ").strip()

    if not city_name:
        print("❌ City name cannot be empty.")
        return

    weather_info = get_weather(city_name, api_key)
    display_weather(city_name, weather_info)


if __name__ == "__main__":
    main()

print("\n\n\n")