#!/user/bin/env python

from io import open
from setuptools import setup

"""
:authors: Ivan Kudinov
:license: The MIT License (MIT) see LICENSE file
:copyright: (c) 2023 Ivan Kudinov
"""

version = "0.0.2"

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="gpswe",
    version=version,

    author="Ivan Kudinov",
    author_email="marvel.2012@mail.ru",

    description=(
        u'Python library for parse, save and work ' 
        u'with Wialon and EGTS data'
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",

    url="https://github.com/KudinovIvan/gpswe",
    download_url="https://github.com/KudinovIvan/gpswe/archive/v{}.zip".format(
        version
    ),

    license='The MIT License (MIT) see LICENSE file',

    packages=['gpswe'],
    install_requires=["asyncio", "pydantic", "crcmod", "asyncpg", "geopy"],

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: CPython',
    ]
)