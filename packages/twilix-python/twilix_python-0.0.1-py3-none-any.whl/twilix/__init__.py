import requests
from icecream import ic

# Initialize the api_key variable
api_key = None
# base_url = 'http://astro-alb-589730097.us-east-1.elb.amazonaws.com:8000'
base_url = 'http://localhost:8000'

def set_api_key(key):
    global api_key
    api_key = key

def add_objects(collection_name: str, objects: list):
    headers = {
        'Authorization': f'Bearer {api_key}',
    }
    response = requests.post(
        base_url + '/collection/bulk_insert', 
        headers=headers,
        json={
            "collection_name": collection_name,
            "objects": objects
        }
    )
    response.raise_for_status()
    return response.json()

def semantic_search(collection_name: str, query: str,
    fields_to_search: list=None):
    headers = {
        'Authorization': f'Bearer {api_key}',
    }
    if fields_to_search is None:
        fields_to_search = []
    response = requests.post(
        base_url + '/collection/semantic_search', 
        headers=headers,
        json={
            "collection_name": collection_name,
            "text": query,
            "fields_to_search": fields_to_search
        }
    )
    ic(response.content.decode())
    response.raise_for_status()
    return response.json()
