
import sys
from setuptools import setup
from os import system

# For convenience.
if sys.argv[-1] == "publish":
    system("python setup.py sdist")
    system("twine upload dist/*")

else:
    setup(
        name=YOUR_PACKAGE_NAME,
        version=0.1,
        author="Andy Casey",
        author_email="anderw.casey@monash.edu",
        license="MIT",
        classifiers=[
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3.6",
            "Topic :: Scientific/Engineering :: Astronomy",
            "Topic :: Scientific/Engineering :: Physics"
        ],
        install_requires=["numpy", "scipy", "six"],
        extras_require={
            "test": ["coverage"]
        },
        package_data={
            "": ["LICENSE"],
        },
        include_package_data=True,
        data_files=None
    )
