import requests

r = requests.get("http://bme590.suyash.io/list") # get request


r2 = requests.post("http://bme590.suyash.io/student", json={"first_name": "Mackenna", "github_username": "mackenna95", "last_name": "Hill", "netid": "mjh91", "team_name": "OlderThanYou"}) # post request