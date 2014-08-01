import os
from setuptools import setup, find_packages


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()
        
    
setup(
    name = "H2Oprops",
    version = "0.1.0",
    author = "Nicolas Edh",
    author_email = "nicolas.edh@gmail.com",
    description = ("A simple GUI for using the iapws package"),
    license = "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    keywords = "iapws water properties gui",
    url = "https://github.com/nicolasedh/H2Oprops.git",
    long_description=read('README.md'),
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: GPLv3",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Programming Language :: Python :: 2.7"
#        "Programming Language :: Python",
        "Topic :: Scientific/Engineering"
    ],
    install_requires = ["iapws>=1.0.3"],
    entry_points={
    'gui_scripts': [
        'h2oprops=H2Oprops.H2Oprops:main']
    },
    packages = find_packages()
)

