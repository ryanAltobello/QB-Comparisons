from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from selenium import webdriver



index_url = 'https://www.pro-football-reference.com/players/P/PlumJa00.htm'
# opening up connection grabbing the page
team_url = uReq(index_url)
# offload content into variable
page_html = team_url.read()
# close connection
team_url.close()

# html parsing
page_soup = soup(page_html, "html.parser")

passing_table = page_soup.find("table", {"id": "passing"})
passing_footer = passing_table.find("tfoot")
career_row = passing_footer.find("tr")
stats = career_row.findAll("td", {"class": "right"})

playoff_table = page_soup.find("div", {"id": "all_passing_playoffs"})

second = playoff_table.find("table", {"id": "passing_playoffs"})
print(second)

"""
playoff_footer = playoff_table.find("tfoot")
playoff_row = playoff_footer.find("tr")
stats2 = playoff_row.findAll("td", {"class": "right"})


filename = "qb_stats.csv"
f = open(filename, "a")
f.write("\n")

for stat in stats:
    print(stat.text, end=" ")
    f.write(stat.text + ",")
for stat2 in stats2:
    print(stat2.text, end=" ")
    f.write(stat2.text + ",")

f.close()

# print(career_row)
"""
