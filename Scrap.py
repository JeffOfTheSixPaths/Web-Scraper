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
	site = str(site)
	if(site == "https://finance.yahoo.com/news/"):
		headlines = get_page("https://finance.yahoo.com/news").find_all("h3")
		return headlines
		
def find_href(string):
	return str(string).split("href=")[1].split("\"")[1]
	
	
	
def get_summaries(site):
	return get_page(str(site)).find_all("p")

def print_summaries(site):
	article = get_summaries(str(site))
	print("====================================")
	for i in range(len(article) - 1):
		if rmAngles(article[i]) != "Related Quotes":
			print(rmAngles(article[i]))
			print("\n\n")
	print("====================================")

def get_articles(site):
	string = rmAngles(str(get_page(str(site)).find_all("div", class_="caas-body")))
	string = string[:0] + string[1:]
	return string[:-1]
	

def rmAngles(string_with_tags):
	# removes the tags by finding all the < and > symbols and removing everything between them
	
	string_with_tags = str(string_with_tags)
	
	## less is < "less than" and greater is > "greater than"
	less_size = len(string_with_tags.split("<"))
	greater_size = len(string_with_tags.split(">"))
	
	
	## less == greater since it's parsing HTML tags 
	if less_size == greater_size:
		for i in range(int(less_size)-1):
			less = string_with_tags.find("<")
			greater = string_with_tags.find(">")
			string_with_tags = string_with_tags[:less] + string_with_tags[greater+1:] 
			#string=string[:index] + string[index+1:] removes the character at [index], but not at [index+1]
	else:
		print("Error:spare \"<\" or \">\" character in: \n" + string_with_tags) # if there was a spare, the parsing algorithm would break
	return string_with_tags ##don't want to do string = string_with_tags somewhere just for return string 

def not_video(link):
	#finds href already
	headline_list = get_page(link).find_all("h3")
	link = find_href(str(headline_list[i+4]))
	if link.find("/video/") == -1:
			#link = link.split("/")[2]
			return True


#448106
if __name__ == '__main__':
	f = open('websites.json')
	data = json.load(f)
	research =[["headline", "summary", "article"]]
	headline_list = get_headlines(data['yahoo finance']['url'])
	summary_list = get_summaries("https://finance.yahoo.com/news/")
	#headline should be buffered by +6 and summaries should be buffered by +4, so the initial range is 4 and headline_list get's 2 added to it's index
	print(len(headline_list))
	print(len(summary_list))

	for i in range(4,len(summary_list)):
		temp_list = [str(headline_list[i+2]),str(summary_list[i]),str(get_articles(data['yahoo finance']['url']))]
		research.append(temp_list)
	for i in range(len(research) - 1):
		for index in range(3):
			print(research[i][index])
			print("\n")
		print(len(research) - i - 2)
		input("press ENTER to continue... \n")
