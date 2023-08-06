from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pygredients',
    version='0.1.3',
    description='Pygredients is an open-source Python library for data structures, algorithms and design patterns available on PyPi.',
    long_description=f"{long_description}",
    long_description_content_type="text/markdown",
    author='François Boulay-Handfield',
    author_email="fbhworks@icloud.com",
    url="https://github.com/FBH514/pygredients",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "twine>=4.0.0",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="data structures algorithms design patterns",
    python_requires=">=3.9"
)