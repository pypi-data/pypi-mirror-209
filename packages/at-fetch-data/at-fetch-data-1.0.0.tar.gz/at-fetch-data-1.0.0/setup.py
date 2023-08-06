from setuptools import setup

setup(
    name='at-fetch-data',
    version='1.0.0',
    author='ctwel',
    description='',
    license = "MIT",
    readme = "README.md",
    packages = ["fetch"],
    install_requires=[
        'python>=3.8',
        'pandas>=1.0.0',
        'httpx>=0.24.0',
    ],
)
