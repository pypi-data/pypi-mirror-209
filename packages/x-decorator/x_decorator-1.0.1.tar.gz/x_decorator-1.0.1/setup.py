import os

from setuptools import setup, find_packages

""" X_decorators setup script. """

from x_decorator import __version__ as version

HERE = os.path.abspath(os.path.dirname(__file__))

NAME = "x_decorator"
PACKAGE_NAME = "x_decorator"
PACKAGES = find_packages(exclude=["*.__old", "*.tests"])

setup(

    name=NAME,
    version=version,
    description=(
        "X Decorator [X Decorator is a python package for decorators that used for a variety of purposes, such as logging, memoization, and more.]"),
    long_description=open("long_description.rst").read(),
    long_description_content_type="text/x-rst",
    author="Muhammed Shokr",
    author_email="mohammedshokr2014@gmail.com",
    maintainer="Muhammed Shokr",
    maintainer_email="mohammedshokr2014@gmail.com",
    url="https://github.com/shokr/x_decorator",
    # download_url="https://github.com/shokr/x_decorator/archive/" "v%s.tar.gz" % version,
    keywords=["decorators", "Python"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Plugins",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Topic :: Software Development",
        "Topic :: Scientific/Engineering",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    license="BSD-3-Clause",
    packages=PACKAGES,
    include_package_data=True,
    install_requires=[
        'schedule',
    ],

)
