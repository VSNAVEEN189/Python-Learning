import requests
from bs4 import BeautifulSoup

class PriceTracer:
    def __init__(self, url):
        self.url = url
        self.user_agent = {"User-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"}
        self.response = requests.get(url = self.url, headers = self.user_agent).text
        self.soup  = BeautifulSoup(self.response, "lxml")

    def product_title(self):
        title = self.soup.find("span", {"id": "productTitle"})
        if title is not None:
            return title.text.strip()
        else:
            return "Tag not found"

    def product_price(self):
        price = self.soup.find("span", {"class": "a-price-whole"})
        if price is not None:
            return price.text
        else:
            return "Tag not found"

device = PriceTracer(url="https://www.amazon.in/OnePlus-Snapdragon%C2%AE-7400mAh-Personalised-Game-Changing/dp/B0FZT1LXPZ/ref=sr_1_3_sspa?crid=1W8FSS0RH5GT6&dib=eyJ2IjoiMSJ9.qBkVWYUNwQq_FMPx9yzng5ybkk3dgCeymoA2QXhGwzCLp3G-720LPtCb7GNePhunCp_Bl8giAdbgg2Af8JBjAkRbsZttCsas_stkTK-oWVd23mxW1wwYYpw-A0KywKGrlyP3ReXCpbtSR2OzVMmyaeUlovxObJNzgLF8H36trIn4ny1CCN7MofAjrtPFT5tMbet79ZPO2s7QL93CigrB8pxPpipoJXuffuXVbyXjYXXV-b-RI0ZDqA4l_u7685ZsP8lbAMwqxMZLriZRP5_ibtqmVBRiMpQxvpBVHT3PMyk.FRhaSZWpWR15W-9r0GlIcbh0EaVvT0enz2QRiQYPf5k&dib_tag=se&keywords=mobile%2Bphone%2Bunder%2B20000&nav_sdd=aps&qid=1772189145&refinements=p_n_feature_eight_browse-bin%3A14267636031&rnid=8561111031&s=electronics&sprefix=mobil&sr=1-3-spons&aref=NCj1O3OkYr&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1")

print(device.product_title())
print(device.product_price())