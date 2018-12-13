from flask import Flask
from flask_bootstrap import Bootstrap
from flask import render_template
import app.charts as charts

from . import app




@app.route("/")
def hello():
    _map = charts.map.create_charts()
    return render_template('index.html')
