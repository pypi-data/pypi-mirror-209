
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = [line.strip() for line in f.readlines()]

setup(
    name="creative-namer",
    version="1.1.0",
    packages=find_packages(),
    py_modules=['creative_namer'],
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'creative_namer = creative_namer:main',
        ],
    },
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',)
