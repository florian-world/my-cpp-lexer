#!/usr/bin/python

from setuptools import setup, find_packages

setup(
    name='pygments-mycpp',
    version='0.2',
    description='Pygments lexer for Custom CPP.',
    long_description=open('README.md').read(),
    keywords='pygments cpp custom lexer',
    license='BSD',

    author='Florian Mahlknecht',
    author_email='m@florian.world',

    url='https://github.com/florian-world/my-cpp-lexer',

    packages=find_packages(),
    install_requires=['pygments >= 1.4'],

    entry_points='''[pygments.lexers]
                    mycpp=pygments_mycpp:MyCppLexer''',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)