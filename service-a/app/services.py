import requests
import json



def call_external_service(ip):
    response = requests.get(url=f"http://ip-api.com/json/{ip}")
    return response.text

def extract_country(data):
    data = json.loads(data)
    country = data["country"]
    return country

