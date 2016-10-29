import requests

token = "8e9b4ca6f16475b8662f51c070d4403d"
firstEndpoint = "http://challenge.code2040.org/api/reverse"
secondEndpoint = "http://challenge.code2040.org/api/reverse/validate"


def reverse(string):
    first = 0
    last = len(string) - 1
    stringArray = [i for i in string]
    while first < last:
        temp = stringArray[first]
        stringArray[first] = stringArray[last]
        stringArray[last] = temp
        first += 1
        last -= 1
        s = ''
    return s.join(stringArray)


getString = requests.post(firstEndpoint, data={'token': token})

result = getString.text

reverse = reverse(result)

answer = requests.post(secondEndpoint, data={'token': token, 'string': reverse})

print(answer.text)
