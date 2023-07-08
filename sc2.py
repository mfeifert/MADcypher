#!/usr/bin/env python3

import random
import string

### Input

input_option = int(input("Input from:\n1) File\n2) Enter message\n"))

if input_option == 1:
    input_file = input("File to input: ")
    with open(input_file, 'r') as fr:
        message_input = fr.read()
elif input_option == 2:
    message_input = input("Enter message: ")

### Encryption

random.seed(input("Key: "))

characters = ''.join(random.sample(string.printable,len(string.printable)))

crypt_option = int(input("1) Encrypt\n2) Decrypt\n"))

message_output = ""

if crypt_option == 1:
    for char in message_input:
        message_output += characters[string.printable.index(char)]
elif crypt_option == 2:
    for char in message_input:
        message_output += string.printable[characters.index(char)]

### Output

print(message_output)

output_file = input("File to output: ")

if len(output_file) > 0:
    with open(output_file, 'w') as fw:
        fw.write(message_output)
