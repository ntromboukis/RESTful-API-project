from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Restaurant
from geocode import getGeocodeLocation
import json
import httplib2
from api import *

import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

engine = create_engine('sqlite:///restaurants.db')
Base.metadata.bind = engine

DBSesison = sessionmaker(bind=engine)
session = DBSesison()

foursquare_client_id = foursquare_id()
foursquare_client_secret = foursquare_secret()
google_api_key = google_key()

app = Flask(__name__)

def getGeocodeLocation(inputString):
	locationString = inputString.replace(" ", "+")
	url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key%s'% (locationString, google_api_key))
	h = httplib2.Http()
	response, content = h.request(url, 'GET')
	result = json.loads(content)
	latitude = result['results'][0]['geometry']['location']['lat']
	longitude = result['results'][0]['geometry']['location']['lng']
	return (str(latitude) + "," + str(longitude))

def findARestaurant(mealType,location):
		coordinates = getGeocodeLocation(location)
		url = ("https://api.foursquare.com/v2/venues/search?client_id=%s&client_secret=%s&v=20130815&ll=%s&query=%s"% (foursquare_client_id, foursquare_client_secret, coordinates, mealType))
		h=httplib2.Http()
		result = json.loads(h.request(url, 'GET')[1])

		if result['response']['venues']:
			#Grab the first restaurant
			restaurant = result['response']['venues'][0]
			venue_id = restaurant['id']
			restaurant_name = restaurant['name']
			restaurant_address = restaurant['location']['formattedAddress']
			#Format the Restaurant Address into one string
			address = ""
			for i in restaurant_address:
					address += i + " "
			restaurant_address = address

			#Get a  300x300 picture of the restaurant using the venue_id (you can change this by altering the 300x300 value in the URL or replacing it with 'orginal' to get the original picture
			url = ('https://api.foursquare.com/v2/venues/%s/photos?client_id=%s&v=20150603&client_secret=%s' % ((venue_id,foursquare_client_id,foursquare_client_secret)))
			result = json.loads(h.request(url,'GET')[1])
			#Grab the first image
			#if no image available, insert default image url
			if result['response']['photos']['items']:
					firstpic = result['response']['photos']['items'][0]
					prefix = firstpic['prefix']
					suffix = firstpic['suffix']
					imageURL = prefix + "300x300" + suffix
			else:
					imageURL = "http://pixabay.com/get/8926af5eb597ca51ca4c/1433440765/cheeseburger-34314_1280.png?direct"

			restaurantInfo = {'name':restaurant_name, 'address':restaurant_address, 'image':imageURL}
			#print "Restaurant Name: %s " % restaurantInfo['name']
			#print "Restaurant Address: %s " % restaurantInfo['address']
			#print "Image: %s \n " % restaurantInfo['image']
			return restaurantInfo
		else:
		#print "No Restaurants Found for %s" % location
			return "No Restaurants Found"


if __name__ == '__main__':
		findARestaurant("Pizza", "Tokyo, Japan")
		findARestaurant("Tacos", "Jakarta, Indonesia")
		findARestaurant("Tapas", "Maputo, Mozambique")
		findARestaurant("Falafel", "Cairo, Egypt")
		findARestaurant("Spaghetti", "New Delhi, India")
		findARestaurant("Cappuccino", "Geneva, Switzerland")
		findARestaurant("Sushi", "Los Angeles, California")
		findARestaurant("Steak", "La Paz, Bolivia")
		findARestaurant("Gyros", "Sydney Austrailia")
