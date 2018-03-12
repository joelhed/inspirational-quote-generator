import secrets
import mkchain
from flask import Flask, render_template


app = Flask("inspirational_quote")
quote_model = mkchain.Model()

with open('dataset.txt') as dataset:
    for line in dataset:
        quote_model.train(line)


@app.route("/")
def index():
    quote = quote_model.generate(50)
    rand_str = secrets.token_urlsafe(16)
    return render_template("index.html", quote=quote, rand_str=rand_str)
