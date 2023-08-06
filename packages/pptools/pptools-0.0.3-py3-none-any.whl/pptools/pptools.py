import asyncio
from PIL import Image
import aiohttp as aiohttp
import requests
import time
import urllib3
from bs4 import BeautifulSoup
from selenium import webdriver
import os



class getSoup:
    """
      This class is used to extract the soup object by any means
    """

    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def requests(self):
        response = requests.get(url=self.url, headers=self.headers)
        soup = BeautifulSoup(response.text, 'lxml')
        return soup

    def urllib(self):
        req = urllib3.PoolManager()
        res = req.request('GET', self.url)
        soup = BeautifulSoup(res.data, 'lxml')
        return soup

    def selenium(self):
        driver = webdriver.Edge()
        driver.get(self.url)
        time.sleep(2)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        return soup

    def aiohttp(self):
        async def get_site_content():
            async with aiohttp.ClientSession() as session:
                async with session.get(self.url) as resp:
                    text = await resp.read()
            return BeautifulSoup(text.decode('utf-8'), 'lxml')

        loop = asyncio.get_event_loop()
        soup = loop.run_until_complete(get_site_content())
        return soup


class Parsers:
    """
        This class creates the basics of the three most popular parsers
    """
    def __init__(self):
        pass

    def getRequestsParser(self):
        with open('requests-parser.py', 'w', encoding='utf-8') as file:
            file.write("""import requests
from bs4 import BeautifulSoup
import lxml
import csv
from itertools import zip_longest

def main(url, headers, cookies):
   response = requests.get(url=url, headers=headers, cookies=cookies)
   soup = BeautifulSoup(response.text, "lxml")

   links = soup.find_all("a", class_="") #If necessary, replace the class
   sp = url.split("/")
   base_url = sp[0] + "//" + sp[1] + sp[2]
   for link in links:
       card_link = link.get("href")
       if base_url not in card_link:
           card_link = base_url + card_link
       card_response = requests.get(url=card_link, headers=headers, cookies=cookies)
       card_soup = BeautifulSoup(card_response.text, "lxml")
       tag = card_soup.find("h1").text
       price = card_soup.find("", class_="").text
       
       tags = [tag]
       prices = [price]
       d = [tags, prices]
       export_data = zip_longest(*d, fillvalue="")
       with open("data.csv", "a", encoding="utf-8", newline="") as file:
           wr = csv.writer(file, delimiter=";")
           wr.writerows(export_data)


if __name__ == "__main__":
   url = "https://example.ru"
   headers = {}
   cookies = {}
   main(url, headers, cookies)
""")

    def getAsyncioParser(self):
        with open('async-parser.py', 'w', encoding='utf-8') as file:
            file.write("""import aiohttp
from bs4 import BeautifulSoup
import asyncio
import csv
from itertools import zip_longest

async def fetch(session, url, headers, cookies):
    async with session.get(url, headers=headers, cookies=cookies) as response:
        return await response.text()

async def main(url, headers, cookies):
    async with aiohttp.ClientSession() as session:
        response = await fetch(session, url, headers, cookies)
        soup = BeautifulSoup(response, "lxml")

        links = soup.find_all("a", class_="")
        for link in links:
            card_link = link.get("href")
            card_response = await fetch(session, card_link, headers, cookies)
            card_soup = BeautifulSoup(card_response, "lxml")

            tag = card_soup.find("h1").text
            price = card_soup.find("", class_="").text

            tags = [tag]
            prices = [price]
            d = [tags, prices]
            export_data = zip_longest(*d, fillvalue="")
            with open("data.csv", "a", encoding="utf-8", newline="") as file:
                wr = csv.writer(file, delimiter=";")
                wr.writerows(export_data)


if __name__ == "__main__":
    url = "https://example.ru"
    headers = {}
    cookies = {}
    asyncio.run(main(url, headers, cookies))
""")

    def getSeleniumParser(self):
        with open('selenium-parser.py', 'w', encoding='utf-8') as file:
            file.write("""import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import csv
import lxml
from itertools import zip_longest

def main(url, pause_time):
    driver = webdriver.Edge()
    driver.get(url)
    time.sleep(pause_time)
    soup = BeautifulSoup(driver.page_source, "lxml")
    links = soup.find_all("a", class_="") #If necessary, replace the class
    sp = url.split("/")
    base_url = sp[0] + "//" + sp[1] + sp[2]
    for link in links:
        card_link = link.get("href")
        if base_url not in card_link:
            card_link = base_url + card_link
        driver1 = webdriver.Edge()
        driver1.get(card_link)
        time.sleep(pause_time)
        card_soup = BeautifulSoup(driver1.page_source, "html.parser")

        tag = card_soup.find("h1").text
        price = card_soup.find("", class_="").text

        tags = [tag]
        prices = [price]
        d = [tags, prices]
        export_data = zip_longest(*d, fillvalue="")
        with open("data.csv", "a", encoding="utf-8", newline="") as file:
            wr = csv.writer(file, delimiter=";")
            wr.writerows(export_data)

    driver.quit()

if __name__ == "__main__":
    url = "https://example.ru"
    pause_time = 3
    main(url, pause_time)
""")


    
class Helper:
    def __init__(self):
        pass

    def installAll(self):
        os.system('pip install lxml requests bs4 selenium pillow aiohttp')
        os.system('python.exe -m pip install --upgrade pip')

    def getHeaders(self, url):
        auth = url.split('/')[2]
        headers = {
            'authority': auth,
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
            'cache-control': 'max-age=0',
            # 'cookie': 'vi_features=%7B%22test%22%3A%221%22%7D; wucf=7; acctoken=eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiJ9.eyJpc3MiOiJ2aXRlY2giLCJhdWQiOiJ2c2VpbnN0cnVtZW50aS5ydSIsImlhdCI6MTY4MzQ0ODYzMCwiZXhwIjoxNjgzNDUyMjMwLCJkZXZpZCI6ImQ1YjMxNjhhLTkyODUtNDRiYi04MmUxLTRmYTdjZmE1NTkwZiIsInRpZCI6ImI3ZGZhMmU2LTVjYzMtNDVjMS1hYzk2LTgxZmY3YTQxYzc4OCJ9.A9h4sm4VPz4X9lXzI8Tk6ZHVqLcdkRX6OZiP_mGWeNhlPMHmRqesGkPMXlg4XgdBwndvLXHd-MMwW4PYg3zPng; reftoken=eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiJ9.eyJpc3MiOiJ2aXRlY2giLCJhdWQiOiJ2c2VpbnN0cnVtZW50aS5ydSIsImlhdCI6MTY4MzQ0ODYzMCwiZXhwIjoxNjkyMDg4NjMwLCJkZXZpZCI6ImQ1YjMxNjhhLTkyODUtNDRiYi04MmUxLTRmYTdjZmE1NTkwZiIsInRpZCI6ImI3ZGZhMmU2LTVjYzMtNDVjMS1hYzk2LTgxZmY3YTQxYzc4OCJ9.y4ZAAkxh1TwUYFQRJlFVTMcHHuNcUrZIgOL3mBuWWBJ4E7oGZG0Xw1jTREEy7Bot-jhqrs4hN9gIlDYByT8Mnw; ab_exps=%7B%22237%22%3A3%2C%22243%22%3A14%2C%22245%22%3A1%2C%22248%22%3A0%2C%22249%22%3A1%2C%22262%22%3A0%2C%22280%22%3A5%2C%22362%22%3A0%2C%22368%22%3A0%2C%22380%22%3A0%2C%22408%22%3A3%2C%22415%22%3A2%2C%22462%22%3A3%2C%22468%22%3A3%2C%22474%22%3A0%2C%22523%22%3A1%2C%22535%22%3A2%2C%22541%22%3A0%2C%22547%22%3A1%2C%22553%22%3A0%2C%22559%22%3A0%2C%22565%22%3A2%2C%22589%22%3A2%2C%22595%22%3A4%2C%22607%22%3A1%2C%22613%22%3A1%2C%22619%22%3A3%2C%22625%22%3A2%2C%22631%22%3A0%2C%22643%22%3A0%2C%22656%22%3A0%2C%22662%22%3A1%2C%22668%22%3A1%2C%22674%22%3A4%2C%22698%22%3A0%2C%22715%22%3A1%2C%22721%22%3A0%2C%22733%22%3A1%7D; isNewCart=0; pages_viewed=%7B%22value%22%3A1%2C%22expiration%22%3A1683463030%7D; cartToken=Adn4SSs1ySM60V77uEB8XEOncEGmBGZ2; _ga=GA1.2.546024606.1683448632; _gid=GA1.2.104747414.1683448632; _ym_uid=1673721450579183691; _ym_d=1683448632; _ym_isad=2; _gcl_au=1.1.162329176.1683448633; tmr_lvid=45b113f76d52db7d4ecb11d15b37f330; tmr_lvidTS=1673721450281; iap.uid=e1e0e42845164d0b87204acdc6e5df2c; g4c_x=1; adrdel=1; adrcid=Axy2MdQW6bxLxkkcE0lmXqA; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; tmr_detect=0%7C1683448636768; mindboxDeviceUUID=3716ec78-fdba-4039-9d55-235402c08910; directCrm-session=%7B%22deviceGuid%22%3A%223716ec78-fdba-4039-9d55-235402c08910%22%7D; emitted_experiments=%7B%22237%22%3A%7B%22changeId%22%3A282%2C%22variant%22%3A3%7D%2C%22243%22%3A%7B%22changeId%22%3A291%2C%22variant%22%3A14%7D%2C%22245%22%3A%7B%22changeId%22%3A297%2C%22variant%22%3A1%7D%2C%22248%22%3A%7B%22changeId%22%3A304%2C%22variant%22%3A0%7D%2C%22249%22%3A%7B%22changeId%22%3A305%2C%22variant%22%3A1%7D%2C%22262%22%3A%7B%22changeId%22%3A215%2C%22variant%22%3A0%7D%2C%22280%22%3A%7B%22changeId%22%3A334%2C%22variant%22%3A5%7D%2C%22362%22%3A%7B%22changeId%22%3A215%2C%22variant%22%3A0%7D%2C%22368%22%3A%7B%22changeId%22%3A434%2C%22variant%22%3A0%7D%2C%22380%22%3A%7B%22changeId%22%3A446%2C%22variant%22%3A0%7D%2C%22408%22%3A%7B%22changeId%22%3A474%2C%22variant%22%3A3%7D%2C%22415%22%3A%7B%22changeId%22%3A480%2C%22variant%22%3A2%7D%2C%22462%22%3A%7B%22changeId%22%3A368%2C%22variant%22%3A3%7D%2C%22468%22%3A%7B%22changeId%22%3A522%2C%22variant%22%3A3%7D%2C%22474%22%3A%7B%22changeId%22%3A552%2C%22variant%22%3A0%7D%2C%22523%22%3A%7B%22changeId%22%3A607%2C%22variant%22%3A1%7D%2C%22535%22%3A%7B%22changeId%22%3A619%2C%22variant%22%3A2%7D%2C%22541%22%3A%7B%22changeId%22%3A215%2C%22variant%22%3A0%7D%2C%22547%22%3A%7B%22changeId%22%3A631%2C%22variant%22%3A1%7D%2C%22553%22%3A%7B%22changeId%22%3A637%2C%22variant%22%3A0%7D%2C%22559%22%3A%7B%22changeId%22%3A643%2C%22variant%22%3A0%7D%2C%22565%22%3A%7B%22changeId%22%3A649%2C%22variant%22%3A2%7D%2C%22589%22%3A%7B%22changeId%22%3A703%2C%22variant%22%3A2%7D%2C%22595%22%3A%7B%22changeId%22%3A811%2C%22variant%22%3A4%7D%2C%22607%22%3A%7B%22changeId%22%3A745%2C%22variant%22%3A1%7D%2C%22613%22%3A%7B%22changeId%22%3A781%2C%22variant%22%3A1%7D%2C%22619%22%3A%7B%22changeId%22%3A787%2C%22variant%22%3A3%7D%2C%22625%22%3A%7B%22changeId%22%3A793%2C%22variant%22%3A2%7D%2C%22631%22%3A%7B%22changeId%22%3A215%2C%22variant%22%3A0%7D%2C%22643%22%3A%7B%22changeId%22%3A215%2C%22variant%22%3A0%7D%2C%22656%22%3A%7B%22changeId%22%3A215%2C%22variant%22%3A0%7D%2C%22662%22%3A%7B%22changeId%22%3A866%2C%22variant%22%3A1%7D%2C%22668%22%3A%7B%22changeId%22%3A884%2C%22variant%22%3A1%7D%2C%22674%22%3A%7B%22changeId%22%3A215%2C%22variant%22%3A4%7D%2C%22698%22%3A%7B%22changeId%22%3A215%2C%22variant%22%3A0%7D%2C%22715%22%3A%7B%22changeId%22%3A215%2C%22variant%22%3A1%7D%2C%22721%22%3A%7B%22changeId%22%3A967%2C%22variant%22%3A0%7D%2C%22733%22%3A%7B%22changeId%22%3A979%2C%22variant%22%3A1%7D%7D; __cf_bm=KLf29_FMgik5l0LE71PP5DSC1IThVEcjaVx4B0i8NOY-1683450982-0-AXFRqR89JM2uXYjdQnk7MwrOQQUYmU3yRaTjeJKqWKJ971j0Fa2B0FDfXJHZRQ4EIlNSCo8ipvz9DCjmKDc4nPk=',
            'sec-ch-ua': '"Chromium";v="112", "Microsoft Edge";v="112", "Not:A-Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        }
        return headers

    def aboutStatusCode(self, status_code):
        if status_code == 200:
            print('You can parse! (In some cases, cloudflare may work and you will have to use Selenium)')
        elif status_code == 404:
            print('You must specify the headers!')
        elif status_code == 403:
            print('You should use Selenium or specify headers and cookies!')
        elif status_code == 401:
            print('You must log in to the site for authentication!')
            print('\n')
            print("""import requests
from requests.auth import HTTPBasicAuth
response = requests.get('https://example.ru', auth=HTTPBasicAuth('user', 'pass'))""")
        elif status_code == 400:
            print('Error in the post request!')
        else:
            print('Sorry, but I don`t know!')

    def download_photo(self, url_photo):
        data = requests.get(url_photo).content
        # Opening a new file named img with extension .jpg
        # This file would store the data of the image file
        f = open('img.jpg', 'wb')
        # Storing the image data inside the data variable to the file
        f.write(data)
        f.close()
        # Opening the saved image and displaying it
        img = Image.open('img.jpg')
        img.show()






