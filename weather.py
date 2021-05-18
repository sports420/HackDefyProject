import bs4
from bs4 import BeautifulSoup
import requests
import timeInfo

def getWeather(city, state):
    url = "https://newjersey.news12.com/weather"
    mainUrl = requests.get(url)
    soup = BeautifulSoup(mainUrl.content, "html.parser")

    divTemp = soup.find("div", {"class": "row"}).find("span").text

    print(f"The temperature in Edison, NJ is {divTemp}° Fahrenheit.")
    return f"The temperature in Edison, NJ is {divTemp}° Fahrenheit."
