import requests
from dotenv import load_dotenv
import os
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.columns import Columns
from rich import box

# Load API Key
load_dotenv()
api_key = os.getenv("API_KEY")

console = Console()


def getWeatherData(city: str) -> None:
    # Weather Table
    weather = Table(
        show_header=False,
        box=box.ROUNDED,
        border_style="bold green",
    )

    # Humidity Table
    humidity = Table(
        show_header=False,
        box=box.ROUNDED,
        border_style="bold red",
    )

    # Wind Table
    wind = Table(
        show_header=False,
        box=box.ROUNDED,
        border_style="bold blue",
    )

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    try:
        response = requests.get(url, timeout=50)
        response.raise_for_status()
    except requests.RequestException as e:
        raise RuntimeError(f"Couldn't retrieve data, failed: {e}")

    data = response.json()

    # Reformat Data into one Dict
    info = {
        "city": data["name"],
        "temperature_celsius": round(data["main"]["temp"] - 273.15),
        "humidity_percent": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
        "wind_degree": data["wind"]["deg"],
        "weather_description": data["weather"][0]["description"]
    }

    # Weather Box
    weather.add_column(justify="center")
    weather.add_row(f"* {info.get('city')}")
    weather.add_row(f"- {info.get('weather_description')}")
    weather.add_row(f"T: {info.get('temperature_celsius')}°C")

    weatherBox = Panel(
        weather,
        title="Weather",
        border_style="bold green"
    )

    # Humidity Box
    humidity.add_column(justify="center")
    humidity.add_row("")
    humidity.add_row(f"H: {info.get('humidity_percent')}%")
    humidity.add_row("")

    humidityBox = Panel(
        humidity,
        title="Humidity",
        border_style="bold red"
    )

    # Wind Box
    wind.add_column(justify="center")
    wind.add_row(f"S: {info.get('wind_speed')} m/s")
    wind.add_row("")
    wind.add_row(f"D: {info.get('wind_degree')}°")

    windBox = Panel(
        wind,
        title="Wind",
        border_style="bold blue"
    )

    # Print in one horizontal row (auto-sized)
    console.print(
        Columns(
            [weatherBox, humidityBox, windBox],
            expand=False,
            equal=False,
            padding=(1, 3)
        )
    )


if __name__ == "__main__":
    city = input("Enter your city: ")
    getWeatherData(city)
