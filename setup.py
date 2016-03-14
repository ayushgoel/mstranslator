from distutils.core import setup

setup(
    name = 'mstranslator-2016',
    packages = ['mstranslator'],
    version = '0.1.0',
    description = 'Python wrapper to consume Microsoft translator API',
    author = 'Ayush Goel',
    author_email = 'ayushgoel111@gmail.com',
    url = 'https://github.com/ayushgoel/mstranslator',
    download_url = 'https://github.com/ayushgoel/mstranslator/archive/0.1.0.tar.gz',
    keywords = ['microsoft', 'translator', 'language'],
    requires = ['requests']
)
