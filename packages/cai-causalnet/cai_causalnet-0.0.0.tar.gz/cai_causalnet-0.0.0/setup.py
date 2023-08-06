# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cai_causalnet']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'cai-causalnet',
    'version': '0.0.0',
    'description': 'CausalNet: Structural Causal Model (SCM)',
    'long_description': '# cai-causalnet: CausalNet Structural Causal Model (SCM)\n',
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
