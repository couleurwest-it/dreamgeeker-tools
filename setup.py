#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import dreamtools
from dreamtools import cfgloader
from dreamtools import tools

cfg = ["cfg/*.yml"]
setup(

    name='dreamtools-dreamgeeker',
    version=dreamtools.__version__,

    packages= find_packages(),
    author="dreamgeeker",
    author_email="dreamgeeker@couleurwest-it.com",
    description="outils de developpement de base",
    long_description=open('README.md').read(),
    install_requires=["pyaml", "requests", "urllib3", "cerberus>= 1.3.2","pillow >= 8.0.1"],

    package_data = {'dreamtools' : cfg },
    #scripts = ["scripts"],
    include_package_data=True,
    python_requires='>=3.8',

    # Une url qui pointe vers la page officielle de votre lib
    url='https://github.com/couleurwest/dreamgeeker-tools',
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: French",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development",
    ],

    # La syntaxe est "nom-de-commande-a-creer = package.module:fonction".
    entry_points= {
        'console_scripts': [
            'tools-installer = scripts.__main__:setproject'
        ],
    }

)