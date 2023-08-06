# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mosek_license']

package_data = \
{'': ['*']}

install_requires = \
['urllib3']

setup_kwargs = {
    'name': 'mosek-license-server',
    'version': '0.0.7',
    'description': 'Expose a mosek license via a nginx server',
    'long_description': "# Mosek License Server\n\nUsing a [nginx image](https://hub.docker.com/_/nginx/) we expose a Mosek license\non a server to be accessible from various research machines without sharing the actual\nlicense file in the underlying repositories.\n\nThis repository serves two purposes. It exposes the server but it is also the home\nfor a little Python package to inject the license into your programs.\n\n## License server\n\n### Copy your license file into folder \n\nCopy the license file you have received (from Mosek) into the license folder.\nName it `mosek'.\n\n\n### Start the nginx server\n\nShare the license folder (after you have copied your personal Mosek license into)\nvia\n\n```bash\ndocker run --name mosek -v $PWD/license:/usr/share/nginx/html:ro -p 8080:80 -d nginx\n```\n\nThe license will now be exposed via http://localhost:8080\n\nAs an alternative you can run the script\n\n```bash\n./license_server.sh\n```\n\n## The mosek_license module\n\nInstall via\n\n```bash\npip install mosek-license-server\n```\nand then\n\n```python\nfrom mosek_license import license\n\n# It's important to upsert the license before you import mosek\nlicense.upsert()\n\n# only now import mosek\nimport mosek\n```\n\n",
    'author': 'Thomas Schmelzer',
    'author_email': 'thomas.schmelzer@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9',
}


setup(**setup_kwargs)
