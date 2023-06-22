import requests
from bs4 import BeautifulSoup
import json
from time import sleep

s = requests.Session()

h1={'Host': 'www.vitacost.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0'
}

input("Press Enter ")
r = s.get("https://www.vitacost.com/irwin-naturals",headers=h1)

soup = BeautifulSoup(r.text, "html.parser")
latitude = soup.find_all("div", class_="pb-image")
#count = str(soup.find("span", class_="active")).text

#lat = soup.find("data-iteminfo").text
#print(latitude)
for line in latitude:
    try:
        #a = soup.find("a", href="")
        data1 = str(line)
        if 'data-iteminfo' in data1:

            print("========================")
            data2 = data1.replace("<a data-iteminfo=","")
            #data3 = data2.replace("'","")
            data3 = data2.split("'")
            #data = json.loads(data3[1])
            print(data3[1])
        else:
            pass
    except json.decoder.JSONDecodeError:
        print("JSON ERROR")
        pass
sleep(5000)
        
