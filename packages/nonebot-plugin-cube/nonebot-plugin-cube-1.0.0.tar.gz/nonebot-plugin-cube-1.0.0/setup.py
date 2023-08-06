#!/usr/bin/env python
#-*- coding:utf-8 -*
from setuptools import setup, find_packages
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='nonebot-plugin-cube',
    version='1.0.0',
    keywords=['nonebot2','plugin','cube'],
    description='Rubik\'s Cube plugin based on nonebot framework,基于nonebot框架的魔方插件',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='initialencounter',
    author_email='2911583893@qq.com',
    license = "MIT Licence",
    url = "https://github.com/initialencounter/nonebot-plugin-cube",
    include_package_data = True,
    packages=find_packages(),
    install_requires = ["nonebot", "pillow","numpy"],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
)