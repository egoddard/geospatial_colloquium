from flask import Flask, request, url_for, render_template
import requests
from requests_oauthlib import OAuth1
import os

app = Flask(__name__)

# Keys for the Yelp API
CONSUMER_KEY = '6LhGlPGDtiHafX_uHH_pZA'
CONSUMER_SECRET = 'FPJ2dp0eoClSAaJpyjmTkmbWy4Q'
TOKEN = 'UWFIdiVtJcu54lXV-7bMoLQaU6tTVPty'
TOKEN_SECRET = 'JIqy43nx5HR8QeLGNWR7g5PRBiM'

@app.route('/')
def index():
    """Returns the index.html template to the client."""
    return render_template('index.html')

@app.route('/within')
def within():
    """
    Makes a request to the Yelp API to search for bars within 500 feet of the
    latitude and longitude included in the request and returns a JSON result
    object.
    """
    url = "http://api.yelp.com/v2/search"
    params = {'radius_filter': 500,
              'category_filter': 'bars,breweries,pubs,irish_pubs,gastropubs',
              'll': '{lat},{lon}'.format(lat=float(request.args.get('lat')),
                                         lon=float(request.args.get('lng'))),
              'sort': 2}

    # We have to authenticate with the yelp api, so create an oauth request
    # using the keys above
    oauth = OAuth1(CONSUMER_KEY, CONSUMER_SECRET, TOKEN, TOKEN_SECRET,
            signature_type='query')
    result = requests.get(url, params=params, auth=oauth)

    return result.text

if __name__ == '__main__':
    app.run(debug=True)
