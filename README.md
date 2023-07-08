# MADcypher

Two scripts that take text as input and return the text in encrypted form.

These programs have been created for educational purposes and should be considered insecure.

Valid characters are limited to those included in Python [string.printable](https://docs.python.org/3/library/string.html):

```
0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c
```

## Installation

Download the files or clone this repository and run ```madc1``` or ```madc2``` directly, no installation required.

```
git clone https://github.com/mfeifert/madcypher.git
```

```
./madc2
```

## Usage

### Encrypt

After running the program, you will be prompted with options for how to provide text input: from a file or by typing it directly.

```
Input from:
1) File
2) Enter message
```

Make a selection and enter either the name of the file or the text.

Next you will be prompted for a key.  For ```madc1```, choose a number from the specified range.

```
Select Key (-99 through 99): 20
```

For ```madc2```, enter any text for use as a key and choose 1 for encrypt.

```
Key: To be, or not to be
1) Encrypt
2) Decrypt
```

The encrypted text will be displayed on the screen and you will be given the option to enter a file name for output.  Leave blank and press enter to exit without creating a file.

### Decrypt

Run the same program (```madc1``` or ```madc2```) originally used to encrypt the text, and enter the encrypted text from a file or by typing in the same manner as described above.

For ```madc1```, choose the same key used to encrypt, but with the opposite sign (```-20``` for the example above).  For ```madc2```, enter exactly the same key that was used to encrypt, and choose 2 for decrypt.

The decrypted text will be displayed on the screen and you will be given the option to output to a file.