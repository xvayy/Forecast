import requests
import datetime
import glob
from pathlib import Path
API_KEY = "862cc41441b762f0c8d091fd63517ef4"

# api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}

def get_city_name(city="London"):
    url_call = ("http://api.openweathermap.org/geo/1.0/direct"
                f"?q={city}"
                "&limit=5"
                f"&appid={API_KEY}")

    response = requests.get(url_call)
    options = response.json()
    result = []
    result.append(options[0]["lat"])
    result.append(options[0]["lon"])
    result.append(options[0]["name"])

    return result


def get_data(place, forecast_days=1, kind="Sky"):
    # Old method
    # url = ("https://api.openweathermap.org/data/2.5/forecast"
    #        f"?q={place}"
    #        f"&appid={API_KEY}")

    url = (f"http://api.openweathermap.org/data/2.5/forecast"
           f"?lat={place[0]}"
           f"&lon={place[1]}"
           f"&appid={API_KEY}"
           "&units=metric")
    response = requests.get(url)
    data = response.json()
    print(data)

    # Calculate frequencies that depends on amount of the days
    frequencies = forecast_days * 8

    # Get dates
    dates = [datetime.datetime.fromtimestamp(dic["dt"], tz=datetime.timezone.utc).strftime("%Y-%m-%d %H:%M") for dic in data["list"][:frequencies]]
    print(dates)
    for i in dates:
        print(i)



    if kind == "Temperature":
        temperatures = [dic["main"]["temp"] for dic in data["list"][:frequencies]]
        print(temperatures)
        return temperatures, dates,
    if kind == "Sky":
        sky = [dic["weather"][0]["main"] for dic in data["list"][:frequencies]]
        print(sky)
        return sky, dates

def get_images():
    filenames = glob.glob("images/*png")

    images_data = []
    for name in filenames:
        new_dict = {}
        new_dict["name"] = Path(name).stem.title()
        new_dict["path"] = name
        images_data.append(new_dict)

    return images_data


if "__main__" == __name__:
    print(get_images())
