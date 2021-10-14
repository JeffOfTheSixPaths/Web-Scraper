from Scrap import *
import json
f = open('websites.json')
data = json.load(f)
headline_list = get_page(data["yahoo finance"]["url"]).find_all("h3")
summ = get_summaries(data["yahoo finance"]["url"])






