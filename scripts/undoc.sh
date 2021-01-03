c:\\Users\\Ohanna\\Geekspace\\dreamtools\\.venv\\scripts\\activate
echo "Extraction docstring :"
python -m pip install --upgrade pip
pip3.8 install sphinx
pip3.8 install rinohtype

echo 'Installation des paquet : OK'
cd c:\\Users\\Ohanna\\Geekspace\\dreamtools\\docs\\source

make html
sphinx-build -b rinoh source _build/rinoh

echo "Extraction terminée"

cd c:\\Users\\Ohanna\\Geekspace\\dreamtools\\

echo "Generation Package"
echo "\tMake Installation tarball"
python setup.py sdist bdist_wheel
python setup.py register
echo "\tVersion Test [O/n]?"
pip install twine
twine upload  dist/*1.0.0*
twine upload --repository testpypi dist/*1.0.4*
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

