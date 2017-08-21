from setuptools import setup

import sys

txt = open('README.rst', 'r').read()
title = txt.split("\n")[0]

kw = dict(
    name='single_process',
    version="2.1",
    description=title,
    long_description=txt,
    author='zsp',
    author_email='xpure@foxmail.com',
    py_modules=['single_process'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    url="https://github.com/gu321/single_process"
)

if sys.version_info[1] == 5:
    kw['install_requires'] = ['simplejson']

setup(**kw)
