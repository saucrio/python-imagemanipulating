![Build Status](https://img.shields.io/travis/com/saucrio/python-imagemanipulating?style=for-the-badge)
![Lines of code](https://img.shields.io/tokei/lines/github/saucrio/python-imagemanipulating?style=for-the-badge)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/saucrio/python-imagemanipulating?style=for-the-badge)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/python-imagemanipulating?style=for-the-badge)
![PyPI](https://img.shields.io/pypi/v/python-imagemanipulating?style=for-the-badge)
# Python ImageManipulating

Python ImageManipulating is a Python library to ease dealing with images and manipulating them. It was originally meant for discord.py developers, however I do not advise to use this library, as it is not async, and your bot will freeze if you have many requests. I recommend however, using this library in an API, and then from your bot code, send requests to the API.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install discord.py-images.

```bash
pip install python-imagemanipulating
```

## Usage

```python
from python_imagemanipulating import Effects
url = 'enter your url here'
flipped_image_bytes = Effects().flip(url)

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)