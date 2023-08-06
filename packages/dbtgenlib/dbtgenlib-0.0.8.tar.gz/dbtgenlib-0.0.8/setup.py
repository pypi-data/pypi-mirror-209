from setuptools import setup, find_packages
setup(
    name='dbtgenlib',
    version='0.0.8',
    packages=find_packages(),
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        dbtgenlib=dbtgengenlib.dbtgenlib:yml_gen
        ''',
)