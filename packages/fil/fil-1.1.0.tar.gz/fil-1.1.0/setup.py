# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['fil']
install_requires = \
['safer>=4.6.1,<5.0.0']

setup_kwargs = {
    'name': 'fil',
    'version': '1.1.0',
    'description': '🏺 Read/write JSON/TOML/Yaml/txt 🏺',
    'long_description': "## Example 1: read a file\n\n    d1 = fil.read('file.json')   # Any Json\n    d2 = fil.read('file.toml')   # A dict\n    d3 = fil.read('file.yaml')   # Any JSON\n    d4 = fil.read('file.txt')    # A string\n\n    # Reading a JSON Line file returns an interator:\n    for record in fil.read('file.jsonl'):\n        print(record)  # A sequence of JSON\n\n## Example 2: write to a file\n\n    fil.write(d1, 'file.json')  # d1 can be any JSON\n    fil.write(d2, 'file.toml')  # d2 must be a dict\n    fil.write(d3, 'file.yaml')  # d3 can be any JSON\n    fil.write(d4, 'file.txt')   # d4 most be a str\n\n    # Write an iterator to a JSON Line file\n    dicts = ({'key': i} for i in range(10))\n    fil.write(dicts, 'file.jsonl')\n\n\n### [API Documentation](https://rec.github.io/fil#fil--api-documentation)\n",
    'author': 'Tom Ritchford',
    'author_email': 'tom@swirly.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
