# TEXT 
import requests

url = "https://www.hypedin.co/"

response = requests.get(url = url)

print(type(response.text))  


