from ez_setup import use_setuptools

use_setuptools()
from setuptools import setup, find_packages

setup(name='TracSubPages',
      version='0.5',
      packages=find_packages(exclude=''),
      package_data={},
      author='Jimmy Theis',
      author_email='jimmy@jetheis.com',
      description='A Trac macro that displays the bodies of wiki pages inside other wiki pages',
      long_description=open('README').read()+'\n'+open('CHANGES').read(),
      url='http://github.com/jetheis/TracSubPages',
      license='GPLv3',
      entry_points={'trac.plugins': ['TracSubPages = TracSubPages']},
)
