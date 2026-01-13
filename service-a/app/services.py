import requests
import json



def call_external_service(ip):
    response = requests.get(url=f"http://ip-api.com/json/{ip}")
    return response.text

def extract_relevant_data(data):
    data = json.loads(data)
    coordinates = {"ip":data["ip"], "lat": data["lat"], "lon": data["lon"]}
    return coordinates



