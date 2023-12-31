from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in arsh_customization/__init__.py
from arsh_customization import __version__ as version

setup(
	name="arsh_customization",
	version=version,
	description="Ariosh Customization",
	author="Optimum Solutions Ltd",
	author_email="optisol.ltd@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
