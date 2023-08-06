# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mosek_license']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'mosek-license-server',
    'version': '0.0.5',
    'description': 'Expose a mosek license via a nginx server',
    'long_description': "# Mosek License Server\n\nUsing the [nginx image](https://hub.docker.com/_/nginx/) we expose a Mosek license\non a server to be accessible from various research machines without sharing the actual\nlicense file in the underlying repos.\n\n## Usage\n\n### Copy your license file into folder \n\nCopy the license file you have received (from Mosek) into the licenses folder.\nName is ```mosek'''\n\n### Start the nginx server\n\nShare the licenses folder (after you have copied your personal Mosek license into)\nvia\n\n```bash\ndocker run --name mosek -v $PWD/licenses:/usr/share/nginx/html:ro -p 8080:80 -d nginx\n```\n\nThe license will now be exposed via http://localhost:8080\n\nAs an alternative you can run the script\n\n```bash\n./license_server.sh\n```\n",
    'author': 'Thomas Schmelzer',
    'author_email': 'thomas.schmelzer@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9',
}


setup(**setup_kwargs)
