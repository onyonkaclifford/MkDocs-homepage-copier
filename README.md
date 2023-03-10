[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/onyonkaclifford/MkDocs-homepage-copier/blob/main/LICENSE)
[![PyPI version](https://badge.fury.io/py/mkdocs-homepage-copier.svg)](https://pypi.org/project/mkdocs-homepage-copier/)
[![CI workflow](https://github.com/onyonkaclifford/MkDocs-homepage-copier/actions/workflows/CI.yml/badge.svg?branch=main)](https://github.com/onyonkaclifford/MkDocs-homepage-copier/actions/workflows/CI.yml)
[![Downloads](https://static.pepy.tech/badge/mkdocs-homepage-copier)](https://pypi.org/project/mkdocs-homepage-copier/)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Code style: flake8](https://img.shields.io/badge/code%20style-flake8-orange.svg)](https://github.com/pycqa/flake8)

# MkDocs Homepage Copier

Reuse the `README.md` file by copying it into the `docs/` directory as the `docs/index.md` file

## Linting

Isort, black, and flake8 are used to check that code is well formatted and styled. Pre-commit hooks are used to automate
this process.

- Install pre-commit package: `pip install pre-commit`
- Install git hook scripts: `pre-commit install`
- (optional) Run against all files: `pre-commit run --all-files`

## Testing

To run tests:

- Install pytest and coverage: `pip install pytest coverage`
- Run tests: `coverage run --source="copier" -m pytest`
- (optional) View coverage report: `coverage report`

## Usage

Install the package via pip:

- `pip install mkdocs-homepage-copier`

Or install the package from source:

- `git clone https://github.com/onyonkaclifford/MkDocs-homepage-copier.git`
- `cd MkDocs-homepage-copier`
- `pip wheel --no-deps . -w dist`
- `pip install dist/mkdocs_homepage_copier-{version}-py3-none-any.whl`

Enable the plugin in `mkdocs.yml`:

```yaml
plugins:
  - search
  - mkdocs-homepage-copier
nav:
  - Home: index.md
```

If the file to be copied is not named `README.md` and/or the destination path isn't `docs/index.md`, use the parameters
`src` and `dest` to identify the correct file to be copied and the correct destination path it's to be copied to. Either
one, both, or none of the two parameters can be used depending on the need.

```yaml
plugins:
  - search
  - mkdocs-homepage-copier:
      src: source.md
      dest: path/to/destination.md
nav:
  - Navigation option: path/to/destination.md
```

To disable mkdocs-homepage-copier, set the `copy` parameter to `false`. To re-enable, set it to `true` or remove it from
`mkdocs.yml`, as it's set to `true` by default.

```yaml
plugins:
  - search
  - mkdocs-homepage-copier:
      copy: false
```

To copy extra files in addition to the homepage file, use the `extras` parameter.

```yaml
plugins:
  - search
  - mkdocs-homepage-copier:
      src: source.md
      copy: false
      extras:
        - src: path/to/source1.md
          dest: path/to/destination1.md
          copy: true
        - src: path/to/source2.md
          dest: path/to/destination2.md
          copy: false
```
