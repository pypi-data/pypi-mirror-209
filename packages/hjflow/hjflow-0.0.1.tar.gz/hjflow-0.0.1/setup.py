from setuptools import setup, find_packages

setup(
    name='hjflow',
    version='0.0.1',
    author='Ville Ahlgren',
    description='Library for defining program flow in HJSON',
    packages=find_packages(),
    install_requires=[
        'hjson',
    ],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
