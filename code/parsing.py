from config import LINK_CITIES_INFORMATION, USER_AGENT_FOR_RUSSIAN_CITES, ACCEPT_FOR_RUSSIAN_CITIES
import requests
from bs4 import BeautifulSoup


def get_html(link: str, user_agent: str, accept) -> str:
    st_accept = accept
    st_useragent = user_agent

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


def population_validation(name_city: str, population: int, is_new_city: bool) -> tuple:
    if is_new_city:
        if population <= 41_900_000:
            return (True, None)
        
        return (False, "В городе не может проживать больше 41,9 млн человек")

    russian_cities = get_cities(get_html(LINK_CITIES_INFORMATION, USER_AGENT_FOR_RUSSIAN_CITES, ACCEPT_FOR_RUSSIAN_CITIES))

    try:
        real_population = russian_cities[name_city.lower()]

        if abs(1 - (population / real_population)) <= 0.1:
            return (True, None)

        return (False, "Данная численность населения откланяется на 10% от данных переписи 2025 года")

    except KeyError:
        return (False, "Города нету в базе данных Российских городов, проверьте правильно ли Вы написали название или просто отметьте его как новый город")

