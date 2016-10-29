import requests

import json

token = '83d9b617120d0299bc0e0c3ef0397752'
firstEndpoint = 'http://challenge.code2040.org/api/prefix'
secondEndpoint = 'http://challenge.code2040.org/api/prefix/validate'

getDict = requests.post(firstEndpoint, data={'token': token})

readWords = json.loads(getDict.text)

arr = readWords['array']
prefix = readWords['prefix']

notInDict = []
inDict = {}

for i in range(0, len(arr)):

    if (arr[i].startswith(prefix) == False):
        notInDict.append(arr[i])

inDict['token'] = token

inDict['array'] = notInDict

results = requests.post(secondEndpoint, json= inDict)

print(results.text)
