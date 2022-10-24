from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', name='Nick')

@app.route('/coin')
def coin():
    res = requests.get('https://api.upbit.com/v1/market/all')
    coin_list = json.loads(res.content)
    print(coin_list)
    return render_template('coin.html', coins=coin_list)

if __name__ == '__main__':
    app.run(debug=True)

