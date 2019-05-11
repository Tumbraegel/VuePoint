# Adapted from http://flask.pocoo.org/docs/0.12/tutorial/
from setuptools import setup

setup(
    name='VuePoint',
    packages=['VuePoint'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)