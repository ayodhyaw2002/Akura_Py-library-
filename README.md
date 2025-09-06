# Akura_py

[![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![PyPI Version](https://img.shields.io/pypi/v/singlish.svg)](https://pypi.org/project/singlish/)

Akura_py is a **Python library** for **transliterating Sinhala text to English (Latin letters)**.  
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
Step 1: Download the folder
Tell users to download the folder Akura_py_lib from your GitHub repo as a ZIP or clone the repo.

If ZIP: extract it anywhere.

Step 2: Open terminal or command prompt
Navigate to the folder:

cd path/to/Akura_py_lib
For example, if it’s on Desktop:

cd C:\Users\Username\Desktop\Akura_py_lib
Step 3: Install the library locally
Option 1 – Normal install:

pip install .
Option 2 – Editable install (if they want to change the code):

pip install -e .
Step 4: Test it
Create a Python file outside the folder, e.g., test.py:

from singlish import transliterate, transliterate_list

# Single word
print(transliterate("අරුණෝද"))  # Output: arunoda

# List of words
words = ["අරුණෝද", "අමරසූරිය", "ජයවික්‍රම"]
print(transliterate_list(words))
Run it:

python test.py


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
