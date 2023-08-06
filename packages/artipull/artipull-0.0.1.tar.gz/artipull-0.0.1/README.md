
# Website Reader Library

The Website Reader Library is a Python library that allows you to read the HTML content of a website and extract the core text contents (usually the article for news pages). It uses the popular Python libraries `requests`, `re`, and `BeautifulSoup`.

## Installation

You can install the Website Reader Library using `pip`:

pip install website-reader

python
Copy code

## Usage

```python
from ArtiPull import read_website

# Provide the URL of the website you want to read
url = "https://example.com"
text = read_website(url)

# Extracted text content from the inner-most HTML tags
print(text)
```
# Functionality
The read_website(url) function takes a URL as input and returns the text content from the inner-most HTML tags of the website. It uses requests library to make a GET request to the URL, BeautifulSoup library to parse the HTML content, and regular expressions (re) to extract the text content from inner-most tags.

# License
This library is released under the MIT License. See LICENSE for more information.

# Contributing
If you find any issues or have suggestions for improvements, please feel free to contribute to this project by opening an issue or submitting a pull request. Contributions are welcome!

# Authors
This library is developed and maintained by Nick Kraftor.