from setuptools import setup, find_packages
setup(
    name='dbtdocgen_rutryk',
    version='0.0.6',
    packages=find_packages(),
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        dbtdocgen=dbtdocgen_rutryk.dbtdocgen:dbtdocgen
        ''',
)