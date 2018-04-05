
I always forget how to register and upload packages to PyPi, and the documentation
is always out of date.

Follow these steps:

1. ``git clone https://github.com/andycasey/setup-on-pypi.git``

2. ``cd setup-on-pypi/``

3. If you don't have one already: ``cp .pypirc ~/.pypirc`` and update the `~/.pypirc` file with your PyPi username and password.

4. Change `YOUR_PACKAGE_NAME` in `setup.py`

5. ``conda install twine``

6. ``python setup.py sdist``

7. ``twine upload dist/*``
