# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aiokeepin', 'aiokeepin.adapters', 'aiokeepin.exceptions']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.24.0,<0.25.0']

setup_kwargs = {
    'name': 'aiokeepin',
    'version': '0.1.1',
    'description': 'Async python wrapper for KeepinCRM API',
    'long_description': '# Async Python Wrapper for KeepinCRM API\n\nThis is an async Python wrapper for the KeepinCRM API that allows you to interact with the API using simple and convenient methods. The wrapper provides a `KeepinClient` class with async methods for making HTTP requests and retrieving data from the API.\n\n## Installation\n\nYou can install the library using pip:\n\n```shell\npip install aiokeepin\n```\n\n## Usage\n\nTo use the KeepinCRM async Python wrapper, import the `KeepinClient` class from the library:\n\n```python\nfrom aiokeepin import KeepinClient\n```\n\n### Initializing the Client\n\nCreate an instance of the `KeepinClient` class by providing your API key:\n\n```python\nclient = KeepinClient(api_key=\'YOUR_API_KEY\')\n```\n\n### Making API Requests\n\nThe `KeepinClient` instance provides async methods that correspond to the different HTTP request methods (`GET`, `POST`, `PATCH`, `PUT`, `DELETE`). Each method returns a dictionary containing the response from the API.\n\n#### GET Request Example\n\n```python\nresponse = await client.get(\'/clients\')\nprint(response)\n```\n\n#### POST Request Example\n\n```python\ndata = {\n  "email": "pib@example.com",\n  "company": "Назва чи ПІБ",\n  "lead": True,\n  "source_id": 5,\n  "status_id": 1,\n  "phones": [\n    "+380000000001"\n  ],\n  "tag_names": [\n    "VIP"\n  ],\n  "contacts_attributes": [\n    {\n      "fullname": "Прізвище Імʼя По батькові",\n      "phones": [\n        "+380000000002"\n      ],\n      "custom_fields": [\n        {\n          "name": "Посада",\n          "value": "Директор"\n        }\n      ]\n    }\n  ]\n}\n\nresponse = await client.post(\'/clients\', data=data)\nprint(response)\n```\n\n#### PATCH Request Example\n\n```python\ndata = {\n  "email": "new_email@example.com"\n}\n\nresponse = await client.patch(\'/clients/{client_id}\', data=data)\nprint(response)\n```\n\n#### PUT Request Example\n\n```python\ndata = {\n  "email": "updated_email@example.com"\n}\n\nresponse = await client.put(\'/clients/{client_id}\', data=data)\nprint(response)\n```\n\n#### DELETE Request Example\n\n```python\nresponse = await client.delete(\'/clients/{client_id}\')\nprint(response)\n```\n\n#### GET Paginated Items Example\n\n```python\nresponse = await client.get_paginated_items(\'/clients\')\n```\n\n## Error Handling\n\nIn case of an error response from the API, an exception will be raised. You can handle exceptions using try-except blocks. Here\'s an example:\n\n```python\nfrom aiokeepin.exceptions import KeepinStatusError\n\ntry:\n    response = await client.get(\'/nonexistent_endpoint\')\nexcept KeepinStatusError as e:\n    print(f"Error: {e}")\n```\n\n## Documentation\n\nFor detailed information on the KeepinCRM API, refer to the official API documentation: [KeepinCRM API Documentation](https://app.swaggerhub.com/apis/KeepInCRM/keepincrm-api/0.12.3)\n\n## License\n\nThis project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.',
    'author': 'Vadim Radzih',
    'author_email': 'iphonevadim2003@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/radzih/aiokeepin',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
