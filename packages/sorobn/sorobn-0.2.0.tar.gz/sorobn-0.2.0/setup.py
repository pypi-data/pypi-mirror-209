# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sorobn']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.24.2,<2.0.0', 'pandas>=1.5.3,<2.0.0', 'vose>=0.1.0,<0.2.0']

entry_points = \
{'console_scripts': ['sorobn = sorobn:cli_hook']}

setup_kwargs = {
    'name': 'sorobn',
    'version': '0.2.0',
    'description': 'Bayesian networks in Python',
    'long_description': 'None',
    'author': 'Max Halford',
    'author_email': 'maxhalford25@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
