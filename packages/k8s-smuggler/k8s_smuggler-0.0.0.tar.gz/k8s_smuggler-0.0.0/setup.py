# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['k8s_smuggler',
 'k8s_smuggler.actions',
 'k8s_smuggler.cli',
 'k8s_smuggler.commands',
 'k8s_smuggler.kubernetes',
 'k8s_smuggler.lib']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0', 'kubernetes>=23,<24']

entry_points = \
{'console_scripts': ['smuggler = k8s_smuggler.main:main']}

setup_kwargs = {
    'name': 'k8s-smuggler',
    'version': '0.0.0',
    'description': '',
    'long_description': '# Kubernetes Smuggler\n\nKubernetes Smuggler is a CLI that aids with the migration of Kubernetes resources between clusters.\n\nRequires Python 3.10 or superior.\n',
    'author': 'DiegoPomares',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
