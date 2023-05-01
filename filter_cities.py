import json
from collections import defaultdict

def split_cities_by_country(file):
    with open(file, 'r') as infile:
        cities = json.load(infile)

    countries = defaultdict(list)
    for city in cities:
        countries[city['country']].append(city)

    for country, cities in countries.items():
        with open(f'jsons/out/{country}_cities.json', 'w') as outfile:
            json.dump(cities, outfile, indent=2)


if __name__ == "__main__":
    input_file = 'jsons/in/city.list.json'
    split_cities_by_country(input_file)
