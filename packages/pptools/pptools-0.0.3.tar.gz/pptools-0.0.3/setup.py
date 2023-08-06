from setuptools import setup
import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='pptools',
    version='0.0.3',
    description='An assistant module for writing parsers',
    author='Alexander554',
    author_email='gaa.280811@gmail.com',
    license='MIT',
    packages=['pptools'],
    install_requires=['requests', 'pillow', 'aiohttp', 'bs4', 'selenium', 'lxml'],
    readme="README.md",
    long_description=long_description,
    long_description_content_type='text/markdown',
)