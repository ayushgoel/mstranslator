mstranslator
-

Python wrapper for Microsoft Translate services.

The API lets you:

1. Detect language for given text.
2. Translate given text to another language supported by Microsft Translate.
3. `access_token` is managed by the package itself.

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

Steps to upload to PyPI
-

```bash

$ git pull
$ vi setup.py # Edit version here.
$ git commit -m "Update version to #NEW_VERSION"
$ python setup.py check # Should return no errors or warnings.
$ git tag # NEW_VERSION
$ git push --tags
$ git push
$ python setup.py sdist upload -r pypi # Upload to PyPI

```

Author
-

Ayush Goel, ayushgoel111@gmail.com

License
-

mstranslator-2016 is available under the MIT license. See the LICENSE file for more info.
