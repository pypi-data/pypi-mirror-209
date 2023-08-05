# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['grai_source_postgres']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'grai-client>=0.2.4,<0.3.0',
 'grai-schemas>=0.1.5,<0.2.0',
 'multimethod>=1.8,<2.0',
 'psycopg2>=2.9.5,<3.0.0',
 'pydantic>=1.9.1,<2.0.0']

setup_kwargs = {
    'name': 'grai-source-postgres',
    'version': '0.1.19',
    'description': '',
    'long_description': '# Grai Postgres Integration\n\nThe Postgres integration synchronizes metadata from your Postgres database into your Grai data lineage graph.\n',
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
