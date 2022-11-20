import requests

param = {
    "amount": 10,
    "type": "boolean",
    "category": 18,
}
response = requests.get(url='https://opentdb.com/api.php', params=param)
response.raise_for_status()
data = response.json()['results']
# questions = {item['question']: item['correct_answer'] for item in data}
