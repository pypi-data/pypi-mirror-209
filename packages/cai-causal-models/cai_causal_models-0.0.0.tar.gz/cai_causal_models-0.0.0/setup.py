# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cai_causal_models']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'cai-causal-models',
    'version': '0.0.0',
    'description': 'Causal Models',
    'long_description': '# cai-causal-models: Causal Models\n',
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
