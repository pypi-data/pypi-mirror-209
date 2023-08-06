from setuptools import setup, find_packages

with open("README.md", "r") as fh:
	long_description = fh.read()

setup(
	name="askCO",
	version="0.0.3",
	author="Lucy Schrader",
	author_email="lucy@schrader.nz",
	license="MIT License",
	description="Python interface for Te Papa's collections API",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/lucyschrader/askCO",
	packages=find_packages(include=["requests"]),
	install_requires=["requests"],
	python_requires=">=3.7",
	keywords=["python", "museum", "api"],
	classifiers=[
		"Development Status :: 3 - Alpha",
		"License :: OSI Approved :: MIT License",
		"Intended Audience :: Education",
		"Programming Language :: Python :: 3",
		"Natural Language :: English",
		])