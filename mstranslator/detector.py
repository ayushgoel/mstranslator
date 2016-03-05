import sys
import requests
import authorizationheader

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

if __name__ == '__main__':
    print detect_language(sys.argv[1])
