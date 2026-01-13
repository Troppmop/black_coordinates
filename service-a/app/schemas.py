from pydantic.networks import IPvAnyAddress
from pydantic import BaseModel, ValidationError
from pydantic_extra_types.coordinate import Coordinate


class Location(BaseModel):
    coordinate: Coordinate

def check_coordinate(latitude, longitude):
    """
    this function receives coordinates as an argument then validates it

    :param latitude: latitude number
    :param longitude: longitude number
    """
    try:
        coordinate = Location(coordinate=(latitude, longitude))
        return {'latitude': coordinate.coordinate.latitude, 'longitude':coordinate.coordinate.longitude} 
    except ValidationError as e:
        return {'message': str(e)}
    
class Ip(BaseModel):
    ip_address: IPvAnyAddress

def validate_ip(ip):
    """
    this function receives ip as an argument then validates it

    :param ip: ip address
    """
    try:
        valid_ip = Ip(ip_address=ip)
        return valid_ip.ip_address
    except ValidationError as e:
        return f"\nInvalid input detected! \n {e.errors()}"

