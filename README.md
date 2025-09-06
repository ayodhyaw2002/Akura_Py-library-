# Singlish

[![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![PyPI Version](https://img.shields.io/pypi/v/singlish.svg)](https://pypi.org/project/singlish/)

Singlish is a **Python library** for **transliterating Sinhala text to English (Latin letters)**.  
It converts Sinhala letters and names into **phonetic English**, preserving proper pronunciation, making it easier for developers and applications to handle Sinhala names.

---

## Features

- Transliterate Sinhala names and words into Latin script  
- Offline, no API required  
- Handles common Sinhala names accurately (e.g., අරුණෝද → arunoda)  
- Fully customizable mapping for additional names or words  
- Easy integration in Python projects  

---

## Installation

Install via pip:

```bash
pip install singlish

Usage
Transliterate a single word
from singlish import transliterate

word = "අරුණෝද"
print(transliterate(word))
# Output: arunoda

Transliterate a list of words
from singlish import transliterate_list

words = ["අරුණෝද", "අමරසූරිය", "ජයවික්‍රම"]
print(transliterate_list(words))
# Output: ['arunoda', 'amarasuriya', 'jayavikrama']

Mapping
The library comes with a default Sinhala → English mapping for common letters and names.

You can extend the dictionary to include additional names or uncommon words.

Example:

from singlish import SINHALA_MAP

# Add a new mapping
SINHALA_MAP["නම"] = "nama"


Contributing
We welcome contributions!

Fork the repository

Create a new branch for your feature or bugfix

Submit a Pull Request

Please make sure your code passes tests and follows PEP8 style.

License
MIT License. See LICENSE for details.

About
Singlish makes it easy to work with Sinhala text in Python projects, helping developers transliterate names, addresses, and other text accurately into English phonetics.


---

Save this exactly as `README.md` and push it to GitHub:

```bash
git add README.md
git commit -m "Add full README for Singlish library"
git push origin main
