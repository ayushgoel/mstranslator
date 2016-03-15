# mstranslator

Python wrapper for Microsoft Translate services.

The API lets you:

1. Create Authorization Header that can be used to query Microsft Translate APIs.
2. Detect language for given text.
3. Translate given text to another language supported by Microsft Translate.

Usage
-

```python

$ import mstranslator.translator as translator

# Create Config instance.
$ config = translator.Config("Client ID", "Client Secret")

# Create translator instance using the Config instance. This instance now uses
# the same config for all translation related tasks. You can create more than
# one instances if required.
$ translator = translator.Translator(config)

# Detect language of the given text. The detected language's code and an
# authorization header is returned.
$ translator.detect_language("Hello")

('en',
 u'Authorization Header')

# Translate a given text to another language (Hindi used in example here).
# Authorization header generated above in detect language call can be reused.
# If not given in argument, a new one is generated.
$ print translator.translate("hello", 'en', 'hi', u'Authorization Header')

नमस्कार

```

## Author

Ayush Goel, ayushgoel111@gmail.com

## License

mstranslator-2016 is available under the MIT license. See the LICENSE file for more info.
