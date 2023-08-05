#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['pandas', 'matplotlib', 'seaborn', 'scikit-learn']

test_requirements = ['pytest>=3',]

setup(
    author="Margarita Harutyunyan",
    author_email='maga220103@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="A python package for customer segmentation",
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    long_description_content_type ='text/markdown',
    include_package_data=True,
    keywords='mycustomersegmentation',
    name='mycustomersegmentation',
    packages=find_packages(include=['mycustomersegmentation', 'mycustomersegmentation.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/Margarita220103/mycustomersegmentation',
    version='0.1.0',
    zip_safe=False,
)
