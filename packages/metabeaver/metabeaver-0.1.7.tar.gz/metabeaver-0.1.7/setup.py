from setuptools import setup, find_packages

setup(
    name='metabeaver',
    version='0.1.7', # Major, minor, patch
    packages=find_packages(exclude=['Testing', '*.xlsx', '*.xls']),
    install_requires=[
        'numpy',
        'pandas',
        'google-cloud-core',
        'google-cloud-bigquery',
    ],
    description='Beaverish about data.',
    author='Luke Anthony Pollen',
    author_email='luke@pollenanalytics.com',
    url='https://github.com/rainbowpusheenthe3rd/dataBeaver',
)


##### ERRATA #####

#QHFG25#DQLPMeEy

#python setup.py sdist bdist_wheel


#pip show twine
#dir /s twine.exe


#twine upload dist/*
#twine upload *

##### ERRATA #####