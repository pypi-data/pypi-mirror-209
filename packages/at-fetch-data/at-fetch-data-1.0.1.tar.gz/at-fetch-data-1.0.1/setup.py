from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='at-fetch-data',
    version='1.0.1',
    author='ctwel',
    description='',
    license = "MIT",
    readme = "README.md",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages = ["fetch"],
    install_requires=[
        'python>=3.8',
        'pandas>=1.0.0',
        'httpx>=0.24.0',
    ],
)
