from bs4 import BeautifulSoup
from requests import get
import pandas as pd

# ICCurl = "https://www.icc-cricket.com/rankings/mens/team-rankings/test"
# ICCurl = "https://www.icc-cricket.com/rankings/mens/team-rankings/t20i"
# ICCurl = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
# ICCurl = "https://www.icc-cricket.com/rankings/womens/team-rankings/t20i"
ICCurl = "https://www.icc-cricket.com/rankings/womens/team-rankings/odi"

def cricketRankings(url):
    response = get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    last_updated = soup.find_all('div', class_ = "rankings-table__last-updated")
    first_ranked = soup.find_all('tr', class_ = "rankings-block__banner")
    first_ranked_tds = first_ranked[0].find_all('td')

    all_rankings = []

    rankings_last_updated = last_updated[0].text
    first_ranked_country = first_ranked_tds[1].find_all('span')[1].text
    first_ranked_matches = first_ranked_tds[2].text
    first_ranked_points = first_ranked_tds[3].text
    first_ranked_rating = first_ranked_tds[4].text.strip()

    all_rankings.append(['1', first_ranked_country, first_ranked_matches, first_ranked_points, first_ranked_rating])

    rest_countries = soup.find_all('tr', class_ = "table-body")
    for country in rest_countries:
        info_array = []
        country_tds = country.find_all('td')
        country_ranking = country_tds[0].text
        country = country_tds[1].find_all('span')[1].text
        country_matches = country_tds[2].text
        country_points = country_tds[3].text
        country_rating = country_tds[4].text
        info_array.append(country_ranking)
        info_array.append(country)
        info_array.append(country_matches)
        info_array.append(country_points)
        info_array.append(country_rating)
        all_rankings.append(info_array)
    print(all_rankings)


cricketRankings(ICCurl)