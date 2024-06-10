import requests

from bs4 import BeautifulSoup

import etl

if __name__ == "__main__" :

    print("GET REQUEST...")

    try :

        page = requests.get("https://liquipedia.net/valorant/VCT/2024/Stage_2/Masters/Statistics")
        soup = BeautifulSoup(page.content, "html.parser")
        data = etl.getData(soup)
        etl.toCSV(data)

    except Exception as e :

        print(str(e))