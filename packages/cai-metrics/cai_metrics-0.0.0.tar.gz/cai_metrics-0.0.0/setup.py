# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cai_metrics']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'cai-metrics',
    'version': '0.0.0',
    'description': 'Metrics for Causal AI',
    'long_description': '# cai-metrics: Causal AI Metrics\n',
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
