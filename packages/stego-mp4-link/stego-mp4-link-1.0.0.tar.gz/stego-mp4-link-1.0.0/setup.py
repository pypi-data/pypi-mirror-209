#!/usr/bin/env python

from io import open
from setuptools import setup

version ='1.0.0'

setup(
    name='stego-mp4-link',
    version=version,
    author='Kirill Osin',
    author_email='kiryusha.osin@yandex.ru',
    url='https://github.com/kib-sources/stego-mp4-link',
    download_url='https://github.com/kib-sources/stego-mp4-link/archive/refs/heads/master.zip',
    packages=['stego-mp4-link'],
    requires=['pycryptodomex', 'pythondotenv', 'requests', 'selenium', 'webdrivermanager', 'repackage'],
)