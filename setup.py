#!/usr/bin/env python
#coding:utf-8
"""
  Author:   --<v1ll4n>
  Purpose: Setup install minihydra
  Created: 04/15/17
"""

from setuptools import setup, find_packages

packages = find_packages()

requires = ['g3ar', 'configparser']

version = '0.5.0'

#
# README.md
#
try:
    readme = None
    with copen('README.md',  encoding='utf-8') as f:
        readme = f.read()
except:
    readme = 'MiniHydra Frame - Fuzz and Burst EVERYTHING!' + \
        '\nGithub: https://github.com/VillanCh/minihydra' + \
        '\nREADME.md: https://github.com/VillanCh/minihydra/blob/master/README.md\n\n'
    #history = 'https://github.com/VillanCh/g3ar/blob/master/HISTORY.md'

setup(
    name = 'minihydra',
    version = version,
    description = 'Minihydra frame - burst and fuzz everything!',
    long_description = readme,
    author = 'v1ll4n',
    author_email = 'v1ll4n@villanch.top',
    url = 'https://github.com/VillanCh/minihydra',
    packages = packages,
    package_data = {
        '':['README.md', 'tests.py'],
        './minihydra/':['minihydra.conf',],
        './minihydra/dicts/':['default_un.txt', 'default_pd.txt'],
    },
    package_dir = {
        'minihydra':'minihydra'
    },
    include_package_data = True,
    install_requires = requires,
    license = 'BSD 2-Clause License',
    zip_safe = False
)