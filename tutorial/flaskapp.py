from flask import Flask, request, url_for, redirect, render_template
import requests
from requests_oauthlib import OAuth1
import os

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'


if __name__ == '__main__':
    app.run()
