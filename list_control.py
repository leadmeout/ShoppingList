from list_settings import Settings

class ListControl:

	def __init__(self):
		self.settings = Settings()


	def add_new_list(self):
		"""Add a new list to the dictionary of lists"""
		while True:
			
			new_list_name = input("Please enter the new list name or 'q' to quit: ")

			if new_list_name != 'q' or new_list_name != 'quit':
				self.settings.lists.update({new_list_name : []})
				self.settings.save_to_file()	
				prompt = input("Add another list? y/n : ")
				if prompt == 'n' or prompt == 'no':
					break
				elif prompt == 'y' or 'yes':
					continue
			elif new_list_name == 'q' or new_list_name == 'quit':
				break


	def delete_list(self):

		print("")
		self._show_lists_by_number()
		print("")
		

		prompt = input("Enter the number of the list you would like to delete. Enter 'q' to exit: ")

		while True:

			if prompt != 'q' or prompt != 'quit':
				try:
					prompt = int(prompt)
					list_to_delete = list(self.settings.lists.keys())[prompt-1]
				#An except clause may name multiple exceptions as a parenthesized tuple	
				except (ValueError, IndexError):
					print("Please enter a valid list number!\n")
					break
				else:
					del self.settings.lists[list_to_delete]
					print(f"The list {list_to_delete} has been deleted.")
					break


	def rename_list(self):
		
		print("")
		self._show_lists_by_number()
		print("")

		prompt = input("Enter the number of the list you would like to rename. Enter 'q' to exit: ")
		new_name = input("Please enter the new name of the list: ")


		while True:

			if prompt != 'q' or prompt != 'quit':
				try:
					prompt = int(prompt)
					list_to_rename = list(self.settings.lists.keys())[prompt-1]
					print(list_to_rename)
				except ValueError:
					print("Please enter a valid list number!\n")
					break
				else:
					self.settings.lists[new_name] = self.settings.lists.pop(list_to_rename)
					break


	def add_item_to_list(self):
		"""Add one item to the list"""

		print('\nPlease enter an item to add to your list.\n')
		print("Enter 'q' to exit.\n")

		while True:

			new_item = input("Enter item: ")

			if new_item != 'q':
				self.settings.lists[self.active_list].append(new_item).lower()
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

			self._print_current_list()
			print("Enter 'q' to return to the previous menu.\n")
			print("\nWhich item would you like to remove?\n")

			while True:

				item_to_remove = input("Enter item: ")

				if item_to_remove != 'q':
					try:
						self.current_key.remove(item_to_remove.title())
					except ValueError:
						print("This item doesn't exist in your list!\n")
					else:
						print(f"{item_to_remove.title()} was removed from your list.\n")
				else:
					break
		else:
			print("\nYour list is empty; there's nothing to remove!\n")
			