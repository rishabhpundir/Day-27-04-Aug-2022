import requests

response = requests.get('http://127.0.0.1:8000/api/event_api/19')
print(response.json()['event_name'])