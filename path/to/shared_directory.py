import json

data = {'key': 'value'}

# Write to JSON file
with open('/path/to/shared_directory/data.json', 'w') as json_file:
    json.dump(data, json_file)

# Read from JSON file
with open('/path/to/shared_directory/data.json', 'r') as json_file:
    loaded_data = json.load(json_file)
    print(loaded_data)
