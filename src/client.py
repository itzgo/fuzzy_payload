import requests
from .config import API_URL

def call_api(payload):
    return requests.post(API_URL, json=payload, timeout=5).json()
