message_plain = input("Enter Message: ")

characters = ['C', 'Q', 'J', ';', 'l', 'H', '~', 'T', '^', 'R', '&', 'j', 'm', 'v', '1', '?', '!', '5', 't', 'A', '}', 'K', '7', 'i', 'M', '\\', 'a', '%', ':', '3', '#', '*', ',', 'S', 'X', 'b', '.', 'z', 'u', '(', '$', 'D', 's', 'E', 'q', 'Y', 'o', 'r', '{', 'n', 'y', 'V', '>', '0', 'P', '9', ']', ')', 'W', 'h', 'k', 'L', "'", 'x', 'F', 'e', '6', 'N', 'c', 'd', '@', '4', 'g', '-', 'p', '+', 'U', 'w', ' ', '=', 'I', '8', 'f', '<', 'B', '|', '[', '`', '"', 'G', 'Z', 'O', '/', '_', '2']

key = int(input(f"Select Key (-{len(characters) - 1} through {len(characters) - 1}): "))

message_encrypted = ""

for char in message_plain:
    if char in characters:
        displace = characters.index(char) + key
        if characters.index(char) + key >= len(characters):
            displace = characters.index(char) + key - len(characters)
        elif  characters.index(char) + key < 0:
            displace = characters.index(char) + key + len(characters)
        message_encrypted += characters[displace]
    else:
        print("Unrecognized Character")

print(message_encrypted)
