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
    'version': '0.0.1',
    'description': '',
    'long_description': '# [WIP] Smuggler\n\n⚠️ This is a Work In Progress ⚠️\n\nSmuggler is a CLI that aids with the migration of Kubernetes resources between clusters.\n\n## Quickstart\n\nRequires Python 3.10 or superior:\n\n```bash\n# (Optional) create and activate a virtualenv to avoid cluttering the system environment\npython3 -m venv venv\nsource venv/bin/activate\n\n# Install Smuggler\npip install k8s-smuggler\n\n# Do a migration, make sure the namespace $NS exists in both clusters\nsmuggler migrate namespace --from "$CTX1" --to "$CTX2" --namespace "$NS"\n```\n\n## Development\n\n### Dev requirements\n\n- Python 3.10 or superior\n- [Poetry](https://python-poetry.org/docs/#installation) for dependency management tool\n\nSetup the dev environment with `poetry install`, this will create a virtualenv with all necessary dependencies installed. Make sure to point your IDE to this virtualenv to take advantage of autocompletion.\n\nSee [pyenv](https://github.com/pyenv/pyenv) if you need a Python version management tool.\n\n### Project structure\n\nThe project has a very simple structure:\n\n- **`k8s_smuggler/`**: Application source code.\n  - **`k8s_smuggler/main.py`**: Application entrypoint.\n  - **`k8s_smuggler/configuration.py`**: Application configuration file, all defaults go here and there should\'t be any configuration hardcoded anywhere else.\n  - **`k8s_smuggler/commands`**: Handlers for CLI arguments, all subcommands are registered in `entrypoint.py`.\n  - **`k8s_smuggler/actions`**: Application specific logic.\n  - **`k8s_smuggler/kubernetes`**: Kubernetes specific logic.\n  - **`k8s_smuggler/cli`**: CLI specific logic, helpers that improve UX.\n  - **`k8s_smuggler/lib`**: Generic and redistributable libraries.\n- **`dummy_service/`**: Kustomize manifests for a simple service for different Kubernetes versions, you can use these to test drive the tool.\n- **`test/`**: Tests (or lack thereof, WIP), currently only has a script that runs the linter.\n',
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
