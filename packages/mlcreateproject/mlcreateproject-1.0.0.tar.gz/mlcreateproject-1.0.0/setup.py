from setuptools import setup, find_packages

setup(
    name="mlcreateproject",
    version="1.0.0",
    author="Faqih Hamami",
    author_email="dhinza702@gmail.com",
    description="a python package for building machine learning project structure",
    packages=find_packages(),
)

# python setup.py sdist bdist_wheel
# twine check dist/*
# twine upload dist/*