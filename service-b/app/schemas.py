from pydantic import BaseModel

class Item(BaseModel):
    ip: str
    lat: float
    lon: float