from setuptools import setup, find_packages

from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name="python_imagemanipulating",
    version="0.0.3",
    description="Easily manipulate images with python_imagemanipulating",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://python-imagemanipulating.readthedocs.io/",
    author="saucrio",
    # author_email="example@email.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
    packages=["python_imagemanipulating"],
    include_package_data=True,
    install_requires=["Pillow", "requests"]
)