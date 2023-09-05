import requests
import json

def call_api(api_name: str, post_data: dict):
    return requests.post(
        url = f"http://127.0.0.1:8901/{api_name}",
        data=json.dumps(post_data)
    )