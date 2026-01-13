from fastapi import APIRouter
import requests
import json
"""from .schemas import Item
from .storage import get_item, set_item"""



router = APIRouter()
  
@router.get('/')
def root():
    return {'status': 'service-b is healthy'}
    

@router.get('/service-a')
def healthcheck_a():
    response = json.loads(requests.get(url='http://a:8000/').text)
    return response

"""
@router.post('/items/')
def add_item(item: Item):
    set_item(item.ip, item.coords)

@router.get('/items/{ip}')
def retrieve(ip:str)"""