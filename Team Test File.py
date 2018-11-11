from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup, Comment

soup = BeautifulSoup

team_url = uReq("https://en.wikipedia.org/wiki/List_of_New_Orleans_Saints_starting_quarterbacks")
page_html2 = team_url.read()
team_url.close()
page_soup2 = soup(page_html2, "html.parser")

player_table = page_soup2.find_all("table", {"class": "wikitable"})
for tables in player_table:
    year = 2000
    for y in range(19):
        player_table_year = tables.find("a", text=year)
        year += 1
        if player_table_year is not None:
            find_player_name = player_table_year.parent.parent
            player_name = find_player_name.select_one("td:nth-of-type(2)")
            player = player_name.findAll("a")
            for qbs in player:
                qb_name = qbs.get("title")
                print(qb_name)