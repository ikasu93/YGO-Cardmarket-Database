conditionDict = {
    "1": "Mint",
    "2": "Near Mint",
    "3": "Excellent",
    "4": "Good",
    "5": "Light Played",
    "6": "Played",
    "7": "Poor"
}

def getCondition(num):
    return conditionDict[num]


languageDict = {
    "1": "Englisch",
    "3": "Deutsch"
}

def getLanguage(num):
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


def getSeries(num):
    return seriesDict[num]


def parseLanguage(txt_input):
    if txt_input == "EN":
        return "1"
    elif txt_input == "DE":
        return "3"
    else:
        return "2"


def parseEdition(txt_input):
    if txt_input == "1. Auflage" or txt_input == "1st Edition":
        return "Y"
    else:
        return "N"


def getCardDictInformation(name, series, isFirstEd, language):
    return {
        "name": name,
        "series": getSeries(series),
        "isFirstEd": isFirstEd,
        "card_language": language
    }