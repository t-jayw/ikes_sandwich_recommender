import os
import sys
import re
import urllib2

from BeautifulSoup import BeautifulSoup as bs


IKES_PATH = 'http://www.ilikeikesplace.com'

SANDWICH_TITLE = 'views-field-title'
# SANDWICH TITLES
# <div class="views-field-title">
#   <span class="field-content">Captain Kirk</span>
# </div>

SANDWICH_INGREDIENTS = 'views-field-tid'
# SANDWICH_INGREDIENTS
# <div class="views-field-tid">
#   <span class="field-content">Avocado, Pepper Jack, Sweet Orange Glaze, Vegan Breaded Chicken</span>
# </div>

SANDWICH_PRICE = 'views-field-field-price-full-value'
# SANDWICH_PRICE
# <div class="views-field-field-price-full-value">
#   <span class="field-content">$12.21</span>
# </div>

def gen_soup(url):
	html = urllib2.urlopen(url)
	soup = bs(html)
	return soup

ikes_soup = gen_soup(IKES_PATH)


soup.find('div', attrs={'class':SANDWICH_TITLE}).find('span').text

x = [x.find('span').text for x in soup.findAll('div', attrs={'class':SANDWICH_TITLE})
