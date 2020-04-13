# -*- coding: utf-8 -*-


from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sample',
    version='0.1.0',
    description='Sample package for Python',
    long_description=readme,
    author='Mike Chirico',
    author_email='mchirico@gmail.com',
    url='https://github.com/mchirico/python',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
