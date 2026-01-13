import requests
from requests import HTTPError
import json


def call_external_service(ip):
    try:
        response = requests.get(url=f"http://ip-api.com/json/{ip}")
        return response.text
    except HTTPError as e:
        raise str(e)
    
def extract_relevant_data(data):
    data = json.loads(data)
    coordinates = {"ip":data["query"], "lat": data["lat"], "lon": data["lon"]}
    return coordinates

