# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cai_causal_discovery']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'cai-causal-discovery',
    'version': '0.0.0',
    'description': 'Causal discovery package focusing on full graph causal discovery for observational data with support for latent variables and the incorporation of domain/background knowledge.',
    'long_description': '# cai-causal-discovery: Causal Discovery Algorithms\n',
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
