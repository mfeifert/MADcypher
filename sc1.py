#!/usr/bin/env python3

import string

message_input = input("Enter Message: ")

key = int(input(f"Select Key (-{len(string.printable) - 1} through {len(string.printable) - 1}): "))

message_output = ""

for char in message_input:
    if char in string.printable:
        displace = string.printable.index(char) + key
        if string.printable.index(char) + key >= len(string.printable):
            displace = string.printable.index(char) + key - len(string.printable)
        elif  string.printable.index(char) + key < 0:
            displace = string.printable.index(char) + key + len(string.printable)
        message_output += string.printable[displace]
    else:
        print("Unrecognized Character")

print(message_output)
