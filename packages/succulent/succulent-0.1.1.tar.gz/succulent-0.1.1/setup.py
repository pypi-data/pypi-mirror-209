# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['succulent']

package_data = \
{'': ['*']}

install_requires = \
['flask>=2.3.2,<3.0.0', 'pandas>=2.0.1,<3.0.0', 'pyyaml>=6.0,<7.0']

setup_kwargs = {
    'name': 'succulent',
    'version': '0.1.1',
    'description': 'Collect POST requests easily',
    'long_description': '---\n\n# succulent - Collect POST requests easily\n\n---\n![PyPI Version](https://img.shields.io/pypi/v/succulent.svg)\n![PyPI - Downloads](https://img.shields.io/pypi/dm/succulent.svg)\n[![Downloads](https://pepy.tech/badge/succulent)](https://pepy.tech/project/succulent)\n![GitHub repo size](https://img.shields.io/github/repo-size/firefly-cpp/succulent?style=flat-square)\n[![GitHub license](https://img.shields.io/github/license/firefly-cpp/succulent.svg)](https://github.com/firefly-cpp/succulent/blob/master/LICENSE)\n![GitHub commit activity](https://img.shields.io/github/commit-activity/w/firefly-cpp/succulent.svg)\n[![Average time to resolve an issue](http://isitmaintained.com/badge/resolution/firefly-cpp/succulent.svg)](http://isitmaintained.com/project/firefly-cpp/succulent "Average time to resolve an issue")\n[![Percentage of issues still open](http://isitmaintained.com/badge/open/firefly-cpp/succulent.svg)](http://isitmaintained.com/project/firefly-cpp/succulent "Percentage of issues still open")\n\n## About\n\nsucculent is a pure Python framework that simplifies the configuration, management, collection, and preprocessing of data collected via POST requests. The inspiration for the framework comes from the practical data collection challenges in smart agriculture. The main idea of the framework was to speed up the process of configuring different collected parameters and providing several useful functions for data transformations.\n\n## Detailed insights\nThe current version includes (but is not limited to) the following functions:\n\n- Request URL generation for data collection\n- Data collection from POST requests\n\n## Installation\n\n### pip\n\nInstall succulent with pip:\n\n```sh\npip install succulent\n```\n\n## Usage\n\n### Example\n\n```python\nfrom succulent.api import SucculentAPI\napi = SucculentAPI(host=\'0.0.0.0\', port=8080, config=\'configuration.yml\', format=\'csv\')\napi.start()\n```\n\n## Configuration\nIn the root directory, create a file named `configuration.yml` and define the following:\n```yml\ndata:\n  - name: # Measure name\n```\n\n## License\n\nThis package is distributed under the MIT License. This license can be found online at <http://www.opensource.org/licenses/MIT>.\n\n## Disclaimer\n\nThis framework is provided as-is, and there are no guarantees that it fits your purposes or that it is bug-free. Use it at your own risk!\n',
    'author': 'Iztok Fister Jr.',
    'author_email': 'iztok@iztok-jr-fister.eu',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/firefly-cpp/succulent',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
