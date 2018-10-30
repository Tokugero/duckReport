#!/usr/bin/python
import os
import json
from functions import duckduckgo
import re

searchQuery = "free clinic massachusetts inurl:contact -animal"

ddgResults = duckduckgo.query(searchQuery.replace(" ","+"))

for result in ddgResults:
	phoneNum = "No number found, search page directly"
	rpattern = "(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})"
	phoneNumParse = re.search(rpattern, result["answer"])
	if phoneNumParse:
		phoneNum = phoneNumParse.group(1)
	print result["url"]+"\n"+result["answer"]+"\n"+phoneNum+"\n-------------\n"

print len(ddgResults)
