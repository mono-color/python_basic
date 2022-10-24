# pip install flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/main/<name>')
def main(name):
    return render_template('main.html', content=name, num=2)

@app.route('/list/')
def list():
    return render_template('list.html', board=['nick', 'jack', 'judy'])

if __name__ == '__main__':
  app.run(debug=True)