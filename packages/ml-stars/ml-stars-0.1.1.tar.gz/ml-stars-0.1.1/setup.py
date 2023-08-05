#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md', encoding='utf-8') as history_file:
    history = history_file.read()

install_requires = [
    'Keras>=2.4,<2.5',
    'mlblocks>=0.4,<0.6',
    'numpy<1.21.0,>=1.16.0',
    'pandas>=1,<2',
    'scikit-learn>=0.21,<1.2',
    'scipy>=1.1.0,<2',
    'statsmodels>=0.9.0,<0.13',
    'tensorflow>=2,<2.5',
    'xgboost>=0.72.1,<1',

    # fix google/protobuf/descriptor
    'protobuf<4',
]

setup_requires = [
    'pytest-runner>=2.11.1',
]

tests_require = [
    'pytest>=3.4.2',
    'pytest-cov>=2.6.0',
    'rundoc>=0.4.3,<0.5',
]

development_requires = [
    # general
    'bumpversion>=0.5.3,<0.6',
    'pip>=9.0.1',
    'watchdog>=0.8.3,<0.11',

    # docs
    'docutils>=0.12,<0.18',
    'm2r2>=0.2.5,<0.3',
    'nbsphinx>=0.5.0,<0.7',
    'Sphinx>=3,<3.3',
    'pydata-sphinx-theme<0.5',
    'autodocsumm>=0.1.10,<1',
    'markupsafe<2.1.0',
    'ipython>=6.5,<7.5',
    'mistune>=0.7,<2',
    'Jinja2>=2,<3',
    
    # style check
    'flake8>=3.7.7,<4',
    'isort>=4.3.4,<5',

    # fix style issues
    'autoflake>=1.2',
    'autopep8>=1.4.3',
    'importlib-metadata<5',

    # distribute on PyPI
    'twine>=1.10.0',
    'wheel>=0.30.0',

    # Advanced testing
    'coverage>=4.5.1',
    'tox>=2.9.1',
]

setup(
    author='MIT Data To AI Lab',
    author_email='dailabmit@gmail.com',
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
    description='Primitives and Pipelines for Time Series Data.',
    entry_points={
        'mlblocks': [
            'primitives=mlstars:MLBLOCKS_PRIMITIVES',
            'pipelines=mlstars:MLBLOCKS_PIPELINES'
        ],
    },
    extras_require={
        'test': tests_require,
        'dev': development_requires + tests_require,
    },
    install_package_data=True,
    install_requires=install_requires,
    license='MIT license',
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='mlstars',
    name='ml-stars',
    packages=find_packages(include=['mlstars', 'mlstars.*']),
    python_requires='>=3.6,<3.9',
    setup_requires=setup_requires,
    test_suite='tests',
    tests_require=tests_require,
    url='https://github.com/sintel-dev/ml-stars',
    version='0.1.1',
    zip_safe=False,
)
