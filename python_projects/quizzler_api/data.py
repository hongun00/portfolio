import requests
data = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
questions = data.json()["results"]







question_data = questions