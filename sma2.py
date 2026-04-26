import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
soup = BeautifulSoup(requests.get(url).text, "html.parser")

quotes = [q.text for q in soup.find_all("span", class_="text")]

df = pd.DataFrame(quotes, columns=["Quote"])
print(df)

df.to_csv("quotes.csv", index=False)

"""
pip install requests
pip install beautifulsoup4
pip install pandas                  or for python3
pip3 install requests beautifulsoup4 pandas
"""
