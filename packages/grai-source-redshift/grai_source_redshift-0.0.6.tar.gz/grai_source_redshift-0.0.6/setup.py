# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['grai_source_redshift']

package_data = \
{'': ['*']}

install_requires = \
['grai-client>=0.2.4,<0.3.0',
 'grai-schemas>=0.1.5,<0.2.0',
 'multimethod>=1.8,<2.0',
 'pydantic[dotenv]>=1.10.7,<2.0.0',
 'redshift-connector>=2.0.910,<3.0.0']

setup_kwargs = {
    'name': 'grai-source-redshift',
    'version': '0.0.6',
    'description': '',
    'long_description': '# Grai Redshift Integration\n\nThe Redshift integration synchronizes metadata from a Redshift datawarehouse into your Grai data lineage graph.\n',
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
