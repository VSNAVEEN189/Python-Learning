import requests
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Ask user what to name the images
search = input("Enter image folder name (example: moon): ")

url = "https://books.toscrape.com/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

images = soup.find_all("img")
print("Total images found:", len(images))

count = int(input("How many images to download? "))
count = min(count, len(images))  # prevent error

# Create folder
os.makedirs(search, exist_ok=True)

print("\nDownloading...\n")

for i in range(count):
    img_src = images[i]["src"]
    img_url = urljoin(url, img_src)

    img_data = requests.get(img_url).content

    with open(f"{search}/{search}_{i+1}.jpg", "wb") as f:
        f.write(img_data)

    print(f"Downloaded {search}_{i+1}.jpg")

print("\nDone!")

# https://www.google.com/search?sca_esv=c937c0e97e5925fd&amp;rlz=1C1CHBD_enIN1152IN1152&amp;sxsrf=ANbL-n7C9C2N9sndrui9iKoQ0MzA8lwNuw:1772089451959&amp;udm=2&amp;fbs=ADc_l-aN0CWEZBOHjofHoaMMDiKpaEWjvZ2Py1XXV8d8KvlI3jljrY5CkLlk8Dq3IvwBz-SJyfRX_inP-J3Cs9lQZu9J3QQItR3OEYwLkKzmr7kPOds-mbrHZ05SQHoSw9Gwghjdt01sH5ZqaLclnWwHCdnb84ZvyEmJ0v7ayb3w69GCb6--AlQkTMIgczcJHznS8W6d3OSxqbAUykH-Zbdtj7cutygTsg&amp;q=moon&amp;sa=X&amp;ved=2ahUKEwjyha3Sy_aSAxV79DgGHTA6INEQtKgLegQIFxAB&amp;biw=772&amp;bih=734&amp;dpr=1.25