## python webscraper
import requests
from bs4 import BeautifulSoup
import json
## lxml parser downloaded
temp = 0;
def get_page(url):
	temp = BeautifulSoup(requests.get(str(url)).text,'lxml')
	return BeautifulSoup(requests.get(str(url)).text,'lxml')
	
def get_headlines(site):
	if(site == "yahoo finance"):
		headlines = get_page("https://finance.yahoo.com/news").find_all("h3")
		return headlines
		
def find_href(string):
	return str(string).split("href=")[1].split("\"")[1]
	
	
	
def get_summaries(site):
	return get_page(str(site)).find_all("p")

def get_articles(site):
	article = get_summaries(str(site))
	print("====================================")
	for i in range(len(article) - 1):
		if rmAngles(article[i]) != "Related Quotes":
			print(rmAngles(article[i]))
			print("\n\n")
	print("====================================")
	
	

def rmAngles(data):
	delete = False
	data = str(data)
	index = 0;
	for i in range(len(data)-1):
		if index < len(data):
			if not delete:
				if data[index] == '<':
					delete = True	
			if delete:
				data=data[:index] + data[index+1:]
			if data[index] == '>':
				data=data[:index] + data[index+1:]
				delete = False;
			elif not delete:
				index = index + 1
		
			
		
	return data




#448106
if __name__ == '__main__':
	f = open('imp.json')
	data = json.load(f)
	headline_list = get_page(data["yahoo finance"]["url"]).find_all("h3")
	summ = get_summaries(data["yahoo finance"]["url"])
	for i in range(3,len(summ)-1):
		link = find_href(headline_list[i+4])
		if link.find("/video/") == -1:
			link = link.split("/")[2]
			print(rmAngles(headline_list[i+4]))
			print("\n")
			print(link)
			print("\n")
			print(rmAngles(summ[i]))
			print("\n\n\n")
		else:
			i += 1

	


	
