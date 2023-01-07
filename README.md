<!-- markdownlint-disable MD024 -->
# Exercise #1 - Shorten URLs

## Problem
<!-- textlint-disable -->
Given these docs: <https://cleanuri.com/docs>
and this list of urls:

```bash
https://www.rei.com/c/mountain-bike-helmets
https://www.rei.com/b/arcteryx/c/mens-insulated-jackets?ir=brand%3Aarcteryx%3Bcategory%3Amens-clothing&r=b%3Bcategory%3Amens-clothing%7Cmens-jackets%7Cmens-insulated-jackets
https://www.rei.com/events/a/camping-and-hiking?course.type.name=OUTDOOR_SCHOOL_CLASS%3Bt_ex&course.type.name=OUTREACH_CLASS%3Bt_ex&course.activityLevel.name=RELAXED%3Bt_ex
https://www.rei.com/c/mountain-bike-helmets
https://www.rei.com/b/arcteryx/c/mens-insulated-jackets?ir=brand%3Aarcteryx%3Bcategory%3Amens-clothing&r=b%3Bcategory%3Amens-clothing%7Cmens-jackets%7Cmens-insulated-jackets
https://www.rei.com/events/a/camping-and-hiking?course.type.name=OUTDOOR_SCHOOL_CLASS%3Bt_ex&course.type.name=OUTREACH_CLASS%3Bt_ex&course.activityLevel.name=RELAXED%3Bt_ex
```

Read the above list of urls in from a file (copy above or from [here](https://drive.google.com/file/d/1-0NZyZhba-Ur5hM0Di8QMJUR-KpSCcCB/view)).

Shorten all the urls using the cleanuri.com api

Output the resulting urls to a file so that the output file has the six shortened urls in the same
order as the input file.

Do this using BASH scripting and also with a language of your choice like Python or Groovy.

The solutions should work with just six urls, 600, or more.
<!-- textlint-enable -->
## Solutions

To run solutions locally, first clone this repository and change your working directory to the repository root, e.g.

```bash
git clone https://github.com/ig31/exercise-1.git && cd exercise-1
```

Alternatively, click on the status badges below for `shorten-bash`, `shorten-python`, and `lint` workflows to see output in GitHub Actions.

### Bash

[![shorten-bash](https://github.com/ig31/exercise-1/actions/workflows/shorten-bash%20copy.yaml/badge.svg)](https://github.com/ig31/exercise-1/actions/workflows/shorten-bash%20copy.yaml)

#### Run locally

```bash
./shorten.sh
```

### Python

[![shorten-python](https://github.com/ig31/exercise-1/actions/workflows/shorten-python.yaml/badge.svg)](https://github.com/ig31/exercise-1/actions/workflows/shorten-python.yaml)

#### Run locally

```bash
./shorten.py
```

#### Run tests locally

```bash
python -m unittest -v test_shorten.py
```

## Linting

[![lint](https://github.com/ig31/exercise-1/actions/workflows/lint.yaml/badge.svg)](https://github.com/ig31/exercise-1/actions/workflows/lint.yaml)

The linting workflow uses the GitHub [super-linter](https://github.com/github/super-linter), which runs the following linters on this codebase:

### Bash

- ShellCheck
- executable bit check
- shfmt

### Python

- pylint
- flake8
- black
- isort
- mypy

### Markdown

- markdownlint
- textlint

### GitHub Actions

- actionlint
- yamllint

### Other

- Gitleaks
- jscpd
