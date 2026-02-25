print("---------FINDING VALUES--------")
print("--------e-------")
print(ord('e'))
print('--------A-------')
print(ord('A'))
print('--------2-------')
print(ord('2'))
print('-------*-------')
print(ord('*'))


print("------For bringing the data---------")
import urllib.request  #To work with the urls and to open and read the urls
import urllib.parse    #parsing
import urllib.error    #Contains all the exception

url = urllib.request.urlopen("https://www.hypedin.co/")

for line in url:
    print(line.decode().strip())


print("-----TO Get the data---------")
import requests

url = "https://www.hypedin.co/"
# print(dir(requests))
response = requests.get(url = url)
# print(dir(response))
print(response.status_code)
print(response.request.headers)


print("-----Stating data using dictionaries----")
url = "https://www.hypedin.co/"
user = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"
}

response = requests.get(url=url, headers = user)
print(response.request.headers)


print("------CONTENT------")
url = "https://cutshort.io/_next/image?url=https%3A%2F%2Fcdnv2.cutshort.io%2Fcompany-static%2F62a727e23734df00285206ea%2Fuser_uploaded_data%2Flogos%2Fwissen_technology_logo.jpeg&w=256&q=75"
user = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"
}

response = requests.get(url=url, headers = user)
print(type(response.content))
pic = response.content

f = open("wissen_technology_logo.jpeg", "wb")
f.write(pic)