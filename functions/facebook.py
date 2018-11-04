import requests
import json
import re
import os

#https://graph.facebook.com/search?type=place&fields=[%22about%22,%22link%22,%22phone%22,%22location%22,%22description%22]&center=42.1878631,-72.0148115&distance=1600000&categories=[%22MEDICAL_HEALTH%22]&access_token=<appid|secret>

fbId = os.environ["FACEBOOK_APP_ID"]
fbSecret = os.environ["FACEBOOK_APP_SECRET"]

def query(distance = 160000, center ="42.1878631,-72.0148115"):
	url = "https://graph.facebook.com/"
	uri = "search?type=place&fields=['about','link','phone','location','description']&center="\
		+center+"&distance="\
		+str(distance)+"&categories=['MEDICAL_HEALTH']&access_token="\
		+fbId+"|"\
		+fbSecret
	response = requests.get(url+uri)
	jsonResponse = json.loads(response.text)
	return jsonResponse

if __name__=="__main__":
	query()
