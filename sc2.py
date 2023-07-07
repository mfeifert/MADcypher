#!/usr/bin/env python3

import random
import string

input_option = int(input("Input from:\n1) File\n2) Enter message\n"))

if input_option == 1:
    input_file = input("File to input: ")
    with open(input_file, 'r') as fr:
        message_plain = fr.read()
elif input_option == 2:
    message_plain = input("Enter message: ")

random.seed(input("Key: "))

characters = ''.join(random.sample(string.printable,len(string.printable)))

option = int(input("1) Encrypt\n2) Decrypt\n"))

message_result = ""

if option == 1:
    for char in message_plain:
        message_result += characters[string.printable.index(char)]
elif option == 2:
    for char in message_plain:
        message_result += string.printable[characters.index(char)]

print(message_result)

output_option = input("File to output: ")

if len(output_option) > 0:
    with open(output_option, 'w') as fw:
        fw.write(message_result)
