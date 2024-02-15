#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = ['pytest>=3', ]

setup(
    author="prashant patel",
    author_email='prashantz7242@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="opensource low resource usage image processor library written in python.",
    install_requires=requirements,
    license="BSD license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='py_imgprocessor',
    name='py_imgprocessor',
    packages=find_packages(include=['py_imgprocessor', 'py_imgprocessor.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/prashantz7242/py_imgprocessor',
    version='0.1.0',
    zip_safe=False,
)
