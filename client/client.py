import requests

url = "https://web-production-93c3.up.railway.app/oauth/convert-token/"

payload = {
    "query": "{\"client_id\":\"ceDPTrU2KFFiisy3xwLYxw0kMH9fCZTfU1uPJTq2\",\"client_secret\":\"VdrBI0PKl990YADF5CA9QypWeOoS0tPWoXqTX6B06jM4Vwguz5IJVSQuNseruo1LuKNKltRqWAypFNim020dXF9QMKj08gv2BiDrBlkjrwJ1NquQhkHY9atOMjFaRJsv\", \"backend\":\"google-oauth2\", \"token\":\"039516402443-522feng3uud7h8gvc936133biv5s4k61.apps.googleusercontent.com\", \"grant_type\":\"convert_token\"}",
    "variables": {}
}
headers = {"Content-Type": "application/json"}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)