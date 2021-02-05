!#/bin/bash
"""Script d'intallation"""
"""
c:\\Users\\Ohanna\\Geekspace\\dreamtools\\.venv\\scripts\\activate
echo 'Modules gestion docstring :'
python -m pip install --upgrade pip
pip3.8 install sphinx
pip3.8 install rinohtype
echo ' - Installation des paquet : OK'
echo 'Modules gestion de pacquets :'
pip install --upgrade setuptools wheel

pip install twine
"""
echo 'Génération documentions'
cd docs
make html
sphinx-build -b rinoh source build/pdf

echo "Generation Package"
#python setup.py install
#python setup.py register
python setup.py sdist bdist_wheel
twine upload dist/*1.2.0*

#twine upload --repository testpypi dist/*1.0.4*
#echo "\tVersion PROD !"
#twine upload --repository dreamtools dist/*
pause


# tester
#sphinx-quickstart
# make html
# sphinx-build -b rinoh source _build/rinoh
# python setup.py install
# publier sur pypi
# $ python setup.py register
# Puis, il faut créer une distribution source (sdist) et le mettre en ligne (upload):
# python setup.py sdist upload
# mise a jour apres changement de version ! :-)

# pip install twine
# #python3 -m pip install --user --upgrade setuptools wheel
# python3 setup.py sdist bdist_wheel
# python3 -m twine upload --repository dreamtools dist/*

