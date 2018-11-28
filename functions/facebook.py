import requests
import json
import re
import os
import sys
from time import sleep
#https://graph.facebook.com/search?type=place&fields=[%22about%22,%22link%22,%22phone%22,%22location%22,%22description%22]&center=42.1878631,-72.0148115&distance=1600000&categories=[%22MEDICAL_HEALTH%22]&access_token=<appid|secret>

fbId = os.environ["FACEBOOK_APP_ID"]
fbSecret = os.environ["FACEBOOK_APP_SECRET"]

def query(url = "", uri = "", nextUrl = "", distance = 320000, center ="42.1878631,-72.0148115"):
    if not url:
        url = "https://graph.facebook.com/"
    if not uri:
        uri = "search?type=place&fields=['about','link','phone','location','description','WebSite']&center="\
            +center+"&distance="\
            +str(distance)+"&categories=['MEDICAL_HEALTH']&access_token="\
            +fbId+"|"\
            +fbSecret
    if not nextUrl:
        response = requests.get(url+uri)
    if nextUrl:
        response = requests.get(nextUrl)
    jsonResponse = json.loads(response.text)
    return jsonResponse

def writeDb(filename, results):
    db = open(filename,"w+")
    jsonResults = json.dumps(results)
    db.write(jsonResults)
    
if __name__=="__main__":
    results = {"nextUrl":"","results":[],"exception":""}
    nextUrl = ""
    result = query()
    for item in result["data"]:
        results["results"].append(item)
    try:
        while result["paging"]["next"]:
            sleep(1)
            result = query(nextUrl = nextUrl)
            nextUrl = result["paging"]["next"]
            for item in result["data"]:
                results["results"].append(item)
            print(nextUrl+"\n")
    except:
        results["exception"] = str(sys.exc_info()[0])
        writeDb("db/facebook.json",results)
        print(sys.exc_info()[0])

    writeDb("db/facebook.json",results)
