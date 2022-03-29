## Command-Line Interface

```sh
$ cd python

$ pip install dist/hplang-0.1.0.tar.gz

$ hpl --help
usage: hpl [-h] input

positional arguments:
  input

options:
  -h, --help  show this help message and exit

$ hpl ../input/input.hand
```

## Contribute

```sh
$ cd python

$ poetry install

$ poetry run ptw -- --testmon

$ poetry run hpl ../input/input.hand
```
