from config import LINK_CITIES_INFORMATION
import requests
from bs4 import BeautifulSoup


def get_html(link: str) -> str:
    st_accept = "text/html"
    st_useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 YaBrowser/26.8.0.0 Safari/537.36"

    headers = {
        "Accept": st_accept,
        "User-Agent": st_useragent
    }

    request = requests.get(link, headers)

    return request.text


def get_cities(src: str) -> dict:
    soup = BeautifulSoup(src, "html.parser")
    
    tr = soup.find_all("tr")
    
    cities = {}
    
    for i in tr:
        if i.find("a") is not None:
            cities[i.find("a").text.lower()] = int("".join(i.find("td", class_="px-4 py-3 font-numeric text-neutral-700 dark:text-neutral-300 md:px-5").text.split("\xa0")))


    return cities


def population_validation(name_city: str, population: int, is_new_city: bool) -> bool:
    if is_new_city:
        return population <= 41_900_000

    