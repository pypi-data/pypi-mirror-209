# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyvulncheck']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pyvulncheck',
    'version': '0.1.0',
    'description': 'pyvulncheck is an open-source tool designed for detecting vulnerabilities in Python packages, drawing inspiration from the capabilities of govulncheck.',
    'long_description': '# pyvulncheck\n\npyvulncheck is an open-source tool designed for detecting vulnerabilities in Python packages, drawing inspiration from the capabilities of [govulncheck](https://pkg.go.dev/golang.org/x/vuln/cmd/govulncheck). It uses [deps.dev Open API](https://docs.deps.dev/api/v3alpha/) to detect vulnerabilities.\n',
    'author': 'Taehyun Lee',
    'author_email': '0417taehyun@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/FastAPI-Korea/pyvulncheck',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
