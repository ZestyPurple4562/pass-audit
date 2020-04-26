#!/usr/bin/env python3
# pass audit - Password Store Extension (https://www.passwordstore.org/)
# Copyright (C) 2017-2020 Alexandre PUJOL <alexandre@pujol.io>.

import os
from setuptools import setup

about = dict()
with open(os.path.join('pass_audit', '__init__.py')) as file:
    exec(file.read(), about)  # nosec pylint: disable=exec-used

with open('README.md') as file:
    long_description = file.read()


setup(
    name=about['__title__'],
    version=about['__version__'],
    author=about['__author__'],
    author_email=about['__email__'],
    description=about['__summary__'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    license=about['__license__'],
    url=about['__uri__'],
    packages=['pass_audit'],
    install_requires=[
        'requests',
        'zxcvbn'
    ],
    python_requires='>=3.5',
    zip_safe=True,
    keywords=[
        'password-store', 'password', 'pass', 'pass-extension',
        'audit', 'password-audit', 'haveibeenpwned',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General'
        ' Public License v3 or later (GPLv3+)',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Security :: Cryptography',
    ],
)
