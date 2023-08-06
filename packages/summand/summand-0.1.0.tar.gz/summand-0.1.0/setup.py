# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['summand']

package_data = \
{'': ['*']}

install_requires = \
['tinydb>=4.7.1,<5.0.0', 'typer[all]>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['summand = summand.cli:app']}

setup_kwargs = {
    'name': 'summand',
    'version': '0.1.0',
    'description': '',
    'long_description': '# Summand\n\n### **list of commands and options**\n\n**Summand add** \\[\\<summand\\>\\] [--description | -D] [--command | -C] [--split]\n\n**Summand edit** [--list-name] [--list-description] [--list-commands]\n\n**Summand export** \\[\\<summands\\>\\] \\[\\<file name\\>\\] [--list | -L] [--all | -A] [--filename*] [--split | -S] [--exclude | -E] \n\n**Summand help** \\[\\<summand\\>\\] [--number | -N]\n\n**Summand import** \\[\\<directory\\>\\] [--ignore | -I] [--show]\n\n**Summand list** \\[\\<summand\\>\\] [--number | -N] [--description | -D]\n\n**Summand remove** \\[\\<query\\>\\] [--description | -D] [--command | -C] [--split] / Should be same as add\n\n**Summand reset**\n\n**Summand run** \\[\\<summand\\>\\]\n',
    'author': 'Alireza',
    'author_email': 'alirezaaraby5@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
