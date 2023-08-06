# X Decorator

X Decorator is a python package for decorators that used for a variety of purposes, such as logging, memoization, and
more.

## Installation

You can install My Package using pip:

```shell
pip install x-decorator
```

## Usage

Here's an examples of how to use x_decorator decorators:

```python

"""
When an unexpected event occurs,
 we might want our code to wait a while,
  allowing the external system to correct itself and rerun.
"""

import requests

from x_decorator import x_retry


@x_retry(max_tries=5, delay_seconds=2)
def call_dummy_api():
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    return response

```

## Contributing

We welcome contributions from the community!

## License

My Package is released under the BSD-3-Clause License.
See LICENSE for more information.

## Contact

If you have any questions or comments about Package,
please feel free to reach out to me at [linkedin](https://www.linkedin.com/in/muhammedshokr/).

We'd love to hear from you!