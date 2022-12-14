import requests
from bs4 import BeautifulSoup
import pandas as pd

start = "http://thefunded.com/?page=1"
url = "http://thefunded.com/?page={}"


pages = 360

reviews=[] 
ratings=[] 

count = 1

print("STARTING.........")

for page in range(1, pages):
    print("IN PAGE ", page)
    soup = BeautifulSoup(requests.get(url.format(page)).content, "html.parser")

    for a in soup.find_all('div', attrs={'id':'post'}):
        review = a.find_all('p')
        text = ""
        for a in review:
            # print("Review: ", a.text)
            text = text + " " + a.text
        # rating = a.find('h3', attrs={'class':'heading'})

        # print("Review: ", text)
        # print("Rating: ", rating.text)

        reviews.append(text)
        # ratings.append(rating.text)

    count += 1

df = pd.DataFrame({'Reviews':reviews}) 
df.to_csv('thefunded_data_2.csv', index=False, encoding='utf-8')