import requests
from bs4 import BeautifulSoup
from CardDictionaries import get_condition, get_language

# define methods to retrieve card information from CardMarket
# get_txt2url()
# get_url()
# get_price()
# get_card_information()


nearmint = "2"
germany = "7"


def parse_txt2url(series, card_name, country, language, condition, is_first_ed):
    return "https://www.cardmarket.com/de/YuGiOh/Products/Singles/" + series+"/"\
           + card_name + "?sellerCountry=" + country+"&language=" + language+"&minCondition="\
           + condition + "&isFirstEd=" + is_first_ed


"""
Wir benutzen "BeautifulSoup", um auf Cardmarket zuzugreifen und den Preis zu entnehmen
"""
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML,like Gecko) Chrome/75.3770.100 Safari/537.36"
}


def get_url(card_dict, country, card_condition):
    return parse_txt2url(card_dict["card_series"], card_dict["card_name"], country, card_dict["card_language"],
                         card_condition, card_dict["isFirstEd"])


def get_price(card_dict, country, card_condition):
    url = get_url(card_dict, country, card_condition)

    print("Card: ", card_dict.get("card_name"), url)

    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    cardmarket_information = soup.find(id="table").get_text().split(" ")

    print("Card Infos: ", cardmarket_information)
    information_list = list(filter(lambda x: "€" in x, cardmarket_information))
    if not information_list:
        # if there are no sellers
        return 0
    else:
        return float(list(filter(lambda x: "€" in x, cardmarket_information))[0][1:-1].replace(",", "."))


def get_card_information(card_dict, country, card_condition):
    name = card_dict["card_name"]
    series = card_dict["card_series"]
    price = get_price(card_dict, country, card_condition)
    is_first_ed = card_dict["isFirstEd"]
    language = get_language(card_dict["card_language"])
    url = get_url(card_dict, country, card_condition)
    return {
        "card_name": name,
        "card_series": series,
        "price": price,
        "isFirstEd": is_first_ed,
        "card_language": language,
        "card_condition": get_condition(card_condition),
        "url": url
    }
