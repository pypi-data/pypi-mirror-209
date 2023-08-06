# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sftp_uploader',
 'sftp_uploader.docs',
 'sftp_uploader.src',
 'sftp_uploader.tests']

package_data = \
{'': ['*']}

install_requires = \
['gitpython>=3.1.31,<4.0.0', 'paramiko>=3.1.0,<4.0.0']

setup_kwargs = {
    'name': 'sftp-uploader',
    'version': '0.1.0',
    'description': 'Script for upload files to sftp',
    'long_description': '# TODO\n\n[ ] Make title, description, which problem is solve, metter of this project description\n[ ] Add more [classifiers](https://pypi.org/classifiers/)\n[ ] Add tests\n[ ] Add additional links to project conf\n',
    'author': 'Moonvent',
    'author_email': 'moonvent@proton.me',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
