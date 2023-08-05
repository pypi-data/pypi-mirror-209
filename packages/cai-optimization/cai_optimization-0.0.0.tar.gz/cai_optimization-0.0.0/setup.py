# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cai_optimization']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'cai-optimization',
    'version': '0.0.0',
    'description': 'Causal AI Optimization',
    'long_description': '# cai-optimization: Causal AI Optimization\n',
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
