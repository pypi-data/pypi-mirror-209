# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ontolol']

package_data = \
{'': ['*'], 'ontolol': ['templates/*']}

install_requires = \
['jinja2>=3.1.2,<4.0.0',
 'owlready2>=0.41,<0.42',
 'rdflib>=6.3.2,<7.0.0',
 'typer[all]>=0.9.0,<0.10.0']

entry_points = \
{'console_scripts': ['ontolol = ontolol.cli:app']}

setup_kwargs = {
    'name': 'ontolol',
    'version': '0.1.0',
    'description': 'Publish repositories of OWL ontologies as website',
    'long_description': '# Ontolol - Publish repositories of OWL ontologies as website\n\nOntolol is a "static site generator" for publishing OWL ontologies as\nfully customisable documentation websites, together with their\nmachine-readable (RDF) definitions.\n',
    'author': 'Dominik George',
    'author_email': 'nik@naturalnet.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://codeberg.org/Chocorize/ontolol',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
