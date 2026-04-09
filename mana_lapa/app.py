# from flask import Flask    # 1. Importē Flask klasi

# app = Flask(__name__)           # 2. Izveido lietotnes instanci

# @app.route('/')              # 3. Saista URL ar funkciju
# def home():                    # 4. Funkcija, kas izpildīsies
#     return "Sveika pasaule!"   # 5. Atgriež atbildi pārlūkam

# if __name__ == '__main__':   # 6. Vai skripts tiek palaists tieši?
#     app.run(debug=True)         # 7. Palaid attīstības serveri

# ------------------------------------

# from flask import Flask

# app = Flask(__name__)

# @app.route('/')          # localhost:5000
# def home():
#     return "Sākumlapa"

# @app.route('/par-mani')   # localhost:5000/par-mani
# def about():
#     return "Par mani lapa"

# @app.route('/kontakti')   # localhost:5000/kontakti
# def kontakti():
#     return "Kontakti lapa"

# if __name__ == '__main__':
#     app.run(debug=True)

# -------------------------------------------------------

# from flask import Flask

# from flask import Flask, render_template  # ← pievienots render_template

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('home.html')  # ← atgriež HTML failu

# if __name__ == '__main__':
#     app.run(debug=True)

# -----------------------------------------------------------

# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('home.html')

# @app.route('/par-mani')
# def about():
#     return render_template('about.html')

# if __name__ == '__main__':
#     app.run(debug=True)

