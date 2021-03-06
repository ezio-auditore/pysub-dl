#!/usr/bin/env python
"""pysub-dl project"""

requirements = []

try:
    from setuptools import setup, find_packages
except ImportError:
    requirements.append('setuptools')
try:
    import BeautifulSoup
except ImportError:
    requirements.append('BeautifulSoup')

try:
    import requests
except ImportError:
    requirements.append('requests')

setup(name = 'pysub-dl',
    version = '0.1',
    description = "A script to download subtitles",
    long_description = "A script to download subtitles",
    platforms = ["Linux"],
    author = "iamsudip",
    author_email = "iamsudip@programmer.net",
    url = "https://github.com/iamsudip/pysub-dl",
    license = "MIT",
    packages = find_packages(),
    install_requires = requirements,
    dependency_links = ['https://pypi.python.org/pypi/requests/1.2.3',
                        'https://pypi.python.org/pypi/BeautifulSoup/3.2.1'
],
    include_package_data = True,
    scripts = ['pysub-dl']
    )
