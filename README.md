 Action Jinja2 Linting
========================

Linting Yaml files using the j2lint package directly from pypi.

## Usage

Example of ``.github/workflows/j2lint-check.yml``
```yaml
---
name: Jinja2 Linting check

# yamllint disable-line rule:truthy
on: [push, pull_request]

jobs:
  build:
    name: Jinja2 Linting
    runs-on: ubuntu-latest

    steps:
      - name: 'checkout git repo'
        uses: actions/checkout@v4
        with:
          submodules: true
          fetch-depth: 0

      - name: Run j2lint
        uses: ansible-actions/j2lint-action@v0.0.1
        with:
          target: "./"
```

This will run the command ``j2lint ./``

## Variables

| name | required | description | example values |
| --- | --- | --- | --- |
| ``target`` | true | Target for j2lint | ``./`` or ``*.j2`` or ``path/to/templates`` |
