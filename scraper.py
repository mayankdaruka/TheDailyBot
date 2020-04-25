from bs4 import BeautifulSoup
from requests import get
import pandas as pd

df = pd.da

url = "https://www.icc-cricket.com/rankings/mens/team-rankings/test"
response = get(url)
print(response.text)
soup = BeautifulSoup(response.text, 'html.parser')

last_updated = soup.find_all('div', class_ = "rankings-table__last-updated")
first_ranked = soup.find_all('tr', class_ = "rankings-block__banner")
print(first_ranked[0])
first_ranked_tds = first_ranked[0].find_all('td')

rankings_last_updated = last_updated[0].text
first_ranked_country = first_ranked_tds[1].find_all('span')[1].text
first_ranked_matches = first_ranked_tds[2].text
first_ranked_points = first_ranked_tds[3].text
first_ranked_rating = first_ranked_tds[4].text.strip()


