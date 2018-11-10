import json

report = open("facebook.json","r+")
rawReport = report.read()

jsonReport = json.loads(rawReport)

for result in jsonReport["results"]:
    print(result["link"])

print("I found "+str(len(jsonReport["results"]))+" websites on facebook")
