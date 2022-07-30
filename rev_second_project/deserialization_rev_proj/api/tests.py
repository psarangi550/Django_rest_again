from django.test import TestCase
import requests
import json

# Create your tests here.

data = {
    "cp_number": "CP00QQQ",
    "sne_id": 20222035,
    "sch_number": 344436,
    "trs_area": "L/COL"
}

json_data = json.dumps(data)

url = "http://127.0.0.1:8000/home/"

headers = {
    "content-type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62"
}


def post_data():
    resp = requests.post(url, data=json_data, headers=headers)
    if resp.status_code == 200:
        print(resp.json())


if __name__ == "__main__":
    post_data()
