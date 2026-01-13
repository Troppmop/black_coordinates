import redis

redis_client = redis.Redis(host='redis', port=6379, db=0)

def get_all(item_id:str):
    ip_list = []
    for key in redis_client.scan_iter():

        cached_item = redis_client.get(key)

        item_data = cached_item.decode('utf-8')
        
        ip_list.append({"ip": item_id, "lat": item_data['lat'], "lon": item_data['lon']})
    
    return {'ip_list':ip_list}

def set_item(item_id:str, lat:float, lon:float):
    item_data = {'lat': lat, 'lon': lon}
    redis_client.setex(f"item_{item_id}", 3600, item_data.encode('utf-8'))
    return {'message':f'added {item_id}:{item_data} to cache'}
