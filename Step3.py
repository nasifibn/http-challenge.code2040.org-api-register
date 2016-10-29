import requests

import json

token = "83d9b617120d0299bc0e0c3ef0397752"
firstEndpoint = "http://challenge.code2040.org/api/haystack"
secondEndpoint = "http://challenge.code2040.org/api/haystack/validate"

find = requests.post(firstEndpoint, data={'token': token})

getString = json.loads(find.text)

needle = getString['needle']
haystack = getString['haystack']


for i in range(0, len(haystack)):

    if haystack[i] == needle:
        temp = i

found = requests.post(secondEndpoint, data={'token': token, 'needle': temp})

print(found.text)