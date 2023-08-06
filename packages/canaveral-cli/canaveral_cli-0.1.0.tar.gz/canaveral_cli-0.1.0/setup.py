# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['canaveral_cli']

package_data = \
{'': ['*'],
 'canaveral_cli': ['oam_types/component/*',
                   'oam_types/policy/*',
                   'oam_types/trait/*',
                   'oam_types/workflowstep/*',
                   'templates/*']}

install_requires = \
['Jinja2>=3.1.2,<4.0.0',
 'PyGithub>=1.58.2,<2.0.0',
 'PyYAML>=6.0,<7.0',
 'inquirerpy>=0.3.4,<0.4.0',
 'python-dotenv>=1.0.0,<2.0.0',
 'rich>=13.3.5,<14.0.0',
 'typer[all]>=0.9.0,<0.10.0']

entry_points = \
{'console_scripts': ['canaveral = canaveral.cli:app']}

setup_kwargs = {
    'name': 'canaveral-cli',
    'version': '0.1.0',
    'description': "Helper CLI to interact with Devscope's internal platform codename Canaveral",
    'long_description': None,
    'author': 'André Gomes',
    'author_email': 'andre.gomes@devscope.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
