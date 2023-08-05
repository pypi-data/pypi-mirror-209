# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cai_features']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'cai-features',
    'version': '0.0.0',
    'description': 'Causal AI Feature Engineering',
    'long_description': '# cai-features: Causal AI Feature Engineering\n',
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
