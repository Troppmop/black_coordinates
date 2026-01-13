import requests
from requests import HTTPError
import json


def call_external_service(ip):
    """
    this function receives ip as an argument sends it to ip-api service
    then returns the response
    
    :param ip: the query ip

    """
    try:
        response = requests.get(url=f"http://ip-api.com/json/{ip}")
        return response.text
    except HTTPError as e:
        raise str(e)
    
def extract_relevant_data(data):
    """
    this function extracts the query ip and coordinates from a ip-api response

    :param data: ip-api respnse
    """
    data = json.loads(data)
    coordinates = {"ip":data["query"], "lat": data["lat"], "lon": data["lon"]}
    return coordinates

def send_to_service_b(data):
    """
    this function sends the given data (ip and coordinates) to the second service

    :param data: ip and coordinates
    """
    try:
        url = "http://b:8001/items"
        response = json.loads(requests.post(url=url, json=data).text)
        return response
    except HTTPError as e:
        raise str(e)
