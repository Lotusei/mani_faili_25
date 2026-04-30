from flask import Flask, render_template, request # 1. Importē Flask klasi

import requests
from bs4 import BeautifulSoup

app = Flask(__name__)           # 2. Izveido lietotnes instanci

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

# def jaunumi_skr():                    # 4. Funkcija, jaunumu skrāpēšanai
#     url = "https://genshin-impact.fandom.com/wiki/Genshin_Impact_Wiki" 
# 
# @app.route('/nations') 
# def nations():
#     return render_template('nations.html')


# # # nolasa API "https://genshin.dev/" un parāda to HTML dokumentā

# @app.route('/characters')
# def character_info():
#     response = requests.get("https://genshin.dev/characters/albedo")
#     if response.status_code == 200:
#         data = response()
#         joki = data['value']
#         return render_template('p2.html', joke=joki)
#     else:
#         return "Nevar saņemt informāciju"

if __name__ == '__main__':   # 6. Vai skripts tiek palaists tieši?
    app.run(debug=True)         # 7. Palaid attīstības serveri
