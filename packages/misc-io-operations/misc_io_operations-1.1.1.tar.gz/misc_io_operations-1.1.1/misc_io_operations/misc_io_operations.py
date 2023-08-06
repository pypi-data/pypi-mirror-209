import random
import requests
import json


def get_cint(prompt: str) -> int:
	try:
		return int(input(prompt))
	except ValueError:
		print("You did not type in the correct type of input.\nYou have to type in an integer.")


def get_randint(first_input: int, second_input: int) -> int:
	return random.randint(first_input, second_input)


def sort_list(i_list: list, reverse: bool = False) -> list:
	return sorted(i_list, reverse=reverse)


def shuffle_list(i_list: list) -> list:
	random.shuffle(i_list)
	return i_list


def get_url_data(url: str):
	try:
		response = requests.get(url)
	except:
		exit("Enter a proper and correct url")

	try:
		json.dumps(response.json(), indent=2)
		return response.json
	except:
		return response.text


def read_sorted_file(filename : str) -> list:
	with open(filename) as file:
		return sorted(file)


def find_data(filename : str, keyword : str) -> tuple(str, bool):
	with open(filename) as file:
		for i in file:
			if i == keyword:
				return i, True
			return False


def check_limit(filename : str, limit : str) -> bool:
	for_iter = 0
	with open(filename) as file:
		for _ in file:
			for_iter += 1
	if for_iter >= limit:
		return True
	return False