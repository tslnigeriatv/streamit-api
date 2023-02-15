import requests

headers = {"Content-Type": "application/json"}

response = requests.request("GET", "​http://localhost:8000/api/profile/")

# print(response)