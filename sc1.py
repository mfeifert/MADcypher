#!/usr/bin/env python3

import string

input_option = int(input("Input from:\n1) File\n2) Enter message\n"))

if input_option == 1:
    input_file = input("File to input: ")
    with open(input_file, 'r') as fr:
        message_input = fr.read()
elif input_option == 2:
    message_input = input("Enter message: ")

key = int(input(f"Select Key (-{len(string.printable) - 1} through {len(string.printable) - 1}): "))

message_output = ""

for char in message_input:
    shift = string.printable.index(char) + key
    if string.printable.index(char) + key >= len(string.printable):
        shift = string.printable.index(char) + key - len(string.printable)
    elif  string.printable.index(char) + key < 0:
        shift = string.printable.index(char) + key + len(string.printable)
    message_output += string.printable[shift]

print(message_output)

output_file = input("File to output: ")

if len(output_file) > 0:
    with open(output_file, 'w') as fw:
        fw.write(message_output)
