#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='TracSubPages',
      version='1.0',
      packages=find_packages(exclude=''),
      package_data={},
      author='Jimmy Theis',
      author_email='jimmy@jetheis.com',
      description='A Trac macro that displays the bodies of wiki pages inside other wiki pages',
      long_description=open('README.rst').read()+'\n'+open('CHANGES').read(),
      url='https://github.com/jetheis/TracSubPages',
      license='GPLv3',
      entry_points={'trac.plugins': ['TracSubPages = TracSubPages']},
      install_requires=['Trac'],
)
