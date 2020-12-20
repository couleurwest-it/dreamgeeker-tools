echo "Extraction docstring :"
cd docs
echo "\t HTML"
make html

echo "\t PDF"
sphinx-build -b rinoh source _build/rinoh

echo "Extraction terminée"
cd ..

echo "Generation Package"
echo "\tMake Installation tarball"
python setup.py sdist bdist_wheel
python setup.py register
echo "\tVersion Test [O/n]?"
twine upload --repository testpypi dist/*1.0.4*
#echo "\tVersion PROD !"
#twine upload --repository dreamtools dist/*

