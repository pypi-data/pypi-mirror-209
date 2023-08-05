# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['grai_source_mysql']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'grai-client>=0.2.6,<0.3.0',
 'grai-schemas>=0.1.11,<0.2.0',
 'multimethod>=1.8,<2.0',
 'mysql-connector-python>=8.0.31,<9.0.0',
 'pydantic>=1.9.1,<2.0.0']

setup_kwargs = {
    'name': 'grai-source-mysql',
    'version': '0.0.14',
    'description': '',
    'long_description': '# Grai MySQL Integration\n\nThe MySQL integration synchronizes metadata from your MySQL database into your Grai data lineage graph.\n',
    'author': 'Ian Eaves',
    'author_email': 'ian@grai.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://www.grai.io/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
