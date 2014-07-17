# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name='bakamecab',
    version='1.0',
    author='Artiom Basenko',
    author_email='demi.log@gmail.com',
    packages=['bakamecab', 'bakamecab.test'],
    url='https://github.com/Xifax/baka-mecab',
    license='LICENSE',
    description='Simplistic MeCab cli parser',
    long_description=open('README.md').read(),
    install_requires=[],
)
