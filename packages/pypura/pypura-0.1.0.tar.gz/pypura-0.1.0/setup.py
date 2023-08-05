# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pypura']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.26.135,<2.0.0', 'pycognito>=2022.12.0,<2023.0.0']

setup_kwargs = {
    'name': 'pypura',
    'version': '0.1.0',
    'description': 'Python package for interacting with Pura smart fragrance diffuser',
    'long_description': '# pypura\nPython package for interacting with Pura smart fragrance diffusers\n',
    'author': 'Nathan Spencer',
    'author_email': 'natekspencer@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8.1,<4.0.0',
}


setup(**setup_kwargs)
