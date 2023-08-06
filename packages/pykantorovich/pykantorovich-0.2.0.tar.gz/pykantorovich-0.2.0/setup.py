# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pykantorovich']

package_data = \
{'': ['*']}

install_requires = \
['cvxpy>=1.1.17,<2.0.0',
 'numpy>=1.21.2,<2.0.0',
 'pycddlib>=2.1.4,<3.0.0',
 'scipy>=1.7.1,<2.0.0']

extras_require = \
{'docs': ['sphinx>=5.3.0,<6.0.0',
          'sphinx-rtd-theme>=1.1.1,<2.0.0',
          'sphinxcontrib-napoleon>=0.7,<0.8',
          'sphinxcontrib-restbuilder>=0.3,<0.4']}

setup_kwargs = {
    'name': 'pykantorovich',
    'version': '0.2.0',
    'description': 'Kantorovich distance between probabilities on a finite space.',
    'long_description': '# PyKantorovich\n\n<!-- badges: start -->\n[![Documentation status](https://readthedocs.org/projects/pykantorovich/badge/)](http://pykantorovich.readthedocs.io)\n<!-- badges: end -->\n\nKantorovich distance with Python.\n\n___\n\n```\npip install pykantorovich\n```\n',
    'author': 'Stéphane Laurent',
    'author_email': 'laurent_step@outlook.fr',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/stla/PyKantorovich',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7.1,<3.10',
}


setup(**setup_kwargs)
