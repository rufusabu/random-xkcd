import requests
from random import randint
from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route('/')
def index():
    # Get count of latest comic
    upperLim = int(requests.get('https://xkcd.com/info.0.json').json()['num'])

    # Get random comic between num - upperLim
    data = requests.get(
        f"http://xkcd.com/{randint(1, upperLim)}/info.0.json").json()

    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
