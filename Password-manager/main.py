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
		def copy(x, data):
			pyperclip.copy(x)
			print(data + " copied to clipboard.")

        # Hashes the password with SHA512
		def hash(password):
			result = hashlib.sha512(password.encode())
			hashed_password = result.hexdigest()
			return hashed_password

		# Generates a random password
		def generatePassword(length = 30):
			random_string = generatePassword(length)
			return random_string

		# Salts the input "x" and stores the salt in a file
		def salt(x):
			random_string = Program.generatePassword(5)
			salt_file = open("salt.txt", "w")
			salt_file.write(random_string) # < Stores the salt in a .txt file
			salt_file.close()
			salted_pass = (x + random_string)
			return salted_pass

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
			print(" [type 'help' for help]")

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
				if len(password) >= 15:
					return True

		# Checking if the 2 lines of the .txt file is "\n"
		def masterPasswordIsEmpty(master_password):
			if master_password[0] == "":
				return True
			return False

		# This method asks the user to specify the slot they want
		def specify():
			# Makes the search easier
			website_upper_list = [Program.decrypt(web, key_dict).upper() for web in website_list]
			username_upper_list = [Program.decrypt(username, key_dict).upper() for username in username_list]

			# Asks for the data
			while True:
				website_input = input("website name: ").upper()	
				username_input = input("username for the website: ").upper()
				index = website_upper_list.index(website_input)
				if website_input not in website_upper_list or username_upper_list[index] != username_input:
					print("username or website not listed")
					confirmation = input("retry?(Y/N): ").upper()
					if confirmation == "Y":
						continue
					elif confirmation == "N":
						program(True)
				elif website_input in website_upper_list and username_upper_list[index] == username_input:
					return index

		# The user can copy the data
		def copyData():
			index = Program.specify()
			
			# The user can copy any aspect of the specified data
			while True:
				copy_input = input(" copy: ")
				if copy_input == "website":
					Program.copy(Program.decrypt(website_list[index], key_dict), "website name")
					break
				elif copy_input == "username":
					Program.copy(Program.decrypt(username_list[index],  key_dict), "username")
					break
				elif copy_input == "url":
					Program.copy(Program.decrypt(url_list[index], key_dict), "url")
					break
				elif copy_input == "password":
					Program.copy(Program.decrypt(password[index], key_dict), "password")
					break
				elif copy_input == "clear" or "cls":
					Program.clear()
				elif copy_input == "back":
					break
				elif copy_input == "quit":
					Program.quit()

		# This method deletes the saved slot's data by specifying
		def deleteData():
			index = Program.specify()

			print()
			Program.display("single", index) # < Displays a specific info

			while True:
				delete_input = input(" delete?(Y/N): ").upper()
				if delete_input == "Y":

					# Deletes the element of the specified info by their index
					website_list.pop(index)
					url_list.pop(index)
					username_list.pop(index)
					password_list.pop(index)

					# Overwrites the existing list with the new popped list
					with open("website_database.txt", "w") as w:
						for web in website_list:
							w.write(web + "\n")
					with open("url_database.txt", "w") as u:
						for url in url_list:
							u.write(url + "\n")
					with open("username_database.txt", "w") as user:
						for username in website_list:
							user.write(username + "\n")
					with open("password_database.txt", "w") as p:
						for password in password_list:
							p.write(password + "\n")

					# Changes the mode from "w" to "r+" to avoid accidental overwriting
					master_password_database = open("master_password_database.txt", "r+")
					username_database        = open("username_database.txt", "r+")
					password_database        = open("password_database.txt", "r+")
					website_database         = open("website_database.txt", "r+")
					url_database             = open("url_database.txt", "r+")
					break
				elif delete_input == "N":
					break

		# Displays the commands to the user
		def info():
			print()
			print(" +----------+")
			print(" | commands |")
			print(" +----------+-----------------------------------+")
			print(" |  >'display' = displays your saved passwords  |")
			print(" |  >'new' = makes a new password               |")
			print(" |   +>'random' = generates a random password   |")
			print(" |  >'copy' = copies the specified info         |")
			print(" |   +>'website' = copies the website name      |")
			print(" |   +>'url' = copies the url                   |")
			print(" |   +>'username' = copies the username         |")
			print(" |   +>'password' = copies the password         |")
			print(" |   +>'back'= goes back a page                 |")
			print(" |  >'delete; = deletes the specified info      |")
			print(" |  >'quit' = ends the program                  |")
			print(" |  >'clear' = clears the screen                |")
			print(" +----------------------------------------------+")
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
						salted_password = Program.salt(input_make_password)
						master_password_database.write((Program.hash(salted_password)) + "\n") # Encrypts the password
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
		def display(mode, line = None):
			if mode == "loop":
				for line in range(len(website_list)):
					# Decrypts the encrypted password
					print(" website  : {}".format(Program.decrypt(website_list[line], key_dict)))
					print(" url      : {}".format(Program.decrypt(url_list[line], key_dict)))
					print(" username : {}".format(Program.decrypt(username_list[line], key_dict)))
					print(" password : {}".format(Program.decrypt(password_list[line], key_dict)))
					print()
			elif mode == "single":
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
					if password_input == "random":
						password = Program.generatePassword()
						Program.writeLine(password_database, password, key_dict)
					else:
						password = password_input
						Program.writeLine(password_database, password, key_dict)
					Program.copy(password, "password")
					print("action successful.\n")
					input("return to continue: ")
					Program.save() # < Saves the new info
					Program.restart(True) # < Goes straight into the program again without having to re-enter the password
					break
				elif confirmation == "N":
					print("action cancelled.\n")
					break
	

	# The main program
	def main():
		Program.infoHelp()
		while True:
			user_input = input(">>").lower()
			if user_input == "display":
				print()
				Program.display("loop")
			elif user_input == "new":
				Program.newSlot()
			elif user_input == "help":
				Program.info()
			elif user_input == "copy":
				Program.copyData()
			elif user_input == "delete":
				Program.deleteData()
			elif (user_input == "clear") or (user_input == "cls"):
				Program.clear()
				Program.infoHelp()
			elif user_input == "quit":
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

	# Reads the lines
	username_list   = Program.readLines(username_database)
	password_list   = Program.readLines(password_database)
	website_list    = Program.readLines(website_database)
	url_list        = Program.readLines(url_database)
	master_password = Program.readLines(master_password_database)

	Program.clear()

	# If there is no master password/if its a new account, then we call the makeMasterPassword() method
	if Program.masterPasswordIsEmpty(master_password):
		Program.makeMasterPassword()
	# Loads/unpickles the encryption key when they're a returnin user
	elif not Program.masterPasswordIsEmpty(master_password):
		global key_dict
		key_dict = Program.openEncKey()

	# Checks whether the user is starting the program or is in the program but just want to restart it
	if not in_program:
		while True:
			master_password_input = input("enter master password: ")
			with open("salt.txt", "r") as salt_database: # < Opens the "salt.txt" file
				salt = Program.readLines(salt_database)  # < Assings the salt list of the file to the variable salt
			if Program.hash(master_password_input + salt[0]) == master_password[0]:
				Program.clear()
				main()
			else:
				Program.quit()
	elif in_program:
		main()

program(False) # < Calls the function and says that the user is starting it
