# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cai_causal_impact']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'cai-causal-impact',
    'version': '0.0.0',
    'description': 'A package to estimate causal impacts of interventions in time-series.',
    'long_description': '# cai-causal-impact: Causal Impact Estimation\n',
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
