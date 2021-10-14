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
	
	

def rmAngles(string_with_tags):
	# removes the tags by finding all the < and > symbols and removing everything between them
	
	data = str(string_with_tags)
	
	## less is the < "less than" and greater is > "greater than"
	less_size = len(string_with_tags.split("<"))
	greater_size = len(string_with_tags.split(">"))
	
	
	## less == greater since it's parsing HTML tags 
	if less_size == greater_size:
		for i in range(less_size-1):
			less = string_with_tags.find("<")
			greater = string_with_tags.find(">")
			string_with_tags = string_with_tags[:less] + string_with_tags[greater+1:] 
			#string=string[:index] + string[index+1:] removes the character at [index], but not at [index+1]
	else:
		print("Error:spare \"<\" or \">\" character in: \n" + string_with_tags) # if there was a spare, the parsing algorithm would break
	
	
	
			
		
	return string_with_tags ##don't want to do string = string_with_tags somewhere just for return string 

def not_video(link):
	if link.find("/video/") == -1:
			link = link.split("/")[2]
			print(rmAngles(headline_list[i+4]))
			print("\n")
			print(link)
			print("\n")
			print(rmAngles(summ[i]))
			print("\n\n\n")


#448106
if __name__ == '__main__':
	f = open('websites.json')
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

	


	
