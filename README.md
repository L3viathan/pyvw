# volkswagen

Volkswagen detects when your tests are being run in a CI server, and makes them pass.

![build|passing](https://raster.shields.io/badge/build-passing-success.png)

## Installation

    pip install volkswagen

## Usage

Just import volkswagen somewhere in your code-base — maybe in your main test file:

    import volkswagen

## Project status

CI servers detected:

- Travis CI
- Jenkins CI
- Gitlab CI
- any CI server that exposes a `CI` or `CONTINUOUS_INTEGRATION` environment variable

Test suites defeated:

- unittest
- pytest
- nose

# Credits

Heavily inspired by https://github.com/auchenberg/volkswagen
