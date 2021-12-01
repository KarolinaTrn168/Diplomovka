from RedisDB import endpoints
import requests

def get_method(baseURL, endpoint):
    print("get request")
    response = requests.get(baseURL+endpoint)
    print(response)
    print("Response: ", response.json())

def post_method():
    print("post request")

def put_method():
    print("put request")

def delete_method():
    print("delete request")