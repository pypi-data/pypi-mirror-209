# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cai_data']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'cai-data',
    'version': '0.0.0',
    'description': 'A data engineering package for Causal AI.',
    'long_description': '# cai-data: Causal AI Data Types, Pipelines, and Engineering\n',
    'author': 'causaLens',
    'author_email': 'opensource@causalens.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
