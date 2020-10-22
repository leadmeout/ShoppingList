import sys

filename = 'groceries.json'
groceries = []

def add_item_to_list():

	print('\nPlease enter an item to add to your shopping list.\n')
	print("Enter 'q' to exit.\n")

	while True:

		new_item = input("Enter item: ")

		if new_item != 'q':
			groceries.append(new_item.title())
			print(f"{new_item.title()} added!\n")
		else:
			break

	print_current_list()


def clear_list():

	print("Would you like to delete the entire list?")
	prompt = input("Enter 'y' for yes or 'n' for no: ")
	print(" ")

	while True:
		if prompt == 'y' or prompt == 'yes':
			groceries.clear()
			print("The list has been cleared!\n")
		elif prompt == 'n' or prompt == 'no':
			break


def remove_item_from_list():

	#_check_if_list_empty()
	if _check_if_list_empty():	

		print_current_list()
		print("Enter 'q' to return to the previous menu.\n")
		print("\nWhich item would you like to remove?\n")

		while True:

			item_to_remove = input("Enter item: ")

			if item_to_remove != 'q':
				try:
					groceries.remove(item_to_remove.title())
					#item_to_remove in groceries
				except ValueError:
					print("This item doesn't exist in your shopping list!\n")
				else:
					print(f"{item_to_remove} has been removed from your list.\n")
			else:
				break

	else:
		print("\nYour list is empty; there's nothing to remove!\n")
		


def _check_if_list_empty():

	if groceries:
		return True
	else:
		return False


def print_current_list():

	if len(groceries) == 0:
		print("\nYour list is currently empty!\n")
	else:
		print("\nYour list so far: \n")
		for item in groceries:
			print(f"\t- {item}")

	print(' ')

def display_menu():

	print("\nWelcome to your shopping list assistant!\n")
	print("What would you like to do?\n")

	while True:

		menu = {
			's' : "Show current items",
			'a' : "Add an item to the list",
			'd' : "Remove an item from the list",
			'c' : "Delete the entire list",
			'q' : "Quit",
		}

		for key, value in menu.items():
			print(f" '{key}' : {value}")

		prompt = input("\nPlease enter your choice: \n")

		try:
			prompt in menu.keys()
		except:
			print("Please enter a valid command!")
		else:
			if prompt == 's':
				print_current_list()
			elif prompt == 'a':
				add_item_to_list()
			elif prompt == 'd':
				remove_item_from_list()
			elif prompt == 'c':
				clear_list()
			elif prompt == 'q':
				break
			else:
				print("Please enter a valid command!")


display_menu()

