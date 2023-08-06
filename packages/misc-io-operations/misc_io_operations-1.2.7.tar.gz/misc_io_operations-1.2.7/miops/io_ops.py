def get_cint(prompt: str) -> int:
	try:
		return int(input(prompt))
	except ValueError:
		print("You did not type in the correct type of input.\nYou have to type in an integer.")