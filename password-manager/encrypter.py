# message encrypter

# import pyperclip
from encryption_dict_file import *

def encrypt(message):
	encrypted_word = ""
	char_list = list(message)
	for char in char_list:
		conv_char = conv_dict[char]
		encrypted_word += conv_char
	return encrypted_word

# print("[Enter your message to encrypt]: ")
# word = input(">>")
# encrypted_word = encrypt(word)
# print("\n[Encrypted]: ")
# print(encrypted_word)
# pyperclip.copy(encrypted_word)
# print("\ncopied to clipboard!")