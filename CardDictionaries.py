conditionDict = {
    "1": "Mint",
    "2": "Near Mint",
    "3": "Excellent",
    "4": "Good",
    "5": "Light Played",
    "6": "Played",
    "7": "Poor"
}


def get_condition(num):
    return conditionDict[num]


languageDict = {
    "1": "Englisch",
    "3": "Deutsch"
}


def get_language(num):
    return languageDict[num]


seriesDict = {
    "MAGO": "Maximum-Gold",
    "LCKC": "Legendary-Collection-Kaiba-Mega-Pack",
    "OP04": "OTS-Tournament-Pack-4",
    "PRIO": "Primal-Origin",
    "BLRR": "Battles-of-Legend-Relentless-Revenge",
    "MP18": "Mega-Pack-2018",
    "MP19": "Mega-Pack-2019",
    "CIBR": "Circuit-Break",
    "OP11": "OTS-Tournament-Pack-11",
    "SOFU": "Soul-Fusion",
    "DUPO": "Duel-Power",
    "RIRA": "Rising-Rampage",
    "LEHD": "Legendary-Hero-Decks",
    "SHVA": "Shadows-in-Valhalla",
    "DANE": "Dark-Neostorm",
    "OP08": "OTS-Tournament-Pack-8"
}


def get_series(num):
    return seriesDict[num]


def parse_language(txt_input):
    if txt_input == "EN":
        return "1"
    elif txt_input == "DE":
        return "3"
    else:
        return "2"


def parse_edition(txt_input):
    if txt_input == "1. Auflage" or txt_input == "1st Edition":
        return "Y"
    else:
        return "N"


def get_card_dict_information(name, series, is_first_ed, language):
    return {
        "name": name,
        "series": get_series(series),
        "isFirstEd": is_first_ed,
        "card_language": language
    }
