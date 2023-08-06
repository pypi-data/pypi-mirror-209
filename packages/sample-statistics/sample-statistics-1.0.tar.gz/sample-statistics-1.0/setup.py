from setuptools import setup, find_packages

setup(
    name='sample-statistics',
    version='1.0',
    description='A package for calculating weighted statistics on a set of samples.',
    author='Christos Tegkelidis',
    author_email='cteg@kth.se',
    packages=find_packages(),
    install_requires=['numpy', 'statsmodels'],
)
