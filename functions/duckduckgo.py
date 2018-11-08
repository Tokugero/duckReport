from bs4 import BeautifulSoup as bs 
import requests
import os
import re
import urllib.request as urllib2

#https://duckduckgo.com/html/?q=valley+forge+national+park

#Define the search function
def query(search):
	url = "https://duckduckgo.com/html/?q="
	request = requests.get(url+search)
	results = beautify(request.text)
	return results

#Clean up the search results, they'll all be gobbledy html
def beautify(results):
	resultsList = []
	resultsPretty = bs(results)
	topics = resultsPretty.findAll('div',{'id':'links'})[0]
	answers = topics.findAll('div',{'class': re.compile('results_*')})
	for answer in answers:
		#TODO: write a proper class for this to share on all the search engines
		cleanUrl = urllib2.unquote(answer.a['href'][15:])
		siteDescription = answer.a.text
		siteDetails = answer.findAll('a',{'class': re.compile('result__snippet')})[0].text
		resultObj = {"url":cleanUrl, "description":siteDescription, "details":siteDetails, "answer":answer.text}
		resultsList.append(resultObj)
	return resultsList
	

#A simple test call if ran directly
if __name__=="__main__":
	query("test")
