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
        "Flask==1.1.1",
        "Flask-HTTPAuth==3.3.0",
        "Flask-Login==0.4.1",
        "Flask-Migrate==2.5.2",
        "Flask-Principal==0.4.0",
        "Flask-Script==2.0.6",
        "Flask-Security==3.0.0",
        "Flask-SQLAlchemy==2.4.1",
        "PyMySQL==0.9.3",
        "SQLAlchemy==1.3",
    ],
    license="MIT",
    name='python-flask-quick-start',
    packages=find_packages(),
    version='1.2',
)
