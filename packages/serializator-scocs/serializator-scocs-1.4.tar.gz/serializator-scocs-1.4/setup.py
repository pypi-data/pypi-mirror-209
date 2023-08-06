from setuptools import setup, find_packages

from codecs import open
from os import path

setup(
    name="serializator-scocs",
    version="1.4",
    description="library for python serialization",
    long_description="SCoSC serialization/deserialization",
    long_description_content_type="text/markdown",
    author="Tarasenko Fyodor",
    author_email="tarasenkafiodar@gmail.com",
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
    packages=find_packages(),
    include_package_data=True
)
