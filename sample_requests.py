import requests
import json

# GETの例
get_response = requests.get(url="http://127.0.0.1:8000/sample/get?input_a=Hello&input_b=Python")
get_response_data = get_response.json()
print(get_response_data)

# GETの例
get_data = {
    "input_a": "Hello",
    "input_b": "Python"
}
get_response = requests.get(url="http://127.0.0.1:8000/sample/get", params=get_data)
get_response_data = get_response.json()
print(get_response_data)

# POSTの例
post_data = {
    "input_a": "Hello",
    "input_b": "Python"
}
post_response = requests.post(url="http://127.0.0.1:8000/sample/post", data=json.dumps(post_data))
post_response_data = post_response.json()

print(post_response_data)