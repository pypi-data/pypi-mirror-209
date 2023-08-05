# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['osconfiglib']

package_data = \
{'': ['*']}

install_requires = \
['toml>=0.10.2,<0.11.0']

setup_kwargs = {
    'name': 'osconfiglib',
    'version': '0.1.4',
    'description': 'Library for image configuration',
    'long_description': None,
    'author': 'Brandon Geraci',
    'author_email': 'brandon.geraci@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
