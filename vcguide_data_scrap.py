import requests
from bs4 import BeautifulSoup
import pandas as pd

start = "https://www.vcguide.co/?3d70cb88_page=1"
url = "https://www.vcguide.co/?3d70cb88_page={}"


pages = 213

reviews=[] 
ratings=[] 

count = 1

print("STARTING.........")

for page in range(1, pages):
    print("IN PAGE ", page)
    soup = BeautifulSoup(requests.get(url.format(page)).content, "html.parser")

    for a in soup.find_all('div', attrs={'class':'collection-item-2 w-dyn-item'}):
        review = a.find('blockquote', attrs={'class':'block-quote-2'})
        rating = a.find('h3', attrs={'class':'heading'})

        # print("Review: ", review.text)
        # print("Rating: ", rating.text)

        reviews.append(review.text)
        ratings.append(rating.text)

    count += 1

df = pd.DataFrame({'Reviews':reviews,'Rating':ratings}) 
df.to_csv('vcguide_data.csv', index=False, encoding='utf-8')