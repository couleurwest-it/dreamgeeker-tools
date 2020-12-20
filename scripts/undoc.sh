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
