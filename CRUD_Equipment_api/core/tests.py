from django.test import TestCase

# Create your tests here.

import httpx  # importing the httpx module
import json

data = {
    "id": 3,
    "sne_id": 232547,
    "trs_area": "L/NWS"
}

json_data = json.dumps(data)

headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71"
}

# get testing

# resp = httpx.post("http://127.0.0.1:9823/home/", data=json_data)
# if resp.status_code == 200:
#     print(resp.json())


# post testing

# resp = httpx.put("http://127.0.0.1:9823/home/3/", data=json_data)
# if resp.status_code == 200:
#     print(resp.json())

# patch testing

# resp = httpx.patch("http://127.0.0.1:9823/home/3/", data=json_data)
# if resp.status_code == 200:
#     print(resp.json())


# delete testing

resp = httpx.delete("http://127.0.0.1:9823/home/3/")
if resp.raise_for_status():
    print(resp.json())
