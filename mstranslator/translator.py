"""Python wrapper for Microsoft Translate services."""

import urllib
import sys
import requests
import time


class Config(object):
    """Config to be given to an instance of translator to do the Authorization."""

    def __init__(self, translator_client_id, translator_client_secret):
        assert translator_client_id is not None
        assert type(translator_client_id) is str

        assert translator_client_secret is not None
        assert type(translator_client_secret) is str

        super(Config, self).__init__()
        self.translator_client_id = translator_client_id
        self.translator_client_secret = translator_client_secret


class Translator(object):
    """An instance of this class can be used to detect language and translate text."""

    def __init__(self, config):
        assert isinstance(config, Config) is True
        super(Translator, self).__init__()
        self.config = config
        self.access_token = self.token_expiry = None

    def _get_access_token(self):
        data = {
            "client_id": self.config.translator_client_id,
            "client_secret": self.config.translator_client_secret,
            "scope": 'http://api.microsofttranslator.com',
            "grant_type": 'client_credentials'
        }
        resp = requests.post(url='https://datamarket.accesscontrol.windows.net/v2/OAuth2-13',
                             data=urllib.urlencode(data))
        if not resp.ok:
            resp.raise_for_status()

        resp_content = resp.json()
        token_expiry = time.time() + int(resp_content["expires_in"])  # in seconds
        access_token = resp_content["access_token"]

        return (access_token, token_expiry)

    def _authorization_header(self):
        # Auth tokens are only valid for a limited number of seconds.
        # Token expiry is sent by the server at the time of obtaining the
        # token and can be used to auto-refresh the token before making a
        # new request, post expiry time.
        if (not self.token_expiry) or (self.token_expiry < time.time()):
            self.access_token, self.token_expiry = self._get_access_token()

        return "Bearer" + " " + self.access_token

    def detect_language(self, text):
        text = text.encode('utf-8')
        authorization_header = self._authorization_header()
        headers = {"Authorization": authorization_header}
        data = {"text": text}
        resp = requests.get(url='http://api.microsofttranslator.com/v2/Http.svc/Detect',
                            params=data, headers=headers)
        if not resp.ok:
            resp.raise_for_status()

        try:
            t = resp.text.encode('utf-8')
            # Different unicodes for different languages are not parsed
            # correctly with xml module.
            detected_language_code = t.split('>')[1].split('<')[0]
            return detected_language_code
        except Exception as e:
            sys.stderr.write(e)
            raise

    def translate(self, text, from_language, to_language):
        text = text.encode('utf-8')
        authorization_header = self._authorization_header()
        headers = {"Authorization": authorization_header}
        data = {
            "text": text,
            "from": from_language,
            "to": to_language
        }
        resp = requests.get(url='http://api.microsofttranslator.com/v2/Http.svc/Translate',
                            params=data, headers=headers)

        if not resp.ok:
            resp.raise_for_status()

        try:
            t = resp.text.encode('utf-8')
            translated_text = t.split('>')[1].split('<')[0]
            return translated_text
        except Exception:
            sys.stderr.write(u"Could not parse XML {0}".format(resp.text))
            raise
