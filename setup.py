"""
    setup
    ~~~~~~~~~~~~~~
    项目的安装文件.

    :copyright: (c) 2019-10-08 by datochan.
"""
from setuptools import setup

from setuptools import setup, find_packages

setup(
    name='python-flask-quick-start',
    version='1.0',
    description="An python3 flask web framework template.",
    packages=find_packages(),
    entry_points={'core': ['settings = dirbot.settings']},
)