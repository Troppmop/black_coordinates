from pydantic.networks import IPvAnyAddress
from pydantic import BaseModel, ValidationError
from pydantic_extra_types.coordinate import Coordinate


class Location(BaseModel):
    coordinate: Coordinate

def check_coordinate(latitude, longitude):
    try:
        coordinate = Location(coordinate=(latitude, longitude))
        return {'latitude': coordinate.coordinate.latitude, 'longitude':coordinate.coordinate.longitude} 
    except ValidationError as e:
        return {'message': str(e)}
    
class Ip(BaseModel):
    ip_address: IPvAnyAddress

def validate_ip(ip):
    try:
        valid_ip = Ip(ip_address=ip)
        return valid_ip.ip_address
    except ValidationError as e:
        return f"\nInvalid input detected! \n {e.errors()}"

