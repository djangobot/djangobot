import os
import sys
from setuptools import find_packages, setup
from djangobot import __version__

# README.md is long description
readme = os.path.join(os.path.dirname(__file__), 'README.md')

setup(
    name='djangobot',
    version=__version__,
    url='https://github.com/djangobot/djangobot',
    author='Scott Burns',
    author_email='scott.s.burns@gmail.com',
    description='Bridge between Slack and Channels-based Django apps',
    long_description=open(readme).read(),
    license='MIT',
    zip_safe=False,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'twisted>=16.0.0',
        'channels>=0.10.3',
        'pyopenssl>=16.0.0',
        'autobahn>=0.13.0',
        'requests>=2.3.1',
    ],
    entry_points={'console_scripts': [
        'djangobot = djangobot.cli:CLI.entry',
    ]},
)

