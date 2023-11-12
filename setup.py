#!/usr/bin/python
##-------------------------------##
## PyTrader                      ##
## Written By: Ryan Smith        ##
##-------------------------------##

## Imports
from setuptools import setup

## Body
with open("requirements.txt", 'r') as f:
    deps = f.read().split('\n')[:-1]

setup(
    name="PyTrader",
    version="0.0.1",
    packages=["pytrader"],
    install_requires=deps
)
