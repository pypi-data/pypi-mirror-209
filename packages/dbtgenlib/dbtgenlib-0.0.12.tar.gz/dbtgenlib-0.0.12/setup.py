from setuptools import setup, find_packages
setup(
    name='dbtgenlib',
    version='0.0.12',
    packages=find_packages(),
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        yml_gen=dbtgenlib.yml_gen:dbtdocgen
        ''',
)