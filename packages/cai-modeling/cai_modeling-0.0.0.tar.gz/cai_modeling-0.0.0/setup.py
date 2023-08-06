# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cai_modeling']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'cai-modeling',
    'version': '0.0.0',
    'description': 'Causal AI Modeling',
    'long_description': '# cai-modeling: Causal AI Modeling\n',
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
