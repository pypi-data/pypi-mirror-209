# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['machineries']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'machineries',
    'version': '0.1.0',
    'description': 'Python framework for controlling machines',
    'long_description': '# Machineries\nPython framework for controlling different machines\n',
    'author': 'michael tadnir',
    'author_email': 'tadnir50@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/tadnir/machineries',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
