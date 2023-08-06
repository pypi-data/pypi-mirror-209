import os
from setuptools import setup

# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "pyxecm",
    #version = "0.0.0",
    keywords = "opentext extendedecm contentserver otds appworks archivecenter",
    url = "https://pypi.org/project/pyxecm/",
    packages=['pyxecm'],
    long_description=read('README.md'),
)