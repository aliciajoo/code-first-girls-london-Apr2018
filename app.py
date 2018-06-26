from typing import List, Any

import flask
import requests
from newsapi import NewsApiClient
from flask import Flask, render_template
app = Flask(__name__)


from bs4 import BeautifulSoup

@app.route('/Resources')
def Resources():

    global summary
    source = requests.get('https://www.bbc.co.uk/search?q=pay+gap').text
    soup = BeautifulSoup(source, 'lxml')

    titles = []
    #hea = []
    #news = []

    for article in soup.find_all('article'):
        summary = article.find("p", class_="summary medium").text
        titles.append(summary)

        #for url in soup.find_all('a'):
            #print(url.get('href'))

    #heading = article.find("h1", itemprop="headline").text
    #hea.append(heading)

    return render_template('Resources.html', news=titles)

if __name__ == '__main__':
   app.run()