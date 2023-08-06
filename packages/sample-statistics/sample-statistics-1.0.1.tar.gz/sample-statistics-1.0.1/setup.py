from setuptools import setup, find_packages

setup(
    name='sample-statistics',
    version='1.0.1',
    description='A package for calculating weighted statistics on a set of samples.',
    long_description='For docs and more information, visit the Github repo at https://github.com/christegk/sample-statistics.',
    author='Christos Tegkelidis',
    author_email='cteg@kth.se',
    packages=find_packages(),
    install_requires=['numpy', 'statsmodels'],
)
