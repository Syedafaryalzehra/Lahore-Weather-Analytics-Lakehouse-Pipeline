import json
import os
import requests

os.makedirs("Full_load", exist_ok=True)
os.makedirs("incremental_load", exist_ok=True)

full_url = (
    "https://archive-api.open-meteo.com/v1/archive"
    "?latitude=31.5204&longitude=74.3587"
    "&start_date=2024-01-01&end_date=2024-01-07"
    "&hourly=temperature_2m,relativehumidity_2m,dewpoint_2m,"
    "precipitation,rain,weathercode,pressure_msl,surface_pressure,"
    "windspeed_10m,windspeed_100m,winddirection_10m,winddirection_100m,"
    "windgusts_10m,soil_temperature_0cm,soil_temperature_6cm,"
    "soil_moisture_0_1cm,vapor_pressure_deficit,et0_fao_evapotranspiration"
    "&timezone=Asia/Karachi"
)

try:
    response = requests.get(full_url, timeout=30)
    if response.status_code == 200:
        data = response.json()
        filepath = "Full_load/full_load_sample.json"
        with open(filepath, "w") as f:
            json.dump(data, f, indent=2)
        hours = len(data["hourly"]["time"])
        print(f" SUCCESS! Got {hours} hourly records")
        print(f" Saved to: {filepath}")
    else:
        print(f" FAILED! Status code: {response.status_code}")
except Exception as e:
    print(f" ERROR: {e}")


incr_url = (
    "https://archive-api.open-meteo.com/v1/archive"
    "?latitude=31.5204&longitude=74.3587"
    "&start_date=2024-01-08&end_date=2024-01-08"
    "&hourly=temperature_2m,relativehumidity_2m,dewpoint_2m,"
    "precipitation,rain,weathercode,pressure_msl,surface_pressure,"
    "windspeed_10m,windspeed_100m,winddirection_10m,winddirection_100m,"
    "windgusts_10m,soil_temperature_0cm,soil_temperature_6cm,"
    "soil_moisture_0_1cm,vapor_pressure_deficit,et0_fao_evapotranspiration"
    "&timezone=Asia/Karachi"
)

try:
    response = requests.get(incr_url, timeout=30)
    if response.status_code == 200:
        data = response.json()
        filepath = "incremental_load/inc_load_sample.json"
        with open(filepath, "w") as f:
            json.dump(data, f, indent=2)
        hours = len(data["hourly"]["time"])
        print(f" SUCCESS! Got {hours} hourly records")
        print(f" Saved to: {filepath}")
    else:
        print(f" FAILED! Status code: {response.status_code}")
except Exception as e:
    print(f" ERROR: {e}")