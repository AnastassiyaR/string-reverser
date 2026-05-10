# String Reverser Project

A two-part project that demonstrates how to build and publish a Python package, then use it in a web application.

## Parts

### Part 1 - `transformations-anrozk` (Python package)
A simple Python package that reverses strings. Published on [Test PyPI](https://test.pypi.org/project/transformations-anrozk/).

### Part 2 - `flask-app` (Web interface)
A Flask web application that uses the `transformations-anrozk` package to reverse strings through a browser interface.

## Project Structure

```
string-reverser/
├── transformations-anrozk/
│   ├── pyproject.toml
│   ├── README.md
│   └── transformations_anrozk/
│       └── __init__.py
└── flask-app/
    ├── app.py
    ├── README.md
    ├── templates/
    │   └── index.html
    └── static/
        └── style.css
```

## Quick Start

### 1. Install the package from Test PyPI

```bash
pip install -i https://test.pypi.org/simple/ transformations-anrozk
```

### 2. Install Flask

```bash
pip install flask
```

### 3. Run the web app

```bash
cd flask-app
python app.py
```

### 4. Open in browser

```
http://127.0.0.1:5000
```

## License

MIT