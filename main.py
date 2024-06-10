import requests

from bs4 import BeautifulSoup

import transform

import load

if __name__ == "__main__" :

    print("GET REQUEST...")

    try :

        page = requests.get("https://liquipedia.net/valorant/VCT/2024/Stage_2/Masters/Statistics")
        soup = BeautifulSoup(page.content, "html.parser")
        data = transform.getData(soup)
        load.toCSV(data)

    except Exception as e :

        print(str(e))