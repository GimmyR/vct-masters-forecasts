from bs4 import BeautifulSoup

def getData(soup: BeautifulSoup) -> list :

    """
    This function gets a table of the name of a player, his team and his average combat score from a HTML page.
    """

    result = [
        ["player", "team", "acs"]
    ]

    table = soup.find("table", class_="wikitable wikitable-striped sortable")
    rows = table.find_all("tr")

    for i in range(1, len(rows)) :

        cells = rows[i].find_all("td")
        links = cells[1].find_all("a")

        player = links[1].string
        team = cells[2].find("span", class_="team-template-team-icon").get("data-highlightingclass")
        acs = int(cells[10].string)

        result.append([player, team, acs])

    return result