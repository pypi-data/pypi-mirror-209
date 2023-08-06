
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = [line.strip() for line in f.readlines()]

setup(
    name="to-pip",
    version="2.0.0",
    packages=find_packages(),
    package_data={'': ['*.*']},
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'to_pip = to_pip:main, hi = hi:main',
        ],
    },
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',)
