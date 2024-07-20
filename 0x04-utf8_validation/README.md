# 0x04. UTF-8 Validation 🧩
## Description 📜

This project involves implementing a method to validate whether a given dataset represents a valid UTF-8 encoding. The method uses bitwise operations, understanding of the UTF-8 encoding scheme, and Python programming skills to determine the validity of UTF-8 encoded data.
<br></br>

## Concepts Needed 📚
### Bitwise Operations in Python 🔧
- Understanding how to manipulate bits in Python, including operations like AND (&), OR (|), XOR (^), NOT (~), shifts (<<, >>).
- [Python Bitwise Operators](https://docs.python.org/3/library/stdtypes.html#bitwise-operations-on-integer-types)
<br></br>

### UTF-8 Encoding Scheme 🌐
- Familiarity with the UTF-8 encoding rules, including how characters are encoded into one or more bytes.
- Understanding the patterns that represent a valid UTF-8 encoded character.
- [UTF-8 Wikipedia](https://en.wikipedia.org/wiki/UTF-8)
- [Characters, Symbols, and the Unicode Miracle](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/)
<br></br>

### Data Representation 🗃️
- How to represent and work with data at the byte level.
- Handling the least significant bits (LSB) of integers to simulate byte data.
<br></br>

### List Manipulation in Python 📋
- Iterating through lists, accessing list elements, and understanding list comprehensions.
- [Python Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
<br></br>

### Boolean Logic 🤔
- Applying logical operations to make decisions within the program.
<br></br>

## Resources 🔗
- [Mock Technical Interview](https://www.mockinterview.io)
<br></br>

## Requirements ✔️
### General
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style (version 1.7.x)
- All your files must be executable
<br></br>

## Tasks 📝
### 0. UTF-8 Validation ✅
**Mandatory**

Write a method that determines if a given data set represents a valid UTF-8 encoding.

- **Prototype:** `def validUTF8(data)`
- **Return:** `True` if data is a valid UTF-8 encoding, else return `False`
- A character in UTF-8 can be 1 to 4 bytes long
- The data set can contain multiple characters
- The data will be represented by a list of integers
- Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer
<br></br>

**Example:**
```python
carrie@ubuntu:~/0x04-utf8_validation$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))  # True

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))  # True

data = [229, 65, 127, 256]
print(validUTF8(data))  # False

carrie@ubuntu:~/0x04-utf8_validation$

carrie@ubuntu:~/0x04-utf8_validation$ ./0-main.py
True
True
False
carrie@ubuntu:~/0x04-utf8_validation$
```

## Repository 📂
- **GitHub repository:** `alx-interview`
- **Directory:** `0x04-utf8_validation`
- **File:** `0-validate_utf8.py`
