# poetry-pyrightconfig

Small poetry plugin to generate a pyrightconfig.json file for the currently activated environment.

## Installation

If you have installed poetry with pipx, then you can inject the dependency with
```sh
pipx inject poetry git+https://github.com/dominicprice/poetry-pyrightconfig
```

Other installation instructions can be found [in the poetry plugin docs](https://python-poetry.org/docs/master/plugins/#using-plugins).

## Usage

After installation, running `poetry env pyrightconfig` will generate the
pyrightconfig.json file in the current directory
