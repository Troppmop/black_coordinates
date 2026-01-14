from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
import requests
import json
import os



import services as s, schemas as sc

router = APIRouter()


@router.post("/post_ip")
def post_ip(ip):
    """
    this function receives ip as an argument and calls four other functions:
    1: validate_ip() to validate the ip
    2: call_external_service() to send the ip to ip-api service and get response
    3: extract_relevant_data() to extract the ip and coordinates from the response
    4: send_to_service_b() to send the ip and coordinates to the second service

    :param ip: user insert ip
    """
    sc.validate_ip(ip)
    raw_response = s.call_external_service(ip)
    relevant_data = s.extract_relevant_data(raw_response)
    return s.send_to_service_b(relevant_data)

@router.get("/items")
def get_coordinates():
    return s.retrieve_coordinates()

@router.get("/")    
def root():
    return {"status": "service a is healthy"}


@router.get("/service-b")
def health_check_b():
    curl = os.getenv('INTERNAL_URL')
    response = json.loads(requests.get(url=curl).text)
    return response
