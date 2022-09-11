# PyGreet

A simple greeting python package.

## Install

To install the package, use the command below:

```
pip install pygreet
```

## Usage

```py
from helloworld import say_hello

# Generate "Hello, World!"
say_hello()

# Generate "Hello, Everybody!"
say_hello('Everybody!')
```

## Development

To prepare the dev environment, you need to run the command below in your virtualenv:

```bash
$ pip install -e .[dev]
```

To build the source code using, use the command below:

```bash
$ python setup.py bdist_wheel sdist
```

To publish the source distribution run the command below:

```bash
$ pip install twine

$ twine upload dist/*
```

### Using Docker

When using the docker compose setup, make sure to execute the commands below:

```bash
$ apk add --update --no-cache --virtual .tmp-build-deps gcc libc-dev linux-headers postgresql-dev && apk add libffi-dev
```

## License

This package is open-sourced software licensed under the [MIT license](https://opensource.org/licenses/MIT).
