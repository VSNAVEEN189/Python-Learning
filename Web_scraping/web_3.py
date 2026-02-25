# POSTING
import requests
url = "http://127.0.0.1:8000/post/"

payload = {
    "Title" : "Greetings",
    "Content" : "Hello python"
}

response = requests.post(url = url, data = payload)

print(response.text)