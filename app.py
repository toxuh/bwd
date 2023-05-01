import json
import time
import requests
import psycopg2
from os import getenv

DATABASE_URL = getenv("DATABASE_URL")
API_KEY = getenv("OWM_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def fetch_weather(city_id):
    url = f"{BASE_URL}?id={city_id}&appid={API_KEY}"
    response = requests.get(url)
    return response.json()

def insert_data_to_db(data):
    with psycopg2.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            query = """INSERT INTO weather_data (city_id, city_name, weather_data)
                       VALUES (%s, %s, %s)"""
            cur.execute(query, (data["id"], data["name"], json.dumps(data)))


def main():
    country_code = "PT"

    with open(f"jsons/out/{country_code}_cities.json", "r") as file:
        cities = json.load(file)

    request_counter = 0
    rate_limit = 60

    while True:
        for city in cities:
            if request_counter >= rate_limit:
                print("Rate limit reached, waiting for 60 seconds...")
                time.sleep(60)
                request_counter = 0

            city_id = city["id"]
            weather_data = fetch_weather(city_id)

            if "name" in weather_data:
                print(f"Fetching weather data for {weather_data['name']} (ID: {city_id})")
                insert_data_to_db(weather_data)
            else:
                print(f"Error fetching weather data for city ID: {city_id}, response: {weather_data}")

            request_counter += 1
            time.sleep(1)


if __name__ == "__main__":
    main()
