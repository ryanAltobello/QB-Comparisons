from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup, Comment


soup = BeautifulSoup
index_url = 'https://www.pro-football-reference.com/players/E/EdwaTr01.htm'

print(index_url)
team_url = uReq(index_url)
page_html = team_url.read()
team_url.close()
page_soup = soup(page_html, "html.parser")

player_name = page_soup.find("h1", attrs={"itemprop": "name"}).text

passing_table = page_soup.find("table", {"id": "passing"}).tfoot.tr
stats = passing_table.find_all("td", {"class": "right"})

college = page_soup.find("strong", text="College").parent.a.text
birthplace = page_soup.find("span", attrs={"itemprop": "birthPlace"}).a.text
nfl_year = int(page_soup.find("table", {"id": "passing"}).tbody.tr.th.a.text)
college_year = str(nfl_year - 1)

filename = "qb_stats.sik"
f = open(filename, "a")
f.write("\n")
f.write(player_name + "," + birthplace + "," + college + "," + college_year + ",")
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
    playoff_footer = newsoup.find("tfoot").tr
    stats2 = playoff_footer.find_all("td", {"class": "right"})

    for stat2 in stats2:
        print(stat2.text, end=" ")
        f.write(stat2.text + ",")

    print("\n")
    f.write("\n")
                                        
f.close()