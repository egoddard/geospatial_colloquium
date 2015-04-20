from flask import Flask, request, url_for, redirect, render_template
import requests
from requests_oauthlib import OAuth1
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
