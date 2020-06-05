import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')

soup = BeautifulSoup(res.text, 'html.parser')

links = soup.select('.storylink')
subtext = soup.select('.subtext')

def sort_by(x):
    
    return sorted(x, key= lambda k:k['votes'], reverse=True)


def create (links,subtext):
    hn = []
    for index , item in enumerate (links):
        title = links[index].getText()
        href = links[index].get('href', None)
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace('points',' '))
            if points >100:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_by(hn)
 
pprint.pprint(create(links,subtext))

 