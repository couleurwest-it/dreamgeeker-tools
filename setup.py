#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import dreamtools
from dreamtools import cfgloader
from dreamtools import tools

#enregistrement des sources de bases (yaml)
directory = tools.dirproject()
mydir = tools.path_build(directory, 'cfg')
source = {}

for file, path_file in tools.dirparser(mydir):
    source[file] = f"{cfgloader.loading(path_file)}"

mysource = tools.path_build(directory, 'source.py')
with open(mysource, encoding='utf-8', mode='w') as src:
    src.write(f'source = {source.__str__()}')
cfg = ["cfg/*.yml"]
with open('README.md') as readme:
    long_description = readme.read()
#setup------------------------------
setup(

    name='dreamtools-dreamgeeker',
    version=dreamtools.__version__,
    packages=find_packages(),
    author="dreamgeeker",
    author_email="dreamgeeker@couleurwest-it.com",
    description="outils de developpement de base",
    long_description=long_description,

    # liste de dépendances pour votre lib
    # install_requires=["gunicorn", "docutils >= 0.3", "lxml==0.5a7"] ,
    install_requires=['setuptools','pyaml','requests', 'cerberus>= 1.3.2', 'pillow', 'pytz'
                      ,"urllib3", "whois==0.9.7","Cerberus== 1.3.2","Pillow == 8.0.1",  ],

    # Active la prise en compte du fichier MANIFEST.in
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
    packages=find_packages(),
    package_data={'dreamtools': cfg},
    include_package_data=True,
    python_requires='>=3.8',
    entry_points= {
        'console_scripts': [
            'tools-installer = scripts.__main__:setproject'
        ],
    }
)

# tester
# make html
# sphinx-build -b rinoh source _build/rinoh
# python setup.py install
# publier sur pypi
# $ python setup.py register
# Puis, il faut créer une distribution source (sdist) et le mettre en ligne (upload):
# python setup.py sdist upload
# mise a jour apres changement de version ! :-)

# python3 -m pip install --user --upgrade setuptools wheel
# python3 setup.py sdist bdist_wheel
# python3 -m twine upload --repository dreamtools dist/*