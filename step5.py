import requests
import datetime
import json

token = "83d9b617120d0299bc0e0c3ef0397752"
firstEndpoint = "http://challenge.code2040.org/api/dating"
secondEndpoint = "http://challenge.code2040.org/api/dating/validate"


getData = requests.post(firstEndpoint, data={"token": token})

getDate = json.loads(getData.text)

holdStamp = getDate["datestamp"]

stampArray = holdStamp.split("T")

timeAdded = getDate["interval"]

date = stampArray[0]

time = stampArray[1]

time = time.split("Z")[0]

holdStamp2 = date + " " + time


normalDate = datetime.datetime.strptime(holdStamp2, '%Y-%m-%d %H:%M:%S')

changedDate =  normalDate+ datetime.timedelta(seconds=timeAdded)

changedDate = changedDate.strftime('%Y-%m-%d %H:%M:%S')

changedDate = changedDate.split(" ")

finishedDate = changedDate[0] + "T" + changedDate[1] + "Z"

finished = requests.post(secondEndpoint, data={"token": token, "datestamp": finishedDate})

print(finished.text)
