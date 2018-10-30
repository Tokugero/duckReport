from BeautifulSoup import BeautifulSoup
import requests
import os
import re
import urllib

#https://api.duckduckgo.com/?q=valley+forge+national+park&format=json&pretty=1

#Define the search function
def query(search):
	url = "https://duckduckgo.com/html/?q="
	request = requests.get(url+search)
	results = beautify(request.text)
	return results

#Clean up the search results, they'll all be gobbledy html
def beautify(results):
	resultsList = []
	resultsPretty = BeautifulSoup(results)
	topics = resultsPretty.findAll('div',{'id':'links'})[0]
	answers = topics.findAll('div',{'class': re.compile('results_*')})
	for answer in answers:
		#TODO: write a proper class for this to share on all the search engines
		resultObj = {"url":urllib.unquote(answer.a['href'][15:]), "answer":answer.text[24:]}
		resultsList.append(resultObj)
	return resultsList
	

#A simple test call if ran directly
if __name__=="__main__":
	query("test")
