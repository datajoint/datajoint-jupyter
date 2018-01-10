#! /usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='datajoint-jupyter',
    version='0.1',
    author='Chris Turner',
    author_email='chris@vathes.com',
    description='datajoint jupyter utilities',
    license='proprietary',
    keywords='datajoint demo jupyter',
    url='http://github.com/datajoint/datajoint-jupyter',
    packages=find_packages(include=['djwidgets']),
)
