import requests
import urllib
import sys

class Config():
    """Config to be given to an instance of translator to do the Authorization."""
    def __init__(self, translator_client_id, translator_client_secret):
        super(Config, self).__init__()
        assert translator_client_id is not None
        assert type(translator_client_id) is str

        assert translator_client_secret is not None
        assert type(translator_client_secret) is str

        self.translator_client_id = translator_client_id
        self.translator_client_secret = translator_client_secret

class Translator():
    """An instance of this class can be used to detect language and translate text."""
    def __init__(self, config):
        super(Translator, self).__init__()
        self.config = config

    def __get_access_token():
        data = {"client_id": self.config.translator_client_id,
         "client_secret": self.config.translator_client_secret,
         "scope": 'http://api.microsofttranslator.com',
         "grant_type": 'client_credentials'}
        resp = requests.post(url='https://datamarket.accesscontrol.windows.net/v2/OAuth2-13', data=urllib.urlencode(data))
        return resp.json()["access_token"]

    def __authorization_header():
        access_token = get_access_token()
        print "Using token", access_token
        return "Bearer" + " " + access_token

    def detect_language(text):
        text = text.encode('utf-8')
        print "Detecting language for text", text
        authorization_header = authorizationheader.authorization_header()
        headers = {"Authorization": authorization_header}
        data = {"text": text}
        resp = requests.get(url='http://api.microsofttranslator.com/v2/Http.svc/Detect', params=data, headers=headers)
        try:
            t = resp.text.encode('utf-8')
            # Different unicodes for different languages are not parsed correctly
            # with xml module.
            detected_language_code = t.split('>')[1].split('<')[0]
            print "Language detected: ", detected_language_code
            return (detected_language_code, authorization_header)
        except Exception as e:
            print "Could not parse XML", resp.text
            print e

    def translate(text, from_language, to_language, authorization_header=authorizationheader.authorization_header()):
        text = text.encode('utf-8')
        print "Translating text", text
        headers = {"Authorization": authorization_header}
        data = {"text": text,
         "from": from_language,
         "to": to_language}
        resp = requests.get(url='http://api.microsofttranslator.com/v2/Http.svc/Translate', params=data, headers=headers)
        try:
            t = resp.text.encode('utf-8')
            translatedText = t.split('>')[1].split('<')[0]
            print "Got translation: ", translatedText
            return translatedText
        except Exception as e:
            print "Could not parse XML", resp.text
            print e

if __name__ == '__main__':
    print translate(sys.argv[1], sys.argv[2], sys.argv[3])
