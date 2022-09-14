from flask import Flask, render_template
from load_equip import LoadEquip

app = Flask(__name__)

@app.route('/')
def index_page():
    return render_template('index.html')


@app.route('/choose-hero/')
def start_game():
    result = LoadEquip()
    return render_template('hero_choosing.html', result=result.load)

if __name__ == "__main__":
    app.run(port=80, debug=True)
