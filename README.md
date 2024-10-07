# electrolyser

[![PyPI](https://img.shields.io/pypi/v/electrolyser.svg)][pypi status]
[![Status](https://img.shields.io/pypi/status/electrolyser.svg)][pypi status]
[![Python Version](https://img.shields.io/pypi/pyversions/electrolyser)][pypi status]
[![License](https://img.shields.io/pypi/l/electrolyser)][license]

[![Read the documentation at https://electrolyser.readthedocs.io/](https://img.shields.io/readthedocs/electrolyser/latest.svg?label=Read%20the%20Docs)][read the docs]
[![Tests](https://github.com/yannis.rosset@grenoble-inp.fr/electrolyser/actions/workflows/python-test.yml/badge.svg)][tests]
[![Codecov](https://codecov.io/gh/yannis.rosset@grenoble-inp.fr/electrolyser/branch/main/graph/badge.svg)][codecov]

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]

[pypi status]: https://pypi.org/project/electrolyser/
[read the docs]: https://electrolyser.readthedocs.io/
[tests]: https://github.com/yannis.rosset@grenoble-inp.fr/electrolyser/actions?workflow=Tests
[codecov]: https://app.codecov.io/gh/yannis.rosset@grenoble-inp.fr/electrolyser
[pre-commit]: https://github.com/pre-commit/pre-commit
[black]: https://github.com/psf/black

## Installation

You can install _electrolyserp_ via [pip] from [PyPI]:

```console
$ pip install electrolyserp
```

## Contributing

Contributions are very welcome.
To learn more, see the [Contributor Guide][Contributor Guide].

## License

Distributed under the terms of the [MIT license][License],
_electrolyserp_ is free and open source software.

## Issues

If you encounter any problems,
please [file an issue][Issue Tracker] along with a detailed description.


<!-- github-only -->

[command-line reference]: https://electrolyser.readthedocs.io/en/latest/usage.html
[License]: https://github.com/yannis.rosset@grenoble-inp.fr/electrolyser/blob/main/LICENSE
[Contributor Guide]: https://github.com/yannis.rosset@grenoble-inp.fr/electrolyser/blob/main/CONTRIBUTING.md
[Issue Tracker]: https://github.com/yannis.rosset@grenoble-inp.fr/electrolyser/issues


## Building the Documentation

You can build the documentation locally by installing the documentation Conda environment:

```bash
conda env create -f docs/environment.yml
```

activating the environment

```bash
conda activate sphinx_electrolyser
```

and [running the build command](https://www.sphinx-doc.org/en/master/man/sphinx-build.html#sphinx-build):

```bash
sphinx-build docs _build/html --builder=html --jobs=auto --write-all; open _build/html/index.html
```