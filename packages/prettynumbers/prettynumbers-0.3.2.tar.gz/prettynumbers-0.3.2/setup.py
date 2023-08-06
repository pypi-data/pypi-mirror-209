# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pretty_numbers']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'prettynumbers',
    'version': '0.3.2',
    'description': 'Display a range of numbers in a human readable way',
    'long_description': '[![vfxGer](https://circleci.com/gh/vfxGer/pretty-numbers.svg?style=svg)](BUILD)\n[![codecov.io](https://codecov.io/gh/vfxGer/pretty-numbers/coverage.svg?branch=master)](https://codecov.io/gh/vfxGer/pretty-numbers)\n[![Code Climate](https://codeclimate.com/github/vfxGer/pretty-numbers/badges/gpa.svg)](https://codeclimate.com/github/vfxGer/pretty-numbers)\n[![PYPI](https://img.shields.io/pypi/v/prettynumbers.svg)](https://pypi.python.org/pypi/prettynumbers)\n\n# Pretty Numbers\n\nPretty Numbers is a simple Python package that displays long series of numbers in a more human readable way.\n\nI have used it for displaying frames of a render in a more human readable way or issues of comic books. It allows the user to quickly see what is included and what is missing.\n\n## Installation\n\nIt is available on [PyPi](https://pypi.python.org/pypi/prettynumbers) meaning you can just:\n\n    pip install prettynumbers\n\n## Usage\n\n```python\nimport pretty_numbers\npretty_numbers.getPrettyTextFromNumbers([1001, 99, 1004, 1005, 1003, 1008,\n                                         1002, 1007, 1010, 1006, 1111, 1009])\n```\n\nReturns:\n\n    "99,1001-1010,1111"\n',
    'author': 'gerardk',
    'author_email': 'gerardk@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/vfxGer/pretty-numbers',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8.0,<4.0.0',
}


setup(**setup_kwargs)
