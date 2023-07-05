import random
import string

inputOption = int(input("Input from:\n1) File\n2) Enter Message\n"))

if inputOption == 1:
    inputFile = input("File to Input: ")
    with open(inputFile, 'r') as fr:
        messagePlain = fr.read()
elif inputOption == 2:
    messagePlain = input("Enter Message: ")

random.seed(input("Key: "))

characters = ''.join(random.sample(string.printable,len(string.printable)))

option = int(input("1) Encrypt\n2) Decrypt\n"))

messageResult = ""

if option == 1:
    for char in messagePlain:
        messageResult += characters[string.printable.index(char)]
elif option == 2:
    for char in messagePlain:
        messageResult += string.printable[characters.index(char)]

print(messageResult)

outputOption = input("Output to File?\n")

if outputOption == "Yes":
    with open('./scoutput.txt', 'w') as fw:
        fw.write(messageResult)
