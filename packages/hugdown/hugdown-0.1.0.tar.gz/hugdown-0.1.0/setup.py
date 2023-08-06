# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hugdown']

package_data = \
{'': ['*']}

install_requires = \
['huggingface-hub>=0.14.1,<0.15.0',
 'psutil>=5.9.5,<6.0.0',
 'tqdm>=4.65.0,<5.0.0',
 'urllib3>=2.0.2,<3.0.0']

setup_kwargs = {
    'name': 'hugdown',
    'version': '0.1.0',
    'description': 'A HuggingFace file downloader that retries automatically.',
    'long_description': '<img src="https://imagedelivery.net/Dr98IMl5gQ9tPkFM5JRcng/2399ebc8-449a-4090-6538-6ac4b92ae700/HD" alt="Cover"/>',
    'author': 'Lingxi Li',
    'author_email': 'lilingxi01@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8',
}


setup(**setup_kwargs)
