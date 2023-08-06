import random


def get_randint(first_input: int, second_input: int) -> int:
	return random.randint(first_input, second_input)


def sort_list(i_list: list, reverse: bool = False) -> list:
	return sorted(i_list, reverse=reverse)


def shuffle_list(i_list: list) -> list:
	random.shuffle(i_list)
	return i_list