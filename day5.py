from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__, template_folder='templates')
app.env = "development"
app.debug = True

@app.route('/')
def index():
    return "Welcome, class day 5"

@app.route('/movies')
def movies():
    url = 'https://movie.daum.net/boxoffice/weekly'
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    soup = soup.select('.desc_boxthumb')
    return render_template('movies.html', soup=soup)

app.run(port=5000)