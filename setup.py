"""
    setup
    ~~~~~~~~~~~~~~
    项目的安装文件.

    :copyright: (c) 2019-10-08 by datochan.
"""
from setuptools import setup, find_packages

setup(
    author="datochan",
    author_email="datochan@qq.com",
    description="An python3 flask web framework template.",
    install_requires=[
        "Flask==2.2.3",
        "Flask-HTTPAuth==4.7.0",
        "Flask-Login==0.6.2",
        "Flask-Migrate==4.0.4",
        "Flask-Principal==0.4.0",
        "Flask-Security==3.0.0",
        "Flask-SQLAlchemy==3.0.3",
        "PyMySQL==1.0.2",
        "SQLAlchemy==2.0.4",
    ],
    license="MIT",
    name='python-flask-quick-start',
    packages=find_packages(),
    version='1.4',
)
