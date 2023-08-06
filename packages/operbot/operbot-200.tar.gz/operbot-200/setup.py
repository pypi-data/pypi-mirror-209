# This file is placed in the Public Domain


_author__ = "B.H.J. Thate <thatebhj@gmail.com>"
__version__ = 1


import os


from setuptools import setup


def read():
    return open("README.rst", "r").read()


setup(
    name="operbot",
    version="200",
    author="Bart Thate",
    author_email="thatebhj@gmail.com",
    url="http://github.com/operbot/operbot",
    description="operator bot",
    long_description=read(),
    long_description_content_type="text/x-rst",
    license="Public Domain",
    install_requires=[
                      "opr",
                     ],
    packages=[
              "operbot",
              "operbot.modules"
             ],
    scripts=[
             "bin/operbot",
             "bin/operbotd",
             "bin/operbotcmd",
             "bin/operbotctl"
            ],
    include_package_data=True,
    data_files=[
                ("operbot", ["files/operbot.service",]),
               ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: Public Domain",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only",
        "Intended Audience :: System Administrators",
        "Topic :: Communications :: Chat :: Internet Relay Chat",
        "Topic :: Software Development :: Libraries :: Python Modules",
     ],
)
