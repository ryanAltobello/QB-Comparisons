from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup, Comment


soup = BeautifulSoup
index_url = 'https://www.pro-football-reference.com/players/B/BlakJe00.htm'

team_url = uReq(index_url)
page_html = team_url.read()
team_url.close()
page_soup = soup(page_html, "html.parser")

player_name = page_soup.find("h1", attrs={"itemprop": "name"}).text

passing_table = page_soup.find("table", {"id": "passing"})
passing_footer = passing_table.find("tfoot")
career_row = passing_footer.find("tr")
stats = career_row.find_all("td", {"class": "right"})

filename = "qb_stats.csv"
f = open(filename, "a")
f.write("\n")
f.write(player_name)

f.write(",")

for stat in stats:
    if(stat.text != ""):
        print(stat.text, end=" ")
        f.write(stat.text + ",")

f.write("\n")
f.write(",")

playoff_table = page_soup.find("div", {"id": "all_passing_playoffs"})
if playoff_table is not None:
    comment = playoff_table.find(text=lambda html_comment: isinstance(html_comment, Comment))
    newsoup = soup(comment, "html.parser")
    playoff_footer = newsoup.find("tfoot")
    career_row2 = playoff_footer.find("tr")
    stats2 = career_row2.find_all("td", {"class": "right"})


    for stat2 in stats2:
        print(stat2.text, end=" ")
        f.write(stat2.text + ",")

    f.write("\n")
    f.close()
