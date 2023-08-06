import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name= "GrappyLfjv",
    version= "0.0.17",
    description= "Simplification de la création de graphiques avec matplotlib",
    long_description=read("README.md"),
    long_description_content_type='text/markdown',
    py_modules=["grappy"],
    package_dir={"": "src"},
    install_requires = [
        "matplotlib > 3.0"
    ],
    url="https://github.com/Benjamin-Trevian/Grappy",
    author="Benjamin Trévian",
    author_email="benjamin.trevian@hotmail.com",
)