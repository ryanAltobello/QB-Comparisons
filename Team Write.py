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
                PFR_url = "https://www.pro-football-reference.com/players/" + qb_name[qb_name.find(" ") + 1] + "/" + qb_name[qb_name.find(" ") + 1:qb_name.find(" ") + 5] + qb_name[0:2] + "00.htm"
                qb_name_2 = qb_name[qb_name.find(" ") + 1]
                
                print(PFR_url)

                qb_url = uReq(PFR_url)
                page_html3 = qb_url.read()
                qb_url.close()
                page_soup3 = soup(page_html3, "html.parser")

                player_name = page_soup3.find("h1", attrs={"itemprop": "name"}).text

                passing_table = page_soup3.find("table", {"id": "passing"})
                passing_footer = passing_table.find("tfoot")
                career_row = passing_footer.find("tr")
                stats = career_row.find_all("td", {"class": "right"})

                # filename = "qb_stats.csv"
                # f = open(filename, "a")
                # f.write("\n")
                # f.write(player_name)
                # f.write(",")

                for stat in stats:
                    if(stat.text != ""):
                        print(stat.text, end=" ")
                        # f.write(stat.text + ",")
                
                # f.write("\n")
                # f.write(",")

                playoff_table = page_soup3.find("div", {"id": "all_passing_playoffs"})
                if playoff_table is not None:
                    comment = playoff_table.find(text=lambda html_comment: isinstance(html_comment, Comment))
                    newsoup = soup(comment, "html.parser")
                    playoff_footer = newsoup.find("tfoot")
                    career_row2 = playoff_footer.find("tr")
                    stats2 = career_row2.find_all("td", {"class": "right"})

                    for stat2 in stats2:
                        print(stat2.text, end=" ")
                        # f.write(stat2.text + ",")

                    print("\n")
                    # f.write("\n")
                    # f.close()