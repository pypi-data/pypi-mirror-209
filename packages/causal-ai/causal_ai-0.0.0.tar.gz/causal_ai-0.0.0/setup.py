# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['causal_ai']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'causal-ai',
    'version': '0.0.0',
    'description': 'Causal AI',
    'long_description': '# causal-ai: Causal AI\n',
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
