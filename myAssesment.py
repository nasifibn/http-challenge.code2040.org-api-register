import requests


registration = "http://challenge.code2040.org/api/register"
token = "8e9b4ca6f16475b8662f51c070d4403d"
gitHub = "https://github.com/nasifibn/http-challenge.code2040.org-api-register.git"

MakeItHappen = requests.post(registration, data = {"token":token, "github":gitHub})

print(MakeItHappen.text)

