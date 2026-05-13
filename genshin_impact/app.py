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

# 4. Funkcija, jaunumu skrāpēšanai paņemta no "mani paraugi" p6.py

def skrapet_virsrakstus():
    url = 'https://game8.co/games/Genshin-Impact/archives/316403'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        konteiners = soup.find(class_='archive-style-wrapper')
        
        dati = []
        if konteiners:
            virsraksti = konteiners.find_all(['h3', 'h4'])
            
            for v in virsraksti:
                teksts = v.get_text(strip=True)
                tips = v.name 
                
                # Pievienojam pašreizējo virsrakstu sarakstam
                dati.append({
                    'teksts': teksts,
                    'tips': tips
                })

                # PĀRBAUDE: Ja šī ir Snezhnaya, mēs pārtraucam ciklu
                if "Snezhnaya" in teksts:
                    break # Aptur skrāpēšanu pie šī vārda
        
        return dati
    except Exception as e:
        print(f"Kļūda: {e}")
        return []

@app.route('/nations')
def index():
    visi_virsraksti = skrapet_virsrakstus()
    return render_template('nations.html', saraksts=visi_virsraksti)




# def jaunumi_skr():                    
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
