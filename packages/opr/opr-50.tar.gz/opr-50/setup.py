# This file is placed in the Public Domain.


"object programming version"


from setuptools import setup


def read():
    return open("README.rst", "r").read()


setup(
    name="opr",
    version="50",
    author="B.H.J. Thate <thatebhj@gmail.com>",
    author_email="thatebhj@gmail.com",
    url="http://github.com/operbot/opr",
    zip_safe=True,
    description="object programming runtime",
    long_description=read(),
    long_description_content_type="text/x-rst",
    license="Public Domain",
    packages=[
              "opr",
             ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: Public Domain",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries :: Python Modules",
     ],
)
