from setuptools import setup, find_packages

setup(
    name="stocksymboltools",
    version="0.2",
    packages=find_packages(),
    description="A library to get stock symbols",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Pavan krishna",
    author_email="narne.pavankrishna1@gmail.com",
    url="https://github.com/pavan-krishna123/stocks",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    install_requires=[
        'pandas',
    ],
)


