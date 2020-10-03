# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in nextcertification/__init__.py
from nextcertification import __version__ as version

setup(
	name='nextcertification',
	version=version,
	description='NextCertification',
	author='Sameer',
	author_email='sshaikh@dexciss.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
