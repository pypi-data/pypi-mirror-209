#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from gitea_backup import __version__

try:
    from setuptools import setup
    setup  # workaround for pyflakes issue #13
except ImportError:
    from distutils.core import setup

# Hack to prevent stupid TypeError: 'NoneType' object is not callable error on
# exit of python setup.py test # in multiprocessing/util.py _exit_function when
# running python setup.py test (see
# http://www.eby-sarna.com/pipermail/peak/2010-May/003357.html)
try:
    import multiprocessing
    multiprocessing
except ImportError:
    pass


def open_file(fname):
    return open(os.path.join(os.path.dirname(__file__), fname))


setup(
    name='gitea-backup',
    version=__version__,
    author='simplebackups',
    author_email='simplebackups.io@gmail.com',
    packages=['gitea_backup'],
    scripts=['bin/gitea-backup'],
    url='http://github.com/simplebackups/python-gitea-backup',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Topic :: System :: Archiving :: Backup',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description='backup a gitea user or organization',
    long_description=open_file('README.rst').read(),
    long_description_content_type='text/x-rst',
    install_requires=open_file('requirements.txt').readlines(),
    zip_safe=True,
    
)
