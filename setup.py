# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in cheque_management/__init__.py
from cheque_management import __version__ as version

setup(
	name='cheque_management',
	version=version,
	description='For managing receivable and payable cheques',
	author='Direction',
	author_email='info@egdirection.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
