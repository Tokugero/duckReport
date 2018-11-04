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
		for litag in oltag.findAll('li'):
			print(urllib2.unquote(litag.a['href']))
			print(litag.a.text)



if __name__ == "__main__":
	query("test")




#def beautify(results):
#        resultsList = []
#        resultsPretty = BeautifulSoup(results)
##        topics = resultsPretty.findAll('div',{'id':'links'})[0]
#        answers = topics.findAll('div',{'class': re.compile('results_*')})
#        for answer in answers:
#                #TODO: write a proper class for this to share on all the search engines
#                cleanUrl = urllib2.unquote(answer.a['href'][15:])
#                siteDescription = answer.a.text
#                siteDetails = answer.findAll('a',{'class': re.compile('result__snippet')})[0].text
#                resultObj = {"url":cleanUrl, "description":siteDescription, "details":siteDetails, "answer":answer.text}
#                resultsList.append(resultObj)
#        return resultsList

