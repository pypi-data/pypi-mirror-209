# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['imap_structure']

package_data = \
{'': ['*']}

install_requires = \
['pyparsing>=3.0.9,<4.0.0']

setup_kwargs = {
    'name': 'imap-structure',
    'version': '0.1.5',
    'description': 'IMAP BODYSTRUCTURE parser',
    'long_description': '# imap-structure\n\nIMAP BODYSTRUCTURE parser\n',
    'author': 'Kiruya Momochi',
    'author_email': '65301509+kiruyamomochi@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
