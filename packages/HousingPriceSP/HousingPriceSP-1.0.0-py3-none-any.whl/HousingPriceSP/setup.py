# setup.py placed at root directory
import tarfile
from setuptools import setup, find_packages

setup(
    name='HousingPriceSP',
    version='1.0.0',
    author='Prakash Singh',
    description='Package to Predict housing Price!',
    long_description='This Package will help to predict housing price using regression model and using differnt parameters',
    packages=['HousingPriceSP'],
    python_requires=">=3.6",
    install_requires=['pandas', 'tarfile', 'six', 'sklearn', 'numpy', 'pickle']

)