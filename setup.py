from setuptools import setup, find_packages

setup(
    name="multi-asset-with-bitcoin",
    version='0.0.1',
    description="Macro Final Project Codebase",
    author="Mahima Raut",
    author_email="mahimaraut@uchicago.edu",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.26.4",
        "pandas>=2.2.3",
        "pdblp>=0.1.8",
        "blpapi>=3.24.11",
        "setuptools>=57.5.0"
    ],
    python_requires='>=3.11.5',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
