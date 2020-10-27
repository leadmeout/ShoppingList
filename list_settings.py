import sys
import json

class Settings:
	"""A class to control the opening and closing of the lists file for the MyList class"""
	"""This class will also hold the dictionary containing the lists for MyList"""

	def __init__(self):

		self.filename = 'lists_save_file.json'
		self.user_information_file = 'user_information.json'
		self.username = ''
		self.lists = {}
		
		
	def _file_check_username(self):
		"""
			Check if a username already exists.
			If not, ask for a username and save it.
		"""

		try:
			with open(self.user_information_file) as f:
				self.username = json.load(f)
		except FileNotFoundError:
			self.username = input("Welcome! What is your name: ")
			with open(self.user_information_file, 'w') as f:
				json.dump(self.username.title(), f)
				print(f"\nHi, {self.username.title()}!")
		else:
			print(f"\nWelcome back, {self.username}!\n")


	def _file_check_lists(self):
		"""Check if a list file already exists. If not, create a new one and add some lists"""

		try:
			with open(self.filename) as f:
				self.lists = json.load(f)
		except FileNotFoundError:
			self.lists = {
				'groceries' : [],
				'to-do' : [],
				'favourite movies' : [],
			}
			with open(self.filename, 'w') as f:
				json.dump(self.lists, f)
			print("We've created some lists for you to get started!\n")
		else:
			with open(self.filename) as f:
				self.lists = json.load(f)


	def save_to_file(self):
		"""Save lists to a json file"""

		with open(self.filename, 'w') as f:
			json.dump(self.lists, f)