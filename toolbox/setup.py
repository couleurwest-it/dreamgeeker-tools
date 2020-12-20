#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import toolbox
from toolbox import cfgloader
from toolbox import tools

#enregistrement des sources de bases (yaml)
mydir = tools.path_build(tools.get_dir_path(), 'cfg')
source = {}

for file, path_file in tools.paser_directory(mydir):
    source[file] = f"{cfgloader.loading(path_file)}"

mysource = tools.path_build(tools.get_dir_path(), 'source.py')
with open(mysource, encoding='utf-8', mode='w') as src:
    src.write(f'source = {source.__str__()}')

#setup------------------------------
setup(

    name='dreamtools',
    version=toolbox.__version__,
    packages=find_packages(),
    author="dreamgeeker",
    author_email="dreamgeeker@couleurwest-it.com",
    description="outils de developpement de base",
    long_description=open('README.md').read(),

    # liste de dépendances pour votre lib
    # install_requires=["gunicorn", "docutils >= 0.3", "lxml==0.5a7"] ,
    install_requires=["PyYAML==5.3.1", "requests==2.25.0", "urllib3==1.26.2", "whois==0.9.7",
                      "Cerberus== 1.3.2","Pillow == 8.0.1",  ],

    # Active la prise en compte du fichier MANIFEST.in
    include_package_data=True,

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

    # C'est un système de plugin, mais on s'en sert presque exclusivement
    # Pour créer des commandes, comme "django-admin".
    # Par exemple, si on veut créer la fabuleuse commande "proclame-sm", on
    # va faire pointer ce nom vers la fonction proclamer(). La commande sera
    # créé automatiquement.
    # La syntaxe est "nom-de-commande-a-creer = package.module:fonction".
    # entry_points={
    #    'console_scripts': [
    #        'proclame-sm = sm_lib.core:proclamer',
    #    ],
    # },

    # A fournir uniquement si votre licence n'est pas listée dans "classifiers"
    # ce qui est notre cas
    license="WTFPL"

)

# tester
# python setup.py install
# publier sur pypi
# $ python setup.py register
# Puis, il faut créer une distribution source (sdist) et le mettre en ligne (upload):
# python setup.py sdist upload
# mise a jour apres changement de version ! :-)
