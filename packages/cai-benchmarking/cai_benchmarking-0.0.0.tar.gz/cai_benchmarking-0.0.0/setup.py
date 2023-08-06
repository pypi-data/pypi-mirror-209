# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cai_benchmarking']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'cai-benchmarking',
    'version': '0.0.0',
    'description': 'Causal AI Benchmarking Framework',
    'long_description': '# cai-benchmarking: Causal AI Benchmarking Framework\n',
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
