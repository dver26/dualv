from setuptools import setup, find_packages

with open("README.md", "r") as f:
    description = f.read()

setup(
    name='dualv',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'numpy>=2.5.0'
    ],
    long_description = description,
    long_description_content_type = "text/markdown"
)
