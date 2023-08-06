from setuptools import setup, find_packages

classifiers = [
'Development Status :: 5 - Production/Stable',
'Intended Audience :: Education',
'Operating System :: Microsoft :: Windows :: Windows 10',
'License :: OSI Approved :: MIT License',
'Programming Language :: Python :: 3'


]

setup(

name = 'archeSetup',
version='0.0.2',
description='This is the setup the basic Application library',
long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
url='',
author='Arche',
author_email='rkdyava@gmail.com',
classifiers=classifiers,
keywords='add',
packages=find_packages(),
install_requires=['']





)