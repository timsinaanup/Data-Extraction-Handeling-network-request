import requests
import json

info = []

try:
    for n in range(1,10):
        url = "https://bg.annapurnapost.com/api/tags/news?page="+ str(n) +"&per_page=10&tag=%E0%A4%B8%E0%A4%82%E0%A4%B8%E0%A4%A6%E0%A5%80%E0%A4%AF-%E0%A4%A8%E0%A4%BF%E0%A4%B0%E0%A5%8D%E0%A4%B5%E0%A4%BE%E0%A4%9A%E0%A4%A8"
        payload={}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        jsondata= json.loads(response.text)
        articles = jsondata['data']
        for article in articles:
            author = article['author']['name']
            news = article['title']
            date = article['publishOn']
            info.append({
            'author': author,
            'news' : news,
            'date' : date
            })

except:
    pass
    
page_size = 10
pages = [info[i:i+page_size] for i in range(0, len(info), page_size)]

for i, page in enumerate(pages):
    with open("page_{}.json".format(i+1), "w") as outfile:
        json.dump(page, outfile)