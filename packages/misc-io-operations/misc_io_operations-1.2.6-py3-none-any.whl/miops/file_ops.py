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