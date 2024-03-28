from setuptools import setup, find_packages

setup(
    name='g2papi',
    version='1.0.0',
    author='Jordan Safer',
    author_email='genomics2proteins@gmail.com',
    description='A tool for interacting with the G2P API.',
    packages=find_packages(),
    install_requires=[
        'requests',
        'pandas'
    ],
    entry_points={
        'console_scripts': [
            'g2papi=g2papi.cli:main',
        ],
    },
)
