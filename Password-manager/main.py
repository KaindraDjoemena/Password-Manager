# Importing all the modules
import os
import time
import hashlib
import pickle
import pyperclip
from cryptography import Crypto
from password_generator import generatePassword

crypto = Crypto() # < Initializing an object "crypto" from the class "Crypto()"

# The program function
def program(in_program):

	# Program class
	class Program:

		# Clears the window
		def clear():
			os.system("cls")

		# Quits the program	
		def quit():
			quit()

		# Delays a command
		def delay(t = 1):
			time.sleep(t)

		# Copies x
		def copy(x):
			pyperclip.copy(x)

        # Hashes the password with SHA512
		def hash(password):
			result = hashlib.sha512(password.encode())
			hashed_password = result.hexdigest()
			return hashed_password

		# Makes the encryption key and pickles it
		def makeKey():
			key = crypto.makeKey()
			key_file = open("key_file.pickle", "wb")
			pickle.dump(key, key_file)
			key_file.close()

		# Opens the encrypted key
		def openEncKey():
			key_file = open("key_file.pickle", "rb")
			key_dict = pickle.load(key_file)
			return key_dict

		# Encrypts the data
		def encrypt(x, key_file):
			encrypted = crypto.encrypt(x, key_file)
			return encrypted

		# Decrypts the encrypted data
		def decrypt(x, key_file):
			decrypted = crypto.decrypt(x, key_file)
			return decrypted

		# Restarts the program
		def restart(user_state):
			program(user_state)

		# Tells the user that by tying "/i" will display all the commands
		def infoHelp():
			print(" [type '/i' for help]")

		# Reads a line of a file
		def readLines(database_file):
			lines_database = database_file.readlines()
			line_list = []
			for line in lines_database:
				line_list.append(line.strip("\n"))
			return line_list

		# Checking if the newly made password is valid or not
		def passwordIsValid(password, confirmation):
			if password == confirmation:
				if len(password) >= 10:
					return True

		# Checking if the 2 lines of the .txt file is "\n"
		def masterPasswordIsEmpty(master_password):
			if master_password[0] == "":
				return True
			return False

		# Displays the commands to the user
		def info():
			print()
			print(" +----------+")
			print(" | commands |")
			print(" +----------+----------------------------+")
			print(" |  /d = displays your saved passwords   |")
			print(" |  /n = makes a new password            |")
			print(" |    /r = generates a random password   |")
			print(" |  /q = ends the program                |")
			print(" |  /c = clears the screen               |")
			print(" +---------------------------------------+")
			print()

		# Making a master password
		def makeMasterPassword():
			print("  lets get started")
			input("\nreturn key to continue: ")
			Program.clear()
			while True:
				print("  make a unique and memorizable password")
				print("  the password should be more than 10 characters long")
				print("password:")
				input_make_password = input(">>")
				print("confirmation:")
				input_confirmation_password = input(">>")
				while True:
					input_continue = input("continue?(Y/N): ").upper()
					if (input_continue == "N") or (input_continue == "Y"):
						break
					print("invalid input.")
				if (input_continue == "Y"):
					if (Program.passwordIsValid(input_make_password, input_confirmation_password)):
						# Overwrites the database with ""
						master_password_database = open("master_password_database.txt", "w")
						username_database        = open("username_database.txt", "w")
						password_database        = open("password_database.txt", "w")
						website_database         = open("website_database.txt", "w")
						url_database             = open("url_database.txt", "w")
						master_password_database.write((Program.hash(input_make_password)) + "\n") # Encrypts the password
						print("welcome")
						input("\nreturn key to continue: ")
						Program.makeKey()
						Program.quit()
					else:
						Program.clear()
						print("invalid password.")
				elif (input_continue == "N"):
					Program.quit()


		# Writes a line to a file
		def writeLine(file, line, key_dict):
			written_line = file.write(Program.encrypt(line, key_dict) + "\n")

		# Displays all of the slots/info
		def display():
			for line in range(len(website_list)):
				# Decrypts the encrypted password
				print(" website  : {}".format(Program.decrypt(website_list[line], key_dict)))
				print(" url      : {}".format(Program.decrypt(url_list[line], key_dict)))
				print(" username : {}".format(Program.decrypt(username_list[line], key_dict)))
				print(" password : {}".format(Program.decrypt(password_list[line], key_dict)))
				print()

		# Saves/closes the file to save it
		def save():
			master_password_database.close()
			username_database.close()
			password_database.close()
			website_database.close()
			url_database.close()

		# Makes a new slot
		def newSlot():
			website_input  = input(" website  : ")
			url_input      = input(" url      : ")
			username_input = input(" username : ")
			password_input = input(" password : ")

			while True:
				# The program will write the input if the user chooses to and restarts the program
				confirmation = input("\ncontinue?(Y/N): ").upper()
				if confirmation == "Y":
					key_file = open("key_file.pickle", "rb")
					key_dict = pickle.load(key_file)
					Program.writeLine(website_database, website_input, key_dict)
					Program.writeLine(url_database, url_input, key_dict)
					Program.writeLine(username_database, username_input, key_dict)
					if password_input == "/r":
						Program.writeLine(password_database, generatePassword(), key_dict)
					else:
						Program.writeLine(password_database, password_input, key_dict)
					print("action successful.")
					print("password copied to clipboard")
					input("return to continue: ")
					Program.save() # < Saves the new info
					Program.restart(True) # < Goes straight into the program again without having to re-enter the password
					break
				elif confirmation == "N":
					print("action cancelled.")
					break
	
	# Makes key_dict global
	global key_dict
	key_dict = Program.openEncKey()

	# The main program
	def main():
		Program.infoHelp()
		while True:
				user_input = input(">>")
				if user_input == "/d":
					print()
					Program.display()
				elif user_input == "/n":
					Program.newSlot()
				elif user_input == "/i":
					Program.info()
				elif user_input == "/c":
					Program.clear()
					Program.infoHelp()
				elif user_input == "/q":
					Program.save()
					Program.quit()
				else:
					print("invalid command")


	# Opens the files
	master_password_database = open("master_password_database.txt", "r+")
	username_database        = open("username_database.txt", "r+")
	password_database        = open("password_database.txt", "r+")
	website_database         = open("website_database.txt", "r+")
	url_database             = open("url_database.txt", "r+")

	# Read the lines
	username_list   = Program.readLines(username_database)
	password_list   = Program.readLines(password_database)
	website_list    = Program.readLines(website_database)
	url_list        = Program.readLines(url_database)
	master_password = Program.readLines(master_password_database)

	Program.clear()

	# If there is no master password/if its a new account, then we call the makeMasterPassword() method
	if Program.masterPasswordIsEmpty(master_password):
		Program.makeMasterPassword()

	# Checks whether the user is starting the program or is in the program but just want to restart it
	if not in_program:
		while True:
			master_password_input = input("enter master password: ")
			if Program.hash(master_password_input) == master_password[0]:
				Program.clear()
				main()
			else:
				Program.quit()
	elif in_program:
		main()

# Calls the function and says that the user is starting it
program(False)