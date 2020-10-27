from list_settings import Settings
from list_control import ListControl

class MyList:
	"""A class for multiple lists through which you can navigate"""
	def __init__(self):

		self.settings = Settings()
		self.control = ListControl()

		#set the first key to be the active list by default
		self.active_list = next(iter(self.settings.lists))
		#Capitalize the list name for output to the console
		self.display_active_list = self.active_list.title()
		#Set the key in the dictionary to which changes should be made
		self.current_key = self.settings.lists[self.active_list]


	def _check_if_list_empty(self):
		"""Helper method to check if a list is empty or not"""

		if self.current_key:
			return True
		else:
			return False


	def _show_lists_by_number(self):
		"""Convert dictionary keys into list and access them by key"""
		print('')
		
		for i in range(0, len(self.settings.lists)):
			print(f"\t{i+1} : {list(self.settings.lists.keys())[i].title()}")

		print('')


	def _print_current_list(self):
		"""Output the current contents of the list"""

		if len(self.current_key) == 0:
			print("\n\tYour list is currently empty!")
		else:
			print("\nYour list so far: \n")
			for item in self.current_key:
				print(f"\t- {item}")

		print('')


	def change_active_list(self):
		"""Set active list to work with"""
		print("\nWhich list should be your active list?")
		print("Type in 'q' to go back.\n")

		self._show_lists_by_number()

		print('')

		prompt = input("Please enter the number of the list: ")

		while True:
			if prompt != 'q' or prompt != 'quit':		
				try:
					prompt = int(prompt)
					self.active_list = list(self.settings.lists.keys())[prompt-1]
				except ValueError:
					print("Please enter a valid list number!\n")
					break
				else:
					self.display_active_list = self.active_list.title()
					self.current_key = self.settings.lists[self.active_list] 
					print(f"Your active list has been changed to {self.display_active_list}.\n")
					break
			else:
				break


	def run_program(self):
		"""
			Starting point for program
			Display a menu with choices
		"""

		while True:
			print(f"Active List: {self.display_active_list}\n")

			menu = {
				'1' : "Change the active list",
				'2' : "Show current lists",
				's' : "Show current items",
				'a' : "Add an item to the list",
				'd' : "Remove an item from the list",
				'c' : "Delete the contents of the active list",
				'n' : "Create a new list",
				'r' : "Rename a list",
				'x' : "Delete an entire list",
				'q' : "Quit",
			}

			for key, value in menu.items():
				print(f"\t'{key}' : {value}")

			prompt = input("\nPlease enter your choice: ")

			try:
				prompt in menu.keys()
			except:
				print("Please enter a valid command!")
			else:
				if prompt == '1':
					self.change_active_list()
				elif prompt == '2':
					self._show_lists_by_number()
				elif prompt == 's':
					self._print_current_list()
				elif prompt == 'a':
					self.control.add_item_to_list()
				elif prompt == 'd':
					self.control.remove_item_from_list()
				elif prompt == 'n':
					self.control.add_new_list()
				elif prompt == 'r':
					self.control.rename_list()
				elif prompt == 'c':
					self.control.clear_list()
				elif prompt == 'x':
					self.control.delete_list()
				elif prompt == 'q':
					self.settings.save_to_file()
					print("Your changes have been saved for the next time you come back!")
					break
				else:
					print("Please enter a valid command!")


if __name__ == '__main__':
	m = MyList()
	m.run_program()

