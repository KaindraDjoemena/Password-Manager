from encryption_dict_file import *

def encrypt(message):
	encrypted_word = ""
	char_list = list(message)
	for char in char_list:
		conv_char = conv_dict[char]
		encrypted_word += conv_char
	return encrypted_word
