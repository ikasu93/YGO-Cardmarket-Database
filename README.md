# YGO-Cardmarket-Database

## Information
This is a fun project. The goal is to retrieve the value of your Yu-Gi-Oh cards based on Cardmarket price (eventually TCGPlayer price) and store in a database.
Here I decide to store in a MongoDB database which I access with a Python library called PyMongo. The work is in progress.

## Aim:
Scan or take a picture of your card or cards.
The program will detect the cards and the necessary information such as Language, Cardset, First edition and maybe also its condition.
The program will then calculate the prices and store the price and some information in the mongodb database.

## Requirements:
- mongodb
- Python 3.7
- Python Libraries: requests, bs4, pymongo, schedule, time, numpy, cv2 (Eventually I will create a Docker so that all environment parameter so that this step is unnecessary, optional I will write a bash script which installs all those libraries automatically)
