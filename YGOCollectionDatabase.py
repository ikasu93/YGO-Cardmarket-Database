import pymongo
from CardmarketScraper import get_card_information
"""
Some data to push into function to retrieve prices
"""
card_info_dict2 = {
        "card_name": "Blue-Eyes-White-Dragon",
        "card_series": "Maximum-Gold",
        "isFirstEd": "Y",
        "card_language": "1"
}
card_info_dict3 = {
        "card_name": "Knightmare-Phoenix",
        "card_series": "Flames-of-Destruction",
        "isFirstEd": "N",
        "card_language": "3"
}
card_info_dict4 = {
        "card_name": "Maxx-C",
        "card_series": "Collectors-Tins-2012",
        "isFirstEd": "N",
        "card_language": "3"
}
card_info_dict6 = {
        "card_name": "Dark-Magician-Girl",
        "card_series": "Speed-Duel-Tournament-Pack-1",
        "isFirstEd": "N",
        "card_language": "1"
}
card_info_dict7 = {
        "card_name": "Blue-Eyes-White-Dragon-V-2",
        "card_series": "Starter-Deck-Kaiba-Reloaded",
        "isFirstEd": "N",
        "card_language": "3"
}
card_info_dict8 = {
        "card_name": "Number-S39-Utopia-the-Lightning",
        "card_series": "OTS-Tournament-Pack-4",
        "isFirstEd": "N",
        "card_language": "3"
}
card_info_dict9 = {
        "card_name": "Bujinki-Amaterasu-V-2",
        "card_series": "Primal-Origin",
        "isFirstEd": "Y",
        "card_language": "3"
}
card_info_dict10 = {
        "card_name": "Sky-Striker-Ace-Kaina",
        "card_series": "OTS-Tournament-Pack-11",
        "isFirstEd": "N",
        "card_language": "3"
}
card_info_dict11 = {
        "card_name": "Firewall-Dragon",
        "card_series": "2018-MegaTin-Mega-Pack",
        "isFirstEd": "Y",
        "card_language": "3"
}
card_info_dict12 = {
        "card_name": "Nekroz-of-Brionac",
        "card_series": "Duel-Power",
        "isFirstEd": "Y",
        "card_language": "3"
}
card_info_dict13 = {
        "card_name": "Elemental-HERO-Liquid-Soldier",
        "card_series": "Legendary-Duelists-Magical-Hero",
        "isFirstEd": "Y",
        "card_language": "3"
}
card_info_dict14 = {
        "card_name": "Droll-Lock-Bird",
        "card_series": "Legendary-Collection-Kaiba-Mega-Pack",
        "isFirstEd": "Y",
        "card_language": "3"
}
card_info_dict15 = {
        "card_name": "Dark-Magician-V-2",
        "card_series": "Starter-Deck-Yugi-Reloaded",
        "isFirstEd": "N",
        "card_language": "3"
}
card_info_dict16 = {
        "card_name": "Dark-Magician-Girl-V-2",
        "card_series": "Yugis-Legendary-Decks",
        "isFirstEd": "Y",
        "card_language": "1"
}
card_info_dict17 = {
        "card_name": "Exodia-the-Forbidden-One",
        "card_series": "Yugis-Legendary-Decks",
        "isFirstEd": "Y",
        "card_language": "1"
}
card_info_dict18 = {
        "card_name": "Right-Leg-of-the-Forbidden-One",
        "card_series": "Yugis-Legendary-Decks",
        "isFirstEd": "Y",
        "card_language": "1"
}
card_info_dict19 = {
        "card_name": "Left-Arm-of-the-Forbidden-One",
        "card_series": "Yugis-Legendary-Decks",
        "isFirstEd": "Y",
        "card_language": "1"
}
card_info_dict20 = {
        "card_name": "Left-Leg-of-the-Forbidden-One",
        "card_series": "Yugis-Legendary-Decks",
        "isFirstEd": "Y",
        "card_language": "1"
}
card_info_dict21 = {
        "card_name": "Right-Arm-of-the-Forbidden-One",
        "card_series": "Yugis-Legendary-Decks",
        "isFirstEd": "Y",
        "card_language": "1"
}
card_info_dict22 = {
        "card_name": "Dimension-Shifter",
        "card_series": "2019-Gold-Sarcophagus-Tin",
        "isFirstEd": "N",
        "card_language": "1"
}
card_info_dict23 = {
        "card_name": "Slifer-the-Sky-Dragon",
        "card_series": "Yugis-Legendary-Decks",
        "isFirstEd": "N",
        "card_language": "1"
}
card_info_dict24 = {
        "card_name": "Slifer-the-Sky-Dragon",
        "card_series": "Legendary-Decks-II",
        "isFirstEd": "N",
        "card_language": "1"
}
card_info_dict25 = {
        "card_name": "Slifer-the-Sky-Dragon",
        "card_series": "Premium-Gold",
        "isFirstEd": "N",
        "card_language": "3"
}
card_info_dict26 = {
        "card_name": "The-Winged-Dragon-of-Ra",
        "card_series": "Yugis-Legendary-Decks",
        "isFirstEd": "N",
        "card_language": "1"
}
card_info_dict27 = {
        "card_name": "The-Winged-Dragon-of-Ra",
        "card_series": "Legendary-Decks-II",
        "isFirstEd": "N",
        "card_language": "1"
}
card_info_dict28 = {
        "card_name": "Black-Luster-Soldier-Envoy-of-the-Beginning",
        "card_series": "Premium-Gold",
        "isFirstEd": "N",
        "card_language": "1"
}
card_info_dict30 = {
        "card_name": "Knightmare-Unicorn",
        "card_series": "2019-Gold-Sarcophagus-Tin-Mega-Pack",
        "isFirstEd": "Y",
        "card_language": "1"
}
card_info_dict31 = {
        "card_name": "Blue-Eyes-Alternative-Ultimate-Dragon",
        "card_series": "2019-Gold-Sarcophagus-Tin",
        "isFirstEd": "N",
        "card_language": "1"
}

card_list = [card_info_dict2, card_info_dict3, card_info_dict4, card_info_dict6, card_info_dict7, card_info_dict8,
             card_info_dict9, card_info_dict10, card_info_dict11, card_info_dict12, card_info_dict13, card_info_dict14,
             card_info_dict15, card_info_dict16, card_info_dict17, card_info_dict18, card_info_dict19, card_info_dict20,
             card_info_dict21, card_info_dict22, card_info_dict23, card_info_dict24, card_info_dict25, card_info_dict26,
             card_info_dict27, card_info_dict28, card_info_dict30, card_info_dict31]

nearmint = "2"
excellent = "3"
germany = "7"


"""
Database
"""
client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["ygo_database"]

col = db["cards"]


"""
Add to Database
list2database: only adds items to the database
"""


def list2database(card_dict_list, country, condition):
    col.delete_many({})
    for i in range(len(card_dict_list)):
        col.insert_one(get_card_information(card_dict_list[i], country, condition))


def main():
    list2database(card_list, germany, nearmint)


main()
