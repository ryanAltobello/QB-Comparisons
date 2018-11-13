from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup, Comment


soup = BeautifulSoup
index_url = 'https://www.pro-football-reference.com/players/E/EdwaTr01.htm'

print(index_url)
team_url = uReq(index_url)
page_html = team_url.read()
team_url.close()
page_soup = soup(page_html, "html.parser")

college_year = int(page_soup.find("table", {"id": "passing"}).tbody.tr.th.a.text)
print(college_year - 1)

passing_table = page_soup.find("table", {"id": "passing"}).tfoot.tr
stats = passing_table.find_all("td", {"class": "right"})


for stat in stats:
    if(stat.text != ""):
        print(stat.text, end=" ")