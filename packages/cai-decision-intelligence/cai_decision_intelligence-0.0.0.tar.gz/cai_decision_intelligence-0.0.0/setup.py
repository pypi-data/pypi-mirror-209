# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cai_decision_intelligence']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'cai-decision-intelligence',
    'version': '0.0.0',
    'description': 'Causal AI Decision Intelligence',
    'long_description': '# cai-decision-intelligence: Causal AI Decision Intelligence\n',
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
