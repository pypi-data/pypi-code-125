# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['toolchest_client',
 'toolchest_client.api',
 'toolchest_client.files',
 'toolchest_client.files.tests',
 'toolchest_client.tools',
 'toolchest_client.tools.tests']

package_data = \
{'': ['*'], 'toolchest_client.files.tests': ['data/*', 'data/paired_end/*']}

install_requires = \
['boto3>=1.18.29,<2.0.0',
 'python-dotenv>=0.18.0,<0.19.0',
 'requests>=2.25.1,<3.0.0',
 'sentry-sdk>=1.5.8,<2.0.0']

extras_require = \
{':python_version < "3.8"': ['importlib-metadata>=1.0,<2.0']}

setup_kwargs = {
    'name': 'toolchest-client',
    'version': '0.9.14',
    'description': 'Python client for Toolchest',
    'long_description': '# Toolchest Python Client\n\n**Toolchest** runs computational biology software in the cloud with just a few lines of code. \nYou can call Toolchest from anywhere Python or R runs, using input files located on your computer or S3.\n\nThis package contains the **Python** client for using Toolchest.\nFor the **R** client, [see here](https://github.com/trytoolchest/toolchest-client-r).\n\n## [Documentation & User Guide](https://docs.trytoolchest.com/)\n\n## Installation\n\nThe Toolchest client is available [on PyPI](https://pypi.org/project/toolchest-client):\n``` shell\npip install toolchest-client\n```\n\n## Usage\n\nUsing a tool in Toolchest is as simple as:\n\n``` python\nimport toolchest_client as toolchest\ntoolchest.set_key("YOUR_TOOLCHEST_KEY")\ntoolchest.kraken2(\n  tool_args="",\n  inputs="path/to/input.fastq",\n  output_path="path/to/output.fastq",\n)\n```\n\nFor a list of available tools, see the [documentation](https://docs.trytoolchest.com/docs#-tools).\n\n## Configuration\n\nTo use Toolchest, you must have an authentication key stored\nin the `TOOLCHEST_KEY` environment variable.\n\n``` python\nimport toolchest_client as toolchest\ntoolchest.set_key("YOUR_TOOLCHEST_KEY") # or a file path containing the key\n```\n\nContact Toolchest if:\n\n-   you need a key\n-   you’ve forgotten your key\n-   the key is producing authentication errors.\n',
    'author': 'Bryce Cai',
    'author_email': 'bcai@trytoolchest.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/trytoolchest/toolchest-client-python',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
