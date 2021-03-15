import random
from random import choices

def generatePassword(length = 30):
	chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890`~!@#$%^&*()-_=+[]|;:',<.>/?"
	#Exceptions = \ " { }

	password = ""
	for times in range(int(length)):
		char = random.choice(chars)
		password += char
	return password