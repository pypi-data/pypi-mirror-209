"""Test for inserting data
"""
import twilix
from icecream import ic

# api_key = "j7UqObCMXFi4i1rQqBUdHidZ_K5fsHZkmf0h91HU9LM="
api_key = "1f2B9oV_xbQvGbFcryiynNOEBwtFd_5YV6huRwVMHSA="

twilix.api_key = api_key

collection_name = "example2"

docs = [
    {
        "answer": "This framework generates embeddings for each input sentence",
    },
    {
        "answer": "Sentences are passed as a list of string.",
    },
    {
        "answer": "The quick brown fox jumps over the lazy dog."
    },
]

result = twilix.add_objects(collection_name=collection_name, objects=docs)
ic(result)
