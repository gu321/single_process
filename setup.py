from setuptools import setup, find_packages

PKG_NAME = 'single_process'
PACKAGES = [PKG_NAME] + ["%s.%s" % (PKG_NAME, i)
                         for i in find_packages(PKG_NAME)]
import sys

txt = open('README.rst', 'r').read()
title = "limit python script just run a single process"

kw = dict(
    name=PKG_NAME,
    version="2.4.1",
    description=title,
    long_description=txt,
    author='zuroc',
    author_email='xpure@foxmail.com',
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
    url="https://github.com/gu321/single_process",
    packages=PACKAGES,

)

if sys.version_info[1] == 5:
    kw['install_requires'] = ['simplejson']

setup(**kw)
