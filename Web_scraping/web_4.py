# PARAMETERS
import requests
url = "http://127.0.0.1:8000/post/?offset=6"

params = {
    "offset" : "6"
}

response = requests.post(url = url, params=params)

print(response.url)