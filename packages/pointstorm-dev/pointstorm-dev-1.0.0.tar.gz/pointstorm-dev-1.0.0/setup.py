from setuptools import setup, find_packages

version = open('VERSION').read().strip()
license = open('LICENSE').read().strip()

setup(
    name = 'pointstorm-dev',
    version = version,
    license = license,
    author = 'Tesfa Shenkute',
    author_email = 'legetesfa@gmail.com',
    url = 'https://pointstorm.io',
    description = 'Lorem ipsum dolor fiat lux',
    long_description = open('README.md').read().strip(),
    packages = find_packages(),
    install_requires=[
        # put packages here
        'six',
    ],
    test_suite = 'tests',
    entry_points = {
	    'console_scripts': [
	        'pointstorm_dev = pointstorm_dev.__main__:main',
	    ]
	}
)
