import requests

meteor_api = requests.get("https://data.nasa.gov/resource/y77d-th95.json")

print(meteor_api.status_code)
#print(meteor_api)

#print(meteor_api.text)

meteor_data = meteor_api.json()

print(meteor_data[0])
