#!/usr/bin/env python

from io import open
from setuptools import setup

"""
:author: Beengoo
:licanse: MIT
:copyright: (C) 2022 Beengoo 
"""

version = "0.2"

long_description = "Donatello.py is a simple unofficial library for the Donatello API"

setup(
    name='donatello',
    version=version,

    author='Beengoo',
    author_email='olddft@gmail.com',

    description=(
        u'Donatello.py is a simple unofficial library for the Donatello API'
    ),
    long_description=long_description,

    url="https://github.com/Beengoo/donatello.py",
    download_url="https://github.com/Beengoo/donatello.py/archive/refs/heads/master.zip",

    license="MIT",

    packages=['donatello'],
    requires=['requests'],

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Service :: Donatello API'
        'Programming Language :: Python'
    ]
)
