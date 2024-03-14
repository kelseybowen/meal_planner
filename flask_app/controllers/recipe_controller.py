from flask_app import app
from flask import render_template, request, redirect, session, flash, url_for

@app.route('/')
def index():
    return render_template("index.html")

