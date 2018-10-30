from BeautifulSoup import BeautifulSoup
import requests
import os
import re
import urllib

#https://api.duckduckgo.com/?q=valley+forge+national+park&format=json&pretty=1

def query(search):
	url = "https://duckduckgo.com/html/?q="
	request = requests.get(url+search)
	results = beautify(request.text)
	return results

def beautify(results):
	resultsList = []
	resultsPretty = BeautifulSoup(results)
	topics = resultsPretty.findAll('div',{'id':'links'})[0]
	answers = topics.findAll('div',{'class': re.compile('results_*')})
	for answer in answers:
		resultObj = {"url":urllib.unquote(answer.a['href'][15:]), "answer":answer.text[24:]}
		resultsList.append(resultObj)
	return resultsList
	

if __name__=="__main__":
	query("test")
