# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['nspyre',
 'nspyre.cli',
 'nspyre.data',
 'nspyre.data.streaming',
 'nspyre.extras',
 'nspyre.gui',
 'nspyre.gui.style',
 'nspyre.gui.widgets',
 'nspyre.instrument',
 'nspyre.misc']

package_data = \
{'': ['*'], 'nspyre.gui': ['images/*']}

install_requires = \
['numpy>=1.23,<2.0',
 'pyqt6>=6.2.3,<7.0.0',
 'pyqtgraph>=0.13.1,<0.14.0',
 'rpyc>=5.2.3,<6.0.0']

extras_require = \
{'dev': ['pre-commit',
         'sphinx',
         'sphinx-copybutton',
         'sphinx_rtd_theme',
         'sphinx-autoapi',
         'pytest',
         'pytest-cov',
         'pint',
         'poetry2setup']}

entry_points = \
{'console_scripts': ['nspyre-dataserv = nspyre.cli.dataserv:_main',
                     'nspyre-inserv = nspyre.cli.inserv:_main']}

setup_kwargs = {
    'name': 'nspyre',
    'version': '0.6.0.1',
    'description': 'Networked Scientific Python Research Environment.',
    'long_description': '# nspyre\n\n[![GitHub](https://img.shields.io/github/v/release/nspyre-org/nspyre?label=GitHub)](https://github.com/nspyre-org/nspyre/)\n[![PyPi version](https://img.shields.io/pypi/v/nspyre)](https://pypi.org/project/nspyre/)\n[![conda-forge version](https://img.shields.io/conda/v/conda-forge/nspyre)](https://github.com/conda-forge/nspyre-feedstock)\n[![License](https://img.shields.io/github/license/nspyre-org/nspyre)](https://github.com/nspyre-org/nspyre/blob/master/LICENSE)\n[![Docs build](https://readthedocs.org/projects/nspyre/badge/?version=latest)](https://nspyre.readthedocs.io/en/latest/?badge=latest)\n[![conda-forge platform](https://img.shields.io/conda/pn/conda-forge/nspyre)](https://github.com/conda-forge/nspyre-feedstock)\n[![DOI](https://zenodo.org/badge/220515183.svg)](https://zenodo.org/badge/latestdoi/220515183)\n\n(N)etworked (S)cientific (Py)thon (R)esearch (E)nvironment.\n\nSee https://nspyre.readthedocs.io/.\n\n# What is nspyre?\n\nnspyre is a Python package for conducting scientific experiments. It provides \na set of tools to allow for control of instrumentation, data collection, \nreal-time plotting, as well as GUI generation. Anyone in the research or \nindustrial spaces using computer-controlled equipment and collecting data can \npotentially benefit from using nspyre to run their experiments.\n\nThe hardware being controlled can be connected either locally on the machine \nrunning the experimental logic, or on a remote machine, which can be accessed \nin a simple, pythonic fashion. This allows for the easy integration of shared \ninstrumentation in a research environment. Data collection is also \nnetworked, and allows for real-time viewing locally, or from a remote machine. \nnspyre provides a set of tools for quickly generating a Qt-based GUI for \ncontrol and data viewing.\n\nIf you use nspyre for an experiment, we would really appreciate it if you \n[cite](https://doi.org/10.5281/zenodo.7315077) it in your publication!\n',
    'author': 'Jacob Feder',
    'author_email': 'jacobsfeder@gmail.com',
    'maintainer': 'Jacob Feder',
    'maintainer_email': 'jacobsfeder@gmail.com',
    'url': 'https://github.com/nspyre-org/nspyre',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
