import requests
import urllib
import sys

class Config:
    """Config to be given to an instance of translator to do the Authorization."""
    def __init__(self, translator_client_id, translator_client_secret):
        assert translator_client_id is not None
        assert type(translator_client_id) is str

        assert translator_client_secret is not None
        assert type(translator_client_secret) is str

        self.translator_client_id = translator_client_id
        self.translator_client_secret = translator_client_secret

class Translator:
    """An instance of this class can be used to detect language and translate text."""
    def __init__(self, config):
        self.config = config

    def __get_access_token(self):
        data = {"client_id": self.config.translator_client_id,
         "client_secret": self.config.translator_client_secret,
         "scope": 'http://api.microsofttranslator.com',
         "grant_type": 'client_credentials'}
        resp = requests.post(url='https://datamarket.accesscontrol.windows.net/v2/OAuth2-13', data=urllib.urlencode(data))
        return resp.json()["access_token"]

    def __authorization_header(self):
        access_token = self.__get_access_token()
        return "Bearer" + " " + access_token

    def detect_language(self, text):
        text = text.encode('utf-8')
        authorization_header = self.__authorization_header()
        headers = {"Authorization": authorization_header}
        data = {"text": text}
        resp = requests.get(url='http://api.microsofttranslator.com/v2/Http.svc/Detect', params=data, headers=headers)
        try:
            t = resp.text.encode('utf-8')
            # Different unicodes for different languages are not parsed correctly
            # with xml module.
            detected_language_code = t.split('>')[1].split('<')[0]
            return (detected_language_code, authorization_header)
        except Exception as e:
            sys.stderr.write(e)
            raise

    def translate(self, text, from_language, to_language, authorization_header):
        if authorization_header is None:
            authorization_header = self.__authorization_header()
        text = text.encode('utf-8')
        headers = {"Authorization": authorization_header}
        data = {"text": text,
         "from": from_language,
         "to": to_language}
        resp = requests.get(url='http://api.microsofttranslator.com/v2/Http.svc/Translate', params=data, headers=headers)
        try:
            t = resp.text.encode('utf-8')
            translatedText = t.split('>')[1].split('<')[0]
            return translatedText
        except Exception as e:
            sys.stderr.write("Could not parse XML {0}".format(resp.text))
            raise

if __name__ == '__main__':
    print translate(sys.argv[1], sys.argv[2], sys.argv[3])
