from setuptools import setup

setup(
    name='django-trackmodels-xls-ritual',
    version='1.1.2',
    packages=['grimoire.django.tracked_xls'],
    url='https://github.com/luismasuelli/django-trackmodels-xls-ritual',
    license='LGPL',
    author='Luis y Anita',
    author_email='luismasuelli@hotmail.com',
    description='XLSX report plugin for django-trackmodels-ritual',
    install_requires=['Django>=4.0', 'XlsxWriter>=0.8.7', 'django-trackmodels-ritual>=1.1.2']
)