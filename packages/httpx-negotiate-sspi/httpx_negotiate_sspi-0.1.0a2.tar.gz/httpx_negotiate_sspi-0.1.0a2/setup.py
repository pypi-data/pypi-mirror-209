# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['httpx_negotiate_sspi']

package_data = \
{'': ['*']}

install_requires = \
['httpx>0.16,<0.25', 'pypiwin32>=223,<224']

setup_kwargs = {
    'name': 'httpx-negotiate-sspi',
    'version': '0.1.0a2',
    'description': 'SSPI authentication for httpx',
    'long_description': '# httpx-negotiate-sspi\n\nAn implementation of HTTP Negotiate authentication for httpx. This module provides single-sign-on using Kerberos or NTLM using the Windows SSPI interface.\n\nThis module supports Extended Protection for Authentication (aka Channel Binding Hash), which makes it usable for services that require it, including Active Directory Federation Services.\n\n',
    'author': 'Rob Blackbourn',
    'author_email': 'rob.blackbourn@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/rob-blackbourn/httpx-negotiate-sspi',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
