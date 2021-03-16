from bs4 import BeautifulSoup
import requests

url = "https://rss.app/feeds/HfGgDE2X0vfrEaxt.xml"

def scrape_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, features='xml')
    tweets = soup.findAll('item')   
    tweet = []             
    for a in tweets:
        content = a.find('title').text
        link = a.find('link').text
        date = a.find('pubDate').text            
        tw = {
                    'content': content,
                    'link': link,
                    'date': date
        }
        tweet.append(tw)        
    return tweet

tweets = scrape_data(url)
for x in tweets:
    print(x)
