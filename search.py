#!/usr/bin/python
import os
import json
from functions import duckduckgo
from functions import bing
import re
import urllib2

#This is a hardcoded query that will be a user input, the inurl & query tuning should be easier options to find or implicitly added
rawSearchQuery = "free clinic massachusetts"
inurl = ["contact"]
exclude = ["animals"]
#transform the query into a usable string
searchQuery = rawSearchQuery.replace(" ","+")
rpattern = "(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})"
missingMessage = "No number found, search page directly"
#pass queries to search engines

#This is to transform ddg results from the form of [{url:"url",answer:"answer"}]
def getDDG(query,inurl=[],exclude=[]):
	inurltext = ""
	excludeText = ""
	for url in inurl:
		inurltext = inurltext+"+inurl:"+url
	for exc in exclude:
		excludeText = excludeText+"+-"+exc
	query = query+inurltext+excludeText
	ddgResults = duckduckgo.query(query)
	for result in ddgResults:
		phoneNum = missingMessage
		#parse out phone numbers
		phoneNumParse = re.search(rpattern, result["answer"])
		if phoneNumParse:
			phoneNum = phoneNumParse.group(1)
		#This outputs to the console, but it should respond with something more useful
		print "DuckDuckGo\n"+urllib2.unquote(result["url"])+"\n"+result["description"]+"\n"+result["details"]+"\n"+phoneNum+"\n-------------\n"

def getBing(query,inurl=[],exclude=[]):
	inurltext = ""
	excludeText = ""
	for url in inurl:
		inurltext = inurltext+"+intitle:"+url
	for exc in exclude:
		excludeText = excludeText+"+-"+exc
	query = query+inurltext+excludeText
	bingResults = bing.query(query)
	for result in bingResults:
		phoneNum = missingMessage
		phoneNumParse = re.search(rpattern, result["answer"])
		if phoneNumParse:
			phoneNum = phoneNumParse.group(1)
		print "Bing\n"+urllib2.unquote(result["url"])+"\n"+result["description"]+"\n"+result["details"]+"\n"+phoneNum+"\n-------------\n"
	return

#add or remove desired search queries here:
getDDG(searchQuery,inurl,exclude)
getBing(searchQuery,inurl,exclude)
