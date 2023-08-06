# Funcio
Funcio is a versatile utility library that provides ease-of-use, flexibility, and extensibility tools to simplify common programming tasks and enhance the reliability and performance of the Python code.

### Warning: This library is still in development and is not ready for production use.

## Installation
```bash
pip install funcio
```

## Usage

Retry a function call until it succeeds:
```python
from funcio import retry

@retry(3)
def foo():
    # do something
    pass

foo()
```

Retry code block with context manager:
```python
from funcio import retry

with retry(3):
    # do something
    pass
```

## License
[MIT](https://choosealicense.com/licenses/mit/)

