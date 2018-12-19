from flask import Flask, render_template
import requests
import time
from bs4 import BeautifulSoup as bs

app = Flask(__name__)

@app.route('/index')
def index():
    print("hi")
    print("nice to meet you")
    return """
    <h1>Hello World</h1>
    <img src="https://taetaetae.github.io/2018/06/29/simple-web-server-flask-apache/flask-apache-python.png">
    <h3>SSAFY 화이팅 ㅎㅎ</h3>
    """


@app.route('/naverToon')
def naver_toon():
    today = time.strftime("%a").lower()
    print(today)
    naver_url = 'https://comic.naver.com/webtoon/weekdayList.nhn?week=tue'
    response = requests.get(naver_url).text
    soup = bs(response, 'html.parser')
    toons = []
    li = soup.select('.img_list li')
    for item in li:
      toon = {
        "title": item.select('dt a')[0].text,
        "url":  item.select('dt a')[0]["href"],
        "img_url":  item.select('.thumb img')[0]["src"]
      }
      toons.append(toon)
      
    return render_template('naver_toon.html', t=toons, toonlist=toon, li = soup.select('.img_list li'))