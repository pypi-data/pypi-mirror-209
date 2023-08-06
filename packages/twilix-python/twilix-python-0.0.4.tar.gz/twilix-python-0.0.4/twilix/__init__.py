import requests
from icecream import ic

# Initialize the api_key variable
api_key = None
base_url = "https://api.twilix.io"
# base_url = "http://localhost:8000"


def set_api_key(key):
    global api_key
    api_key = key


def make_post_request(endpoint: str, json: dict, params: dict = None):
    headers = {
        "Authorization": f"Bearer {api_key}",
    }
    response = requests.post(
        base_url + endpoint, headers=headers, json=json, params=params
    )
    if response.status_code != 200:
        ic(response.content.decode())
    response.raise_for_status()
    return response.json()


def make_delete_request(endpoint: str, json: dict):
    headers = {
        "Authorization": f"Bearer {api_key}",
    }
    response = requests.delete(base_url + endpoint, headers=headers, json=json)
    ic(response.content.decode())
    response.raise_for_status()
    return response.json()


def make_get_request(endpoint: str, params: dict = None):
    headers = {
        "Authorization": f"Bearer {api_key}",
    }
    response = requests.get(base_url + endpoint, headers=headers, params=params)
    ic(response.content.decode())
    response.raise_for_status()
    return response.json()


def add_objects(collection_name: str, objects: list):
    return make_post_request(
        endpoint=f"/collection/{collection_name}/bulk_insert",
        json={"objects": objects},
    )


def search(collection_name: str, query: str, fields_to_search: list = None):
    return make_post_request(
        endpoint=f"/collection/{collection_name}/search",
        json={
            "text": query,
            "fields_to_search": fields_to_search,
        },
    )


def answer(
    collection_name: str,
    query: str,
    fields_to_search: list = None,
    include_reference_documents: bool = False,
):
    return make_post_request(
        endpoint=f"/collection/{collection_name}/answer",
        json={
            "text": query,
            "fields_to_search": fields_to_search,
            "include_reference_documents": include_reference_documents,
        },
    )


def delete_object(collection_name: str, object_id: str):
    """Delete an object"""
    return make_delete_request(
        endpoint=f"/collection/{collection_name}/object/delete",
        json={"object_id": object_id},
    )


def list_collections():
    """List collections"""
    return make_get_request(
        endpoint="/collection/list",
    )


def list_objects(collection_name: str):
    """List documents"""
    return make_post_request(
        f"/collection/{collection_name}/list",
        json=None,
    )


def graphql(graphql_query: str):
    """GraphQL"""
    return make_post_request(
        endpoint=f"/graphql",
        json={
            "graphql_query": graphql_query,
        },
    )


def get_number_of_objects(collection_name: str):
    """Number of documents"""
    return make_get_request(
        endpoint=f"/collection/{collection_name}/number_of_objects",
    )


def get_collection_schema(collection_name: str):
    """Get collection schema"""
    return make_get_request(
        endpoint=f"/collection/{collection_name}/schema",
    )
