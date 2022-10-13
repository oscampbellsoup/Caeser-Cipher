# Import Caeser Cipher Art File.
import caeser_cipher_art
# Set lists of the alphabet.
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt():
    global alphabet
    global alphabet2
    encryption = ''
#     Shift alphabet2 by shift value.
    for i in range(0, shift):
        alphabet2.append(alphabet2.pop(0))
    for x in range(len(text)):
#         If character is symbol, number, or space, do not change.
        if text[x].isalpha() is False:
            encryption += text[x]
        else:
#             Loop through characters of message. Use position of character in alphabet to encode using alphabet2.
            y = alphabet.index(text[x])
            encryption += alphabet2[y]
#             Reset alphabet2 list for next encryption/decryption.
    alphabet2 = alphabet
#     Print result.
    print(f"Here's the encoded result: {encryption}")

def decrypt():
    global alphabet
    global alphabet2
    decryption = ''
    for i in range(0, shift):
        alphabet2.append(alphabet2.pop(0))
    for x in range(len(text)):
        if text[x].isalpha() is False:
            decryption += text[x]
        else:
#             Loop through characters of message. Use position of characters in alphabet2 to decode using alphabet.
            y = alphabet2.index(text[x])
            decryption += alphabet[y]
    alphabet2 = alphabet
    print(f"Here's the decoded result: {decryption}")

print(caeser_cipher_art.logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
if direction == 'encode':
    pass
elif direction == 'decode':
    pass
else:
    raise ValueError("Input must be 'encode' OR 'decode'.") 
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
if direction == 'encode':
    encrypt()
elif direction == 'decode':
    decrypt()
    
restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
if restart == 'yes':
    start()
elif restart == 'no':
    exit()
else:
    raise ValueError("Input must be 'yes' or 'no'.")