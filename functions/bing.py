import re
import requests
from bs4 import BeautifulSoup as bs 
import json
import os
import urllib.request as urllib2
import time

#https://www.bing.com/search?q=free+clinic+massachusetts&first=21


def query(searchQuery, firstResult = 1):
    url = "https://www.bing.com/search?q="
    response = requests.get(url+searchQuery+"&first="+str(firstResult))
    results = beautify(response.text)
    return results

def beautify(results):
    resultsList = []
    resultsPretty = bs(results)
    for oltag in resultsPretty.findAll('ol', {'id': re.compile('b_results')}):
        try:
            for litag in oltag.findAll('li'):
                cleanUrl = urllib2.unquote(litag.a['href'])
                siteDetails = litag.a.text
                siteDescription = litag.p.text
                resultObj = {"url":cleanUrl, "description":siteDescription, "details":siteDetails, "answer":litag.text}
                resultsList.append(resultObj)
        except:
            continue
    return resultsList
			
def writeDb(filename, results):
    db = open(filename,"w+")
    jsonResults = json.dumps(results)
    db.write(jsonResults)



if __name__ == "__main__":
    maxCount = 20 
    results = [{"url":"","description":"","details":"","answer":""}]
    progress = 1
    cont = True
    for i in range(1,maxCount,10):
        try:
            bingAnswer = query("free+clinic+massachusetts",firstResult=i)
        except Exception as e:
            print(e) 
            break
        for answer in bingAnswer:
            cont = True
            for result in results:
                if answer["url"] in result["url"]:
                    print("Got a dupe, waiting for a bit for bing to forive me.")
                    time.sleep(2)
                    cont = False
                    break
            if cont:
                print(results)
                results.append(answer)
        print(i)
        time.sleep(1)
    print(results)
    print(len(results))
    writeDb("db/bing.json", results)
