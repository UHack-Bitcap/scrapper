########importing Libraries
import requests
from bs4 import BeautifulSoup as bs

######## url of the website
url="http://indiatoday.intoday.in/story/some-on-twitter-ask-who-killed-aarushi/1/1067739.html"
r=requests.get(url)
print r
soup = bs(r.text,"html.parser")

########scrapping the various elements
data = soup.findAll("div", { "class" : "strleft" })[0]
findHeadline = data.find_all('h1')
# print findHeadline[0].text




date = soup.findAll("div", { "class" : "story-timedate" })[0]
# print date.text




content = soup.findAll("div", { "class" : "mediumcontent" })[0]
findContent = content.find_all('p')
a = 0
content = ''
for i in findContent:
	# print findContent[a].text
	content = content + findContent[a].text
	a = a + 1

######## returning the final json

finalJson = { 
				"headline":findHeadline[0].text, 
				"content":content, 
				"date":date.text
			}

print finalJson
