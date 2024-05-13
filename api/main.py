import requests

from pprint import pprint


JSON_PLACEHOLDER_BASE_URL = "https://jsonplaceholder.typicode.com/"
REST_COUNTRIES_BASE_URL = "https://restcountries.com/v3.1/"
IP_API_BASE_URL = "https://ipapi.co"
POKEMON_API = "https://pokeapi.co/api/v2/"

# ===== Play with test API ===== #
# res = requests.get(f"{JSON_PLACEHOLDER_BASE_URL}posts")
# print(f"Response status code is {res.status_code}")
# res.raise_for_status()
# if res.status_code == 200:
#     data = res.json()
#     print(f"Items count is {len(data)}")
#     for item in data:
#         print(f"Item ID is {item.get('id')}")

# res = requests.post(f"{JSON_PLACEHOLDER_BASE_URL}posts")
# print(res.status_code)

# res = requests.put(f"{JSON_PLACEHOLDER_BASE_URL}posts/1")
# print(res.status_code)

# res = requests.patch(f"{JSON_PLACEHOLDER_BASE_URL}posts/1")
# print(res.status_code)

# res = requests.delete(f"{JSON_PLACEHOLDER_BASE_URL}posts/1")
# print(res.status_code)

# res = requests.get(f"{JSON_PLACEHOLDER_BASE_URL}posts")
# print(res.status_code)
# data = res.json()
# for item in data[:5]:
#     post_id = item.get("id")
#     query_params = {"postId": post_id}
#     res = requests.get(
#         f"{JSON_PLACEHOLDER_BASE_URL}comments",
#         params=query_params
#     )
#     print(f"Post ID: {post_id}, Objects count: {len(res.json())}")


# ===== Get info about Ukraine ===== #
# country_name = "Ukraine"
# res = requests.get(f"{REST_COUNTRIES_BASE_URL}name/{country_name}")
# print(res.status_code)
# pprint(res.json())

# res = requests.get(f"{REST_COUNTRIES_BASE_URL}all")
# print(res.status_code)
# pprint(res.json())


# ===== Get info about IP address ===== #
# ip = "172.217.23.206"
# form = "json"
#
# res = requests.get(f"{IP_API_BASE_URL}/{ip}/{form}")
# pprint(res.json())


# ===== Get Pikachu ===== #
# pokemon_name = "pikachu"
# res = requests.get(f"{POKEMON_API}/pokemon/{pokemon_name}/")
# pprint(res.json())


# ===== Get Pokemon abilities paginated ===== #
# page = 1
# offset = 0
# limit = 5
# query_params = {"limit": limit, "offset": offset}
#
# while True:
#     res = requests.get(f"{POKEMON_API}/ability/", params=query_params)
#     print([item.get("name") for item in res.json().get("results")])
#     page_number = int(input("Enter a page number: "))
#     query_params["offset"] = (page_number - 1) * query_params.get("limit")