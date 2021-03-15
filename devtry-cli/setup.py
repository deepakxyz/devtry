from setuptools import setup
setup(
    name = 'devtry-cli',
    version = '0.1.0',
    packages = ['tx'],
    entry_points = {
        'console_scripts': [
            'tx= tx.__main__:main',
        ]
    })