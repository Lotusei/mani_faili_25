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

#--------------------------------------------------------------------------------------------------

@app.route('/characters')
def get_characters():
    # 1. iegūstu varoņu vārdu sarakstu
    try:
        varonu_saraksts = requests.get("https://genshin.jmp.blue/characters")
        visi_vardi = varonu_saraksts.json() if varonu_saraksts.status_code == 200 else []
    except:
        visi_vardi = []

    # 2. Iegūstu izvēlētos datus par izvēlēto varoni
    selected_name = request.args.get('character_id')
    informacija = None

    if selected_name:
        try:
            varonu_info = requests.get(f"https://genshin.jmp.blue/characters/{selected_name}")
            if varonu_info.status_code == 200:
                informacija = varonu_info.json()
        except:
            pass


    return render_template('characters.html', names=visi_vardi, details=informacija)
    

#--------------------------------------------------------------------------------------------------

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
