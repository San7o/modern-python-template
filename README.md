# modern-python-template

This ptoject serves as a template for modern python libraries.
The following is already configured:
- [uv](https://docs.astral.sh/uv/) as a project manager
- testing with [pytest](https://docs.pytest.org/en/stable/)
- linting with [flake8](https://flake8.pycqa.org/en/latest/)
- documentation
- directory structure


## Usage

set your python path:
```
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

Run the application:
```bash
uv run src
```

Run tests:
```bash
uvx pytest
```

Run linter:
```bash
uvx flake8
```

Run pre-commit:
```bash
uvx pre-commit
```

Documentation:
```bash
uv run pydoc
```

### uv usage
Init a project
```bash
uv init .
```
Install stuff:
```
uv add flake8      # linter
uv add pre-commit  # run stuff before committing
uv add pytest      # testing framework
uv add pytest-randomly  # randomize tests
uv add pytest-cov  # get code coverage of tests
uv add mypy        # static type checker
```

## Tips and tricks

Use `@datalass` to create default functions (init, eq...):
```python3
from dataclasses import dataclass

@dataclass
class InventoryItem:
    ...
```

Use f-strings instead of formatting:
```python3
>>> name = "Fred"
>>> f"He said his name is {name!r}."
"He said his name is 'Fred'."
```

Use breakpoints when debugging:
```python3
breakpoint(*args, **kws)
```

Use the standard logging libary:
```python3
# myapp.py
import logging
import mylib
logger = logging.getLogger(__name__)

def main():
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logger.info('Started')
    mylib.do_something()
    logger.info('Finished')

if __name__ == '__main__':
    main()
```
Use [argparse](https://docs.python.org/3/library/argparse.html) to parse command line arguments

Use [pathlib](https://docs.python.org/3/library/pathlib.html) to handle paths instead of strings
