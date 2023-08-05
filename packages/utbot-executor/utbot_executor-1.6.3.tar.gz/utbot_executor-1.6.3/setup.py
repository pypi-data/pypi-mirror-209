# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['utbot_executor', 'utbot_executor.deep_serialization']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['utbot-executor = utbot_executor:utbot_executor']}

setup_kwargs = {
    'name': 'utbot-executor',
    'version': '1.6.3',
    'description': '',
    'long_description': '# UtBot Executor\n\nUtil for python code execution and state serialization.\n\n## Installation\n\nYou can install module from [PyPI](https://pypi.org/project/utbot-executor/):\n\n```bash\npython -m pip install utbot-executor\n```\n\n## Usage\n\n### From console with socket listener\n\nRun with your `<hostname>` and `<port>` for socket connection\n```bash\n$ python -m utbot_executor <hostname> <port> <logfile> [<loglevel DEBUG | INFO | ERROR>] <coverage_hostname> <coverage_port>\n```\n\n### Request format\n```json\n{\n  "functionName": "f",\n  "functionModule": "my_module.submod1",\n  "imports": ["sys", "math", "json"],\n  "syspaths": ["/home/user/my_project/"],\n  "argumentsIds": ["1", "2"],\n  "kwargumentsIds": ["4", "5"],\n  "serializedMemory": "string",\n  "filepath": ["/home/user/my_project/my_module/submod1.py"],\n  "coverageId": "1"\n}\n```\n\n* `functionName` - name of the tested function\n* `functionModule` - name of the module of the tested function\n* `imports` - all modules which need to run function with current arguments\n* `syspaths` - all syspaths which need to import modules (usually it is a project root)\n* `argumentsIds` - list of argument\'s ids\n* `kwargumentsIds` - list of keyword argument\'s ids\n* `serializedMemory` - serialized memory throw `deep_serialization` algorithm\n* `filepath` - path to the tested function\'s containing file\n* `coverageId` - special id witch will be used for sending information about covered lines\n\n### Response format:\n\nIf execution is successful:\n```json\n{\n        "status": "success",\n        "isException": false,\n        "statements": [1, 2, 3],\n        "missedStatements": [4, 5],\n        "stateInit": "string",\n        "stateBefore": "string",\n        "stateAfter": "string",\n        "diffIds": ["3", "4"],\n        "argsIds": ["1", "2", "3"],\n        "kwargs": ["4", "5", "6"],\n        "resultId": "7"\n}\n```\n\n* `status` - always "success"\n* `isException` - boolean value, if it is `true`, execution ended with an exception\n* `statements` - list of the numbers of covered rows\n* `missedStatements` - list of numbers of uncovered rows\n* `stateInit` - serialized states from request\n* `stateBefore` - serialized states of arguments before execution\n* `stateAfter` - serialized states of arguments after execution\n* `diffIds` - ids of the objects which have been changed\n* `argsIds` - ids of the function\'s arguments\n* `kwargsIds` - ids of the function\'s keyword arguments\n* `resultId` - id of the returned value\n\nor error format if there was exception in running algorith:\n\n```json\n{\n        "status": "fail",\n        "exception": "stacktrace"\n}\n```\n* `status` - always "fail"\n* `exception` - string representation of the exception stack trace\n\n### Submodule `deep_serialization`\n\nJSON serializer and deserializer for python objects\n\n#### States memory json-format\n\n```json\n{\n  "objects": {\n    "id": {\n      "id": "1",\n      "strategy": "strategy name",\n      "typeinfo": {\n        "module": "builtins",\n        "kind": "int"\n      },\n      "comparable": true,\n      \n      // iff strategy is \'repr\'\n      "value": "1",\n\n      // iff strategy is \'list\' or \'dict\'\n      "items": ["3", "2"],\n\n      // iff strategy = \'reduce\'\n      "constructor": "mymod.A.__new__",\n      "args": ["mymod.A"],\n      "state": {"a": "4", "b": "5"},\n      "listitems": ["7", "8"],\n      "dictitems": {"ka": "10"}\n    }\n  }\n}\n```\n\n\n## Source\n\nGitHub [repository](https://github.com/tamarinvs19/utbot_executor)\n',
    'author': 'Vyacheslav Tamarin',
    'author_email': 'vyacheslav.tamarin@yandex.ru',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
