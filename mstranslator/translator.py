import sys
import requests
import authorizationheader

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
