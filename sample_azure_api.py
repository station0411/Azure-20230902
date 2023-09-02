import requests
import json

# ネット上の画像
post_headers = {
    "Content-Type": "application/json",
    "Ocp-Apim-Subscription-Key": "INPUT_YOUR_API_KEY",
}
post_data = {
    "url": "https://www.happy-bears.com/kajily/wp-content/uploads/2019/11/c565ce857b083be9dc09c3ba40f81d30_s-630x420.jpg"
}
post_response = requests.post(
    url="https://INPUT_YOUR_RESOURDE_NAME.cognitiveservices.azure.com/vision/v3.1/tag?language=ja",
    headers= post_headers,
    data=json.dumps(post_data))
post_response_data = post_response.json()
for tag in post_response_data["tags"]:
    print(tag["name"])


# ローカルの画像
post_headers = {
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': "INPUT_YOUR_API_KEY",
}
image_file = open('.\\sample_image.jpg', 'rb').read()
post_response = requests.post(
    url="https://INPUT_YOUR_RESOURDE_NAME.cognitiveservices.azure.com/vision/v3.1/tag?language=ja",
    headers=post_headers,
    data=image_file)
post_response_data = post_response.json()
for tag in post_response_data["tags"]:
    print(tag["name"])