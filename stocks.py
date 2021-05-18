import bs4
from bs4 import BeautifulSoup
import requests
import timeInfo

from datetime import *

def getDateAndTime():
    date = datetime.today().strftime("%B %d, %Y")
    time = datetime.now().strftime('%I:%M %p')

    return [str(date), str(time)]

def stockAlert(symbol, name):
    url = "https://finance.yahoo.com/quote/" + symbol
    mainUrl = requests.get(url)
    soup = bs4.BeautifulSoup(mainUrl.text, "html.parser")

    getPrice = soup.find("div", {"class": "D(ib) Va(m) Maw(65%) Ov(h)"}).find("span").text

    getTime = soup.find("div",
                        {"class": "C($tertiaryColor) D(b) Fz(12px) Fw(n) Mstart(0)--mobpsm Mt(6px)--mobpsm"}).find(
        "span").text

    timeStr = getTime[-1:9:-1]
    time = timeStr[::-1].strip()
    date = getDateAndTime()

    newName = name.lower()
    finalName = newName[0].upper() + newName[1:]

    print(f"\nThe price of {symbol} is ${getPrice} at {time} on {date[0]}.")
    return f"\nThe price of {sybmbol} is ${getPrice} at {time} on {date[0]}."
