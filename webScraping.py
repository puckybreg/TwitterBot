#!/usr/bin/env python3
import urllib.request
from bs4 import BeautifulSoup

cds_stevie = "http://oberlin.cafebonappetit.com/cafe/stevenson/"

cds_simple = "http://legacy.cafebonappetit.com/weekly-menu/139759"

cds_hours = "https://dining.oberlin.edu/xcds/hours/now.php"

test = "https://www.bloomberg.com/quote/SPX:IND"

page = urllib.request.urlopen(cds_simple)

soup = BeautifulSoup(page, "html.parser" )
#.div.div.div.div.section.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.article


#print(soup.prettify())
#print(soup.get_text())

# Take out the <div> of name and get its value
#name_box = soup.find('h5', attrs={'class': 'station-item-title'})
#name_box = soup.find('h1', attrs={'class': 'name'})
#name_box = soup.find('h4', attrs={'id': 'station-5626'})
#test_box = soup.find('tr', attrs={'class': 'td-2 spright prompt line staticrow'})
#name_box = soup.find('table', attrs={'class': 's11 tdrows space'})
foodCounter = soup.find_all('div', class_ = "row")
mondayID = 'td-4378-1'
tuesdayID = 'td-4378-2'
wedID = 'td-4378-3'
thursID = 'td-4378-4'
friID = 'td-4378-5'
satID = 'td-4378-6'
sunID = 'td-4378-0'

def f(day):
	return {
		0 : mondayID,
		1 : tuesdayID,
		2 : wedID,
		3 : thursID,
		4 : friID,
		5 : satID,
		6 : sunID,
	}[day]

# for i in monday.contents:
# 	if (i.name == 'strong'):
# 		print('plop')

def getMenu(day):
	ID = f(day)

	menu = soup.find('div', id = mondayID)	
	print(menu.strong.span.string)
	#return menu.strong.span.string

