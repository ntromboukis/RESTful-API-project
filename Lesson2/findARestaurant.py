from geocode import getGeocodeLocation
import json
import httplib2
from api import *

import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

# - - - - - REMEMBER TO REMOVE THIS AND YOUR API KEY - - - -
# - - - - - - - - THEN REPLACE AFTER COMMIT - - - - - - - -

foursquare_client_id = foursquare_id()
foursquare_client_secret = foursquare_secret()


def findARestaurant(mealType,location):
	coordinates = getGeocodeLocation(location)
	url = ("https://api.foursquare.com/v2/venues/search?client_id=%s&client_secret=%s&v=20130815&ll=%s&query=%s"% (foursquare_client_id, foursquare_client_secret, coordinates, mealType))
	h=httplib2.Http()
	response, content = h.request(url, 'GET')
	result = json.loads(content)

	# Grabs the first restaurant
	firstID = result['response']['venues'][0]['id']
	name = result['response']['venues'][0]['name']
	venueUrl = ("https://api.foursquare.com/v2/venues/%s?client_id=%s&client_secret=%s&v=20130815"% (firstID, foursquare_client_id, foursquare_client_secret))
	res, cont = h.request(venueUrl, 'GET')
	venueResult = json.loads(cont)

	# Gets a  300x300 picture of the restaurant using the venue_id (you can change this by altering the 300x300 value in the URL or replacing it with 'orginal' to get the original picture
	photoUrl = venueResult['response']['venue']['bestPhoto']['prefix'] + '300x300' + venueResult['response']['venue']['bestPhoto']['suffix']
	loc = venueResult['response']['venue']['location']['formattedAddress']
	address = ''
	for i in loc:
		address += i + ','
	venueDict = {name, address, photoUrl}
	return venueDict

