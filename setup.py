from distutils.core import setup

version = '1.0.0'

setup(
    name = 'mstranslator-2016',
    packages = ['mstranslator'],
    version = version,
    description = 'Python wrapper to consume Microsoft translator API',
    author = 'Ayush Goel',
    author_email = 'ayushgoel111@gmail.com',
    license='MIT',
    url = 'https://github.com/ayushgoel/mstranslator',
    download_url = 'https://github.com/ayushgoel/mstranslator/archive/{0}.tar.gz'.format(version),
    keywords = ['microsoft', 'translator', 'language', 'mstranslator'],
    requires = ['requests']
)
