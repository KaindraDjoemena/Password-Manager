from encryption_dict_file import *

def decrypt(enc):
	decrypted_message = ""
	seperated_enc_char = [enc[i:i+2] for i in range(0, len(enc), 2)]
	for enc_char in seperated_enc_char:
		for letter, value in conv_dict.items():
			if enc_char == value:
				decrypted_message += letter
	return decrypted_message
