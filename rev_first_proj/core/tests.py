from django.test import TestCase
import requests
# Create your tests here.
headers={
    "Content-Type":"application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62"
}

def get_data():
    resp=requests.get("http://127.0.0.1:8000/homeall/",headers=headers)
    if resp.status_code == 200:
        print(resp.json())

get_data()