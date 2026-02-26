import requests
from bs4 import BeautifulSoup
import csv

def Extract(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    response = requests.get(url=url, headers=headers).content
    soup = BeautifulSoup(response, "lxml")
    tag = soup.find("div",{"id":"mp-right"}) #Main data
    # h = tag.find("h2")                      #Sub data
    h = tag.find_all("h2")                   # find all the h2 tag with title 
    # print(h)                                 #Result
    content = [heading.text for heading in h]
    # print(content)                                   #List comphrension
    
    with open("wiki.csv" , "w") as csv_file:  #Created the file
        csv_write = csv.writer(csv_file)      #Enable it to write
        csv_write.writerow(content)            #Adding the content

Extract(url="https://en.wikipedia.org/wiki/Main_Page")