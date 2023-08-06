import requests
import json


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