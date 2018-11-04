import re
import requests
from BeautifulSoup import BeautifulSoup
import json
import os
import urllib2

#https://www.bing.com/search?q=free+clinic+massachusetts&first=21

url = "https://www.bing.com/search?q="
maxResults = 50

def query(searchQuery, firstResult = 1):
	response = requests.get(url+searchQuery+"&first="+str(firstResult))
	results = beautify(response.text)
	return results

def beautify(results):
	resultsList = []
	resultsPretty = BeautifulSoup(results)
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
			



if __name__ == "__main__":
	print(query("test"))

