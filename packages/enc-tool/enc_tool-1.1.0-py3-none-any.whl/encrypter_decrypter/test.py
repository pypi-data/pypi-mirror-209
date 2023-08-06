import json
with open("config/config.json", 'r') as file:
    data = json.load(file)
print(data.name)