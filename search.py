#!/usr/bin/python
import os
import json
from functions import duckduckgo
import re

#This is a hardcoded query that will be a user input, the inurl & query tuning should be easier options to find or implicitly added
rawSearchQuery = "free clinic massachusetts inurl:contact -animal"

#transform the query into a usable string
searchQuery = rawSearchQuery.replace(" ","+")

#pass queries to search engines
ddgResults = duckduckgo.query(searchQuery)


#Transform queries here

#This is to transform ddg results from the form of [{url:"url",answer:"answer"}]
for result in ddgResults:
	phoneNum = "No number found, search page directly"
	#parse out phone numbers
	rpattern = "(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})"
	phoneNumParse = re.search(rpattern, result["answer"])
	if phoneNumParse:
		phoneNum = phoneNumParse.group(1)
	#This outputs to the console, but it should respond with something more useful
	print result["url"]+"\n"+result["answer"]+"\n"+phoneNum+"\n-------------\n"

print len(ddgResults)
