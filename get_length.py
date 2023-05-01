import json

def get_json_length(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return len(data)


if __name__ == "__main__":
    country_code = 'PT'
    input_file = f'jsons/out/{country_code}_cities.json'
    json_length = get_json_length(input_file)
    print(f'The JSON file {input_file} contains {json_length} items.')
