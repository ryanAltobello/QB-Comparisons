from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


index_url = 'https://en.wikipedia.org/wiki/List_of_starting_quarterbacks_in_the_National_Football_League'
# opening up connection grabbing the page
team_url = uReq(index_url)
# offload content into variable
page_html = team_url.read()
# close connection
team_url.close()
# html parsing
page_soup = soup(page_html, "html.parser")

team_table = page_soup.find("table", {"class": "wikitable"})
team_table_body = team_table.find("tbody")
team_table_rows = team_table_body.findAll("tr")
rows = team_table_rows

for row in rows:
    team_table_data = row.find("td")
    if team_table_data is not None:
        get_link_element = team_table_data.find("a", text="list")
        get_link = get_link_element.get("href")
        full_team_link = "https://en.wikipedia.org" + get_link

        team_url = uReq(full_team_link)
        page_html2 = team_url.read()
        team_url.close()
        page_soup2 = soup(page_html2, "html.parser")

        player_table = page_soup2.find("a", text="2000").parent.parent
        player_name = player_table.select_one("td:nth-of-type(2)")
        player = player_name.findAll("a")

        for players in player:
            qb_name = players.get("title")
            PFR_url = "https://www.pro-football-reference.com/players/" + qb_name[qb_name.find(" ") + 1] + "/" + qb_name[qb_name.find(" ") + 1:qb_name.find(" ") + 5] + qb_name[0:2] + "00.htm"
            qb_name_2 = qb_name[qb_name.find(" ") + 1]
            print(PFR_url)
            









'''
for countries in country_table:
    partial_link = countries.find("a")
    get_country_link = partial_link.get("href")
    full_country_link = "https://en.wikipedia.org" + get_country_link

    country_url = uReq(full_country_link)
    page_html2 = country_url.read()
    country_url.close()
    page_soup2 = soup(page_html2, "html.parser")

    country_name = page_soup2.find("h1", {"id": "firstHeading"})
    country = country_name.text
    species_table = page_soup2.find("div", {"id": "mw-pages"})
    if species_table is not None:
        li = species_table.findAll("li")
        lis = li[0]
        for lis in li:
            a = lis.find("a")
            species = unidecode(a.text)
            print(country + ", " + species)
            filename = "endemicspecies.csv"
            f = open(filename, "a")
            f.write(country + "," + species + "\n")

f.close()
'''
