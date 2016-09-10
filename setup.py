# -*- coding: utf-8 -*-

from setuptools import setup

setup(
        name="pluralizefr",
        description="pluralize for french language",
        long_description=open("README.rst").read(),
        version="0.0.1",
        url="https://github.com/sblondon/pluralizefr",
        packages=[
            "pluralizefr",
            ],
        test_suite='tests',
        )

