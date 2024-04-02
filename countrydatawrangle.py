from bs4 import BeautifulSoup
import requests
import pandas as pd
import re


url = 'https://geographyfieldwork.com/WorldCapitalCities.htm'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

def remove_text_within_brackets(text):
    # Define a regular expression pattern to match text within brackets
    pattern = r'\[.*?\]'
    # Use re.sub() to replace the matched pattern with an empty string
    result = re.sub(pattern, '', text)
    return result

clist = []

element = soup.select('#anyid td')
for elem in element:
    clist.append(elem.text)
countries = []
capitals = []
for i in range(len(clist)):
    clist[i] = remove_text_within_brackets(clist[i])
    clist[i] = clist[i].replace("(very limited international recognition)", "")
    if i % 2 == 0:
        countries.append(clist[i])
    else:
        capitals.append(clist[i])

df = pd.DataFrame({'Countries': countries, 'Capitals': capitals})
df.to_csv('C:/Users/themi/Downloads/countrycapital2.csv', index=False)
