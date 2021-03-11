import os
import sys
import time
from encrypter import encrypt
from decrypter import decrypt
from password_generator import generatePassword

class Program:
	def clear():
		os.system("cls")
	
	def quit():
		quit()

	def delay(t = 1):
		time.sleep(t)

	def readLines(database_file):
		lines_database = database_file.readlines()
		line_list = []
		for line in lines_database:
			line_list.append(line.strip("\n"))
		return line_list

	def writeLine(file, line):
		written_line = file.write(line + "\n")
		return written_line

	def display():
		for line in range(len(website_list)):
			print(" website  : {}".format(website_list[line]))
			print(" url      : {}".format(url_list[line]))
			print(" username : {}".format(username_list[line]))
			print(" password : {}".format(decrypt(password_list[line])))
			print()

	def newSlot():
		website_input  = input(" website  : ")
		url_input      = input(" url      : ")
		username_input = input(" username : ")
		password_input = input(" password : ")

		while True:
			confirmation = input("\ncontinue?(Y/N): ").upper()
			if confirmation == "Y":
				Program.writeLine(website_database, website_input)
				Program.writeLine(url_database, url_input)
				Program.writeLine(username_database, username_input)
				if password_input == "/r":
					Program.writeLine(password_database, encrypt(generatePassword()))
				else:
					Program.writeLine(password_database, encrypt(password_input))
				print("action successful.")
				break
			elif confirmation == "N":
				print("action cancelled.")
				break

	def save():
		master_password_database.close()
		username_database.close()
		password_database.close()
		website_database.close()
		url_database.close()


master_password_database = open("master_password_database.txt", "r+")
username_database        = open("username_database.txt", "r+")
password_database        = open("password_database.txt", "r+")
website_database         = open("website_database.txt", "r+")
url_database             = open("url_database.txt", "r+")

username_list   = Program.readLines(username_database)
password_list   = Program.readLines(password_database)
website_list    = Program.readLines(website_database)
url_list        = Program.readLines(url_database)
master_password = Program.readLines(master_password_database)

Program.clear()

while True:
	master_password_input = input("enter master password: ")
	if encrypt(master_password_input) == master_password[0]:
		Program.clear()
		while True:
			user_input = input("h]>>")
			if user_input == "/d":
				Program.clear()
				while True:
					user_input = input("h]d]>>")
					if user_input == "//":
						Program.clear()
						break
					elif user_input == "/d":
						print()
						Program.display()
					elif user_input == "/n":
						Program.newSlot()
					elif user_input == "/c":
						Program.clear()
					elif user_input == "/q":
						Program.save()
						Program.quit()
					else:
						print("invalid input. Try again")
			elif user_input == "/c":
				Program.clear()
			elif user_input == "/q":
				Program.save()
				Program.quit()
			else:
				print("invalid command")
	else:
		Program.quit()