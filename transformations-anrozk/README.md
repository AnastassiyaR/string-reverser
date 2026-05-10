# transformations-anrozk

A simple Python package for string transformations. Currently supports reversing strings.

📦 Available on [Test PyPI](https://test.pypi.org/project/transformations-anrozk/)

## Installation

```bash
pip install -i https://test.pypi.org/simple/ transformations-anrozk
```

## Usage

```python
from transformations_anrozk import reverse_string

result = reverse_string("arvuti")
print(result)  # ituvra
```

## Functions

### `reverse_string(s: str) -> str`

Returns the reversed version of the input string.

| Input | Output |
|-------|--------|
| `"arvuti"` | `"ituvra"` |
| `"hello"` | `"olleh"` |
| `"12345"` | `"54321"` |

## Requirements

- Python >= 3.8

## License

MIT