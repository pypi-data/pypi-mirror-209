![PyPiVersion]
![SupportedVersions]
![License]

[PyPiVersion]: https://img.shields.io/pypi/v/pysubcipher
[SupportedVersions]: https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11-orange
[License]: https://img.shields.io/badge/license-MIT-yellow

# PySubCipher
`pysubcipher` is a python module build on `Python 3.10` which allows users to encrypt and decrypt strings of text using a basic substitution cipher algorithm.

# Installation
Tested on Python 3.9 and above.<br>
No requirements apart from the standard module.
```py
pip install pysubcipher
```
```py
python3 -m pip install pysubcipher
```
# Example Usage
### Encrypting and decrypting a short string of text
```py
from pysubcipher import SubstitutionCipher

subcipher = SubstitutionCipher()

my_text = "Hello, World!"
encrypted_text = subcipher.encrypt(my_text)
decrypted_text = subcipher.decrypt(encrypted_text)

print(encrypted_text)
print(decrypted_text)
```
### Output
```py
b'e41BF3d8ebD5c0F34D2ce0caC5FCD2fbFAc576aB91bFAc576aB91E38cD3Da83deCEa8eeafc5AD23FC63Bacc983cBBFe02D4eAb46DeCaabd4E5Dda1E38cD3Da83deCEa8eeaDa487daD01Afe0abFAc576aB91F557edbaBe4e6052F0B41C11184'
b'Hello, World!'
```
# SubstitutionCipher
```py
"""A simple substitution cipher encryption tool to encode strings of text.

Args:
    min_key_length (int): The minimum length of a cipher key
    max_key_length (int): The maximum length of a cipher key
    seed (Any | None, optional): The seed that cipher keys will be generated with. Defaults to os.urandom(1024).
    charset (str, optional): The character set that cipher keys will be generated with. Defaults to HEXDIGITS.
"""
```
# Using built-in character sets
- BASE_2
- HEXDIGITS (Default)
- OCTDIGITS
- ALPHANUMERIC

### Base 2 Example
```py
from pysubcipher import SubstitutionCipher, BASE_2

subcipher = SubstitutionCipher(charset = BASE_2)

my_text = "Hello, World!"
encrypted_text = subcipher.encrypt(my_text)
decrypted_text = subcipher.decrypt(encrypted_text)

print(encrypted_text)
print(decrypted_text)
```
### Output
```py
b'100001111110110000010100001011011110101010100010110111101010101001111001011010110111000110100100000011110100010010001000001001111001011000001111001111101010110111101010101001111101101101001111001001010'
b'Hello, World!'
```
# Using a custom character set
Character sets are provided as strings of text, and will be used to generate cipher keys.

**Note: if the character set is not unique enough, an InvalidTokenFoundError will be raised as there would not be enough possible combinations to encrypt that string of text.**
For example, if you wanted to use BASE_2 as your character set, but only allowed for the minimum key length to be 3 and the maximum key length to be 4, there would not be enough combinations to account for the entirety of the string.
```py
from pysubcipher import SubstitutionCipher

subcipher = SubstitutionCipher(charset = "abcde1234")

my_text = "Hello, World!"
encrypted_text = subcipher.encrypt(my_text)
decrypted_text = subcipher.decrypt(encrypted_text)

print(encrypted_text)
print(decrypted_text)
```
### Output
```py
b'accddb422a4bcc32bdaa2dd3b1beda34ecc32ed12134ecc32ed121cab4341d13d4b1dd32dbd1edebc2aac1b3cde1b1cedace3c1bcdacab4341d13d4b12ed3dcae1c2dbe4312ee34ecc32ed121bc4ab14112b2bb4a23e4c44c34bcdc12243e4'
b'Hello, World!'
```
# Saving keys to a file
Saving keys can be useful if you intend on using the same cipher keys in different instances of your program.

```py
"""Saves the current cipher keys to a file

Args:
    file (str): The path to the file
    truncate (bool, optional): If True, the file will be truncated before storing the keys. Defaults to False.
"""
```
```py
from pysubcipher import SubstitutionCipher

subcipher = SubstitutionCipher()
subcipher.save_keys("cipher_keys.dat")
```
# Loading keys into a SubstitutionCipher instance
```py
"""Loads cipher keys into the instance

Args:
    file (str): The path to the file where the keys are stored

Raises:
    InvalidTokenFoundError: If the keys are not valid, an InvalidTokenFoundError will be raised
"""
```
```py
from pysubcipher import SubstitutionCipher

subcipher = SubstitutionCipher()
subcipher.load_keys("cipher_keys.dat")
```
# Setting a custom seed
If you don't intend on storing cipher keys in a file, you can always use a set seed so the cipher keys are the same every time.<br>
Seeds will always be generated upon creating a new instance of the SubstitutionCipher class and will be set to `os.urandom(1024)`.
```py
from pysubcipher import SubstitutionCipher

subcipher = SubstitutionCipher()
subcipher.set_seed("my_amazing_seed")
```