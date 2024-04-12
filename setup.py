from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='g2papi',
    version='1.0.3',
    author='Jordan Safer',
    author_email='genomics2proteins@gmail.com',
    description='A python client and CLI for easy access to G2P portal APIs',
    long_description=long_description,
    long_description_content_type="text/markdown",
    project_urls={
        "GitHub": "https://www.github.com/broadinstitute/g2papi",
        "G2P portal": "https://g2p.broadinstitute.org"
    },
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
