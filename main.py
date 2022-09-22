from unicodedata import name
from flask import Flask
app = Flask(__name__)
@app.route('/')

def index():
    return "HolaMonda"

app.run(debug = True)

