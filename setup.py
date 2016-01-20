# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 11:53:49 2016

@author: nsf
"""

from distutils.core import setup
import py2exe

incs=[
      "sip","scipy",
      "scipy.integrate",
      "scipy.special.*",
      "scipy.linalg.*",
      "scipy.sparse.csgraph._validation"
      ]

opts = {"py2exe":{"includes":incs}}

#setup(console=['H2Oprops.py'], options=opts)
#setup(windows=['H2Oprops.py'], options=opts)


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()
        
    
setup(
#    console=['H2Oprops.py'],
    windows=['H2Oprops.py'],
    name = "H2Oprops",
    version = "0.1.0",
    author = "Nicolas Edh",
    author_email = "nicolas.edh@gmail.com",
    description = ("A simple GUI for using the iapws package"),
    license = "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    keywords = "iapws water properties gui",
    url = "https://github.com/nicolasedh/H2Oprops.git",
#    long_description=read('README.md'),
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
    options=opts
)