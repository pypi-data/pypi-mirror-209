import requests
from icecream import ic

# Initialize the api_key variable
api_key = None
base_url = "http://api.twilix.io"

def set_api_key(key):
    global api_key
    api_key = key


def make_post_request(endpoint: str, json: dict):
    headers = {
        "Authorization": f"Bearer {api_key}",
    }
    response = requests.post(base_url + endpoint, headers=headers, json=json)
    ic(response.content.decode())
    response.raise_for_status()
    return response.json()


def add_objects(collection_name: str, objects: list):
    return make_post_request(
        endpoint="/collection/bulk_insert",
        json={"collection_name": collection_name, "objects": objects},
    )


def semantic_search(collection_name: str, query: str, fields_to_search: list = None):
    return make_post_request(
        endpoint="/collection/semantic_search",
        json={
            "collection_name": collection_name,
            "text": query,
            "fields_to_search": fields_to_search,
        },
    )


def ask(
    collection_name: str,
    query: str,
    fields_to_search: list = None,
    include_reference_documents: bool = False,
):
    return make_post_request(
        endpoint="/collection/ask_question",
        json={
            "collection_name": collection_name,
            "text": query,
            "fields_to_search": fields_to_search,
            "include_reference_documents": include_reference_documents,
        },
    )

