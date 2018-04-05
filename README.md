
I always forget how to register and upload packages to PyPi, and the documentation
is always out of date.

Follow these steps:

1. ``git clone https://github.com/andycasey/setup-on-pypi.git``

2. ``cd setup-on-pypi/``

3. Change `YOUR_PACKAGE_NAME` in `setup.py`

4. ``conda install twine``

5. ``python setup.py sdist``

6. ``twine upload dist/*``
