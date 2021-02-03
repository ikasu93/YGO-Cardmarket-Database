import requests
from bs4 import BeautifulSoup
from CardDictionaries import getCondition, getLanguage

# define methods to retrieve card information from CardMarket
# get_txt2url()
# get_url()
# get_price()
# get_card_information()


nearmint = "2"
germany = "7"

def parse_txt2url(series, card_name, country, language, condition, isFirstEd):
    return "https://www.cardmarket.com/de/YuGiOh/Products/Singles/"+series+"/"+card_name+"?sellerCountry="+country+"&language="+language+"&minCondition="+condition+"&isFirstEd="+isFirstEd


"""
Wir benutzen "BeautifulSoup", um auf Cardmarket zuzugreifen und den Preis zu entnehmen
"""
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML,like Gecko) Chrome/75.3770.100 Safari/537.36"
}


def get_url(card_dict, country, card_condition):
    return parse_txt2url(card_dict["card_series"], card_dict["card_name"],
                  country, card_dict["card_language"], card_condition, card_dict["isFirstEd"])


def get_price(card_dict, country, card_condition):
    url = get_url(card_dict, country, card_condition)

    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    cardmarket_information = soup.find(id="table").get_text().split(" ")
    return float(list(filter(lambda x: "€" in x, cardmarket_information))[0][1:-1].replace(",", "."))


def get_card_information(card_dict, country, card_condition):
    name = card_dict["card_name"]
    series = card_dict["card_series"]
    price = get_price(card_dict, country, card_condition)
    is_first_ed = card_dict["isFirstEd"]
    language = getLanguage(card_dict["card_language"])
    url = get_url(card_dict, country, card_condition)
    return {
        "card_name": name,
        "card_series": series,
        "price": price,
        "isFirstEd": is_first_ed,
        "card_language": language,
        "card_condition": getCondition(card_condition),
        "url": url
    }

