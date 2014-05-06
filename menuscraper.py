import os
import sys
import re
import urllib2

from BeautifulSoup import BeautifulSoup as bs


IKES_PATH = 'http://www.ilikeikesplace.com'

SANDWICH_TITLE = 'views-field-title'
# SANDWICH TITLES
# <div class="views-field-title">
#               <span class="field-content">Captain Kirk</span>
# </div>

SANDWICH_INGREDIENTS = 'views-field-tid'
# SANDWICH_INGREDIENTS
# <div class="views-field-tid">
#                 <span class="field-content">Avocado, Pepper Jack, Sweet Orange Glaze, Vegan Breaded Chicken</span>
# </div>

SANDWICH_PRICE = 'views-field-field-price-full-value'
# SANDWICH_PRICE
# <div class="views-field-field-price-full-value">
#         <span class="field-content">$12.21</span>
# </div>

def gen_soup(url):
	html = urllib2.urlopen(url)
	soup = bs(html)
	return soup

ikes_soup = gen_soup(IKES_PATH)


def parse_sandwich(array):
    price = x.findNext('span').text
    name = x.findNext('div').findNext('span').text
    ingredients = x.findNext('div').findNext('span').findNext('span').text.split(',')
    array += [{"name": name,
            "price": price,
            "ingredients": ingredients}]

menu = []
for x in soup.findAll('div', attrs={'class':SANDWICH_PRICE}):
    parse_sandwich(menu)

mdf = pd.DataFrame.from_dict(menu)

#  need to figure out how to get the ingredients represented as dummy variables
#  maybe need "ingredient1 | ingredient2 | so on..." and then go to dummys, or perhaps
#  it would make sense to write a function to translate it to Avocado | French Dressing |
#  etc in the parse_sandwich function
