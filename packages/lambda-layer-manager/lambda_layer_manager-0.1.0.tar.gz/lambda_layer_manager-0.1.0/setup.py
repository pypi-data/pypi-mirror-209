# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['src', 'src.managers', 'src.models']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.26.98,<2.0.0', 'pydantic>=1.10.7,<2.0.0', 'typer>=0.9.0,<0.10.0']

entry_points = \
{'console_scripts': ['llm = src.main:app']}

setup_kwargs = {
    'name': 'lambda-layer-manager',
    'version': '0.1.0',
    'description': 'Automatic Lambda Layer Manager',
    'long_description': '# Lambda Layer Manager\n\n[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)\n[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v1.json)](https://github.com/charliermarsh/ruff)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)\n[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat-square&labelColor=ef8336)](https://pycqa.github.io/isort/)\n\n## Overview\n\nAutomatically build and deploy AWS Lambda layer.\n\n**Config:**\n```json\n{\n  "layers": [\n    {\n      "name": "<name_of_the_layer>",\n      "requirements": "<path_to_requirements_file>",\n      "config": {\n        "description": "<description>",\n        "compatible_runtimes": ["<python3.10>"],\n        "compatible_architectures": ["<x86_64>"]\n      }\n    }\n  ]\n}\n```\n\nAn example configuration can be found in the `./example` directory.\n\n## Quickstart\n\nRun the *Lambda Layer Manager* (*llm*) with the following command:\n```bash\nllm <path/to/config_file>\n```\n\n## Contribution\n\nInstall the dependencies:\n```bash\npoetry install\n```\n\nEnable the *pre-commit* hooks:\n```bash\npre-commit install\n```\n\n## License\n\nThis project is licensed under the MIT license.\n',
    'author': 'MMartin09',
    'author_email': 'mmartin09@outlook.at',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/MMartin09/lambda_layer',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
