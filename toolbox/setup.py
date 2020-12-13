#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

# notez qu'on import la lib
# donc assurez-vous que l'importe n'a pas d'effet de bord
import app

# Ceci n'est qu'un appel de fonction. Mais il est trèèèèèèèèèèès long
# et il comporte beaucoup de paramètres
setup(

    # le nom de votre bibliothèque, tel qu'il apparaitre sur pypi
    name='dreamgeeker-tools',

    # la version du code
    version=app.__version__,

    # Liste les packages à insérer dans la distribution
    # plutôt que de le faire à la main, on utilise la foncton
    # find_packages() de setuptools qui va cherche tous les packages
    # python recursivement dans le dossier courant.
    # C'est pour cette raison que l'on a tout mis dans un seul dossier:
    # on peut ainsi utiliser cette fonction facilement
    packages=find_packages(),

    # votre pti nom
    author="dreamgeeker",

    # Votre email, sachant qu'il sera publique visible, avec tous les risques
    # que ça implique.
    author_email="dreamgeeker@couleurwest-it.com",

    # Une description courte
    description="outils de deeloppement de base",
    long_description=open('README.md').read(),

    # liste de dépendances pour votre lib
    # install_requires=["gunicorn", "docutils >= 0.3", "lxml==0.5a7"] ,
    install_requires=["PyYAML==5.3.1", "requests==2.25.0", "urllib3==1.26.2", "whois==0.9.7"],

    # Active la prise en compte du fichier MANIFEST.in
    include_package_data=True,

    # Une url qui pointe vers la page officielle de votre lib
    url='https://github.com/couleurwest/dreamgeeker-tools',

    # Il est d'usage de mettre quelques metadata à propos de sa lib
    # Pour que les robots puissent facilement la classer.
    # La liste des marqueurs autorisées est longue:
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers.
    #
    # Il n'y a pas vraiment de règle pour le contenu. Chacun fait un peu
    # comme il le sent. Il y en a qui ne mettent rien.
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 1 - Préparation",
        "License :: OSI Approved",
        "Natural Language :: French",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Topic :: Communications",
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
