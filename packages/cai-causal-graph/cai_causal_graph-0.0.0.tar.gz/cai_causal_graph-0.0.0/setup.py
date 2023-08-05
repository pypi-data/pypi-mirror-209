# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cai_causal_graph']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'cai-causal-graph',
    'version': '0.0.0',
    'description': 'A causal graph package.',
    'long_description': '# causal-graph: Causal Graph\n\n',
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
