import twilix
from icecream import ic

collection_name = "example2"

api_key = "1f2B9oV_xbQvGbFcryiynNOEBwtFd_5YV6huRwVMHSA="
# api_key = "j7UqObCMXFi4i1rQqBUdHidZ_K5fsHZkmf0h91HU9LM="

twilix.api_key = api_key

result = twilix.search(
    collection_name=collection_name,
    query="what animal is the largest?",
    fields_to_search=["answer"],
)
ic(result)
