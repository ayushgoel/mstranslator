import requests
import urllib
import constants

def get_access_token():
    data = {"client_id": constants.translator_client_id,
     "client_secret": constants.translator_client_secret, "scope": 'http://api.microsofttranslator.com',
     "grant_type": 'client_credentials'}
    resp = requests.post(url='https://datamarket.accesscontrol.windows.net/v2/OAuth2-13', data=urllib.urlencode(data))
    return resp.json()["access_token"]

def authorization_header():
    access_token = get_access_token()
    print "Using token", access_token
    return "Bearer" + " " + access_token
