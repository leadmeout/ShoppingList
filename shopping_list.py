import sys



class ShoppingList:

	def __init__(self):

		self.date_file = 'groceries.json'

		self.lists = {
			'groceries' : [],
			'appliances' : [],
			'car' : [],
		}

		self.groceries = []
		#set the first key to be the active list by default
		self.active_list = next(iter(self.lists))
		#Capitalize the list name for output to the console
		self.display_active_list = self.active_list.title()
		#Set the key making changes to the current list
		self.current_key = self.lists[self.active_list]
	

	def change_active_list(self):
		"""Set active list to work with"""
		print("\nWhich list should be your active list?\n")

		#Convert dictionary keys into list and access them by key
		for i in range(0, len(self.lists)):
			print(f"\t{i+1} : {list(self.lists.keys())[i].title()}")

		print('\n')

		prompt = int(input("Please enter the number of the list: "))
		
		try:
			self.active_list = list(self.lists.keys())[prompt-1]
		except ValueError:
			print("Please enter a valid list number!\n")
		else:
			self.display_active_list = self.active_list.title()
			self.current_key = self.lists[self.active_list] 
			print(f"Your active list has been changed to {self.display_active_list}.\n")

		
	def add_new_list(self):
		"""Add a new list to the dictionary of lists"""
		pass	

	def delete_list(self):
		pass

	def rename_list(self):
		pass


	def add_item_to_list(self):
		"""Add one item to the list"""

		print('\nPlease enter an item to add to your shopping list.\n')
		print("Enter 'q' to exit.\n")

		while True:

			new_item = input("Enter item: ")

			if new_item != 'q':
				self.lists[self.active_list].append(new_item.title())
				#groceries.append(new_item.title())
				print(f"{new_item.title()} added!\n")
			else:
				break


	def clear_list(self):
		"""Remove all items from the list"""

		if self._check_if_list_empty():

			while True:

				print("Would you like to delete the entire list?")
				prompt = input("Enter 'y' for yes or 'n' for no: ")
				print(" ")

				if prompt == 'y' or prompt == 'yes':
					self.current_key.clear()
					print("The list has been cleared!\n")
					break
				elif prompt == 'n' or prompt == 'no':
					print("The list was not cleared.\n")
					break
				else:
					print("Please enter a valid command!\n")
		else:
			print("\nThe list is already empty!\n")


	def remove_item_from_list(self):
		"""Remove one item from the list"""

		if self._check_if_list_empty():	

			self.print_current_list()
			print("Enter 'q' to return to the previous menu.\n")
			print("\nWhich item would you like to remove?\n")

			while True:

				item_to_remove = input("Enter item: ")

				if item_to_remove != 'q':
					try:
						self.current_key.remove(item_to_remove.title())
					except ValueError:
						print("This item doesn't exist in your shopping list!\n")
					else:
						print(f"{item_to_remove.title()} was removed from your list.\n")
				else:
					break

		else:
			print("\nYour list is empty; there's nothing to remove!\n")
			


	def _check_if_list_empty(self):
		"""Check if list is empty or not"""

		if self.current_key:
			return True
		else:
			return False


	def print_current_list(self):
		"""Output the current contents of the list"""

		if len(self.current_key) == 0:
			print("\nYour list is currently empty!")
		else:
			print("\nYour list so far: \n")
			for item in self.current_key:
				print(f"\t- {item}")

		print(' ')


	def display_menu(self):
		"""
			Starting point for program
			Display a menu with choices
		"""

		print("\nWelcome to your shopping list assistant!\n")

		while True:
			print("Active List: " + self.display_active_list)
			self.print_current_list()

			menu = {
				'1' : "Change the active list",
				's' : "Show current items",
				'a' : "Add an item to the list",
				'd' : "Remove an item from the list",
				'c' : "Delete the entire list",
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
				elif prompt == 's':
					self.print_current_list()
				elif prompt == 'a':
					self.add_item_to_list()
				elif prompt == 'd':
					self.remove_item_from_list()
				elif prompt == 'c':
					self.clear_list()
				elif prompt == 'q':
					break
				else:
					print("Please enter a valid command!")


if __name__ == '__main__':
	s = ShoppingList()
	s.display_menu()

