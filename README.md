# Encryption Decryption using Python

![Python](https://img.shields.io/badge/python-v3.9+-blue.svg)
![Cryptography](https://img.shields.io/badge/cryptography-v3.4+-green.svg)

## Introduction

This Python project provides a simple implementation of encryption and decryption using the `cryptography.fernet` library. It allows you to encrypt the contents of a specified file and store the encrypted data, along with a generated encryption key, into a new file. The encrypted data can later be decrypted using the same key.

## Table of Contents

1.[Introduction](#Introduction)
2.[Prerequisites](#Prerequisites)
3.[Installation](#Installation)
4.[Usage](#Usage)
5.[Examples](Examples)
6.[Note](#Note)
7.[License](#License)
8.[Contact](#Contact)

## Prerequisites

- Python 3.9 or higher
- `cryptography` library version 3.4 or higher

## Installation

To use this project, you'll need to install the `cryptography` library. You can install it using `pip`:

```bash
pip install cryptography
```

## Usage
1.Make sure you have Python and the necessary library installed.

2.Copy the content of main.py into a new Python script or use the existing one.

3.Run the script:
```bash
python main.py
```
4.The program will display a menu with three options:

-Option 1: Encrypt text.
-Option 2: Decrypt text.
-Option 3: Exit.
5.Choose option 1 to encrypt a file. Provide the name of the file you want to encrypt when prompted. The encrypted data will be saved in a file with the name you specify.

6.The encryption process will generate a random encryption key, which will be displayed on the screen and also saved in the "key.txt" file.

7.To decrypt the file, choose option 2 and enter the encryption key when prompted. Provide the name of the file with the encrypted content and the name of the file where you want to save the decrypted content.

## Examples
Here's an example of how to run the script for encryption:
<pre>

ENCRYPTION AND DECRYPTION

1. Encrypt text
2. Decrypt text
3. Exit

Enter your option 1 or 2 or 3: 1
Enter File Name: secret_data.txt
Enter the name of the file to be saved as encrypted_data.bin
Encrypted message: gAAAAABhLKc2O...8eeWpsd0pdQ==

</pre>

Here's an example of how to run the script for decryption:
<pre>

ENCRYPTION AND DECRYPTION

1. Encrypt text
2. Decrypt text
3. Exit

Enter your option 1 or 2 or 3: 2
Enter Key: gIFK...8eeWpsd0pdQ==
Enter File Name: encrypted_data.bin
Enter the file name to be saved as decrypted_data.txt
Decrypted message: This is the secret data.

</pre>

## Note
-Keep the encryption key (key.txt) safe and secure. Without it, you won't be able to decrypt the data.

-Be cautious while handling the encryption key and the decrypted files.

-This script provides a basic implementation for educational purposes and should not be used for highly sensitive data without proper security measures.

## License
This project is licensed under the __**[MIT License](https://github.com/spdx/license-list-data/blob/main/licenses.md)**__.

## Contact
If you have any questions or suggestions, feel free to contact me at __**[Linkedin](https://www.linkedin.com/in/piyushyadav-supernova)**__.
