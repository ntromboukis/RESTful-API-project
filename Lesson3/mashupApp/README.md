#Mashup API Project for Lesson 3

This is a mashup project using the Foursquare and Google Maps APIs to search for a venue and store it in a database.

###Running the application
- Assuming you have a VM up and running skip to step 2 if not, follow the directions on how to get your VM up and running [here](https://www.udacity.com/wiki/ud197/install-vagrant) do not do the last step.
- Clone this repository and navigate to /Lesson3/mashupApp
- Now run ```python models.py``` which will create a restaurants.db file.
- Run ```python findARestaurant.py```
- In a new terminal window navigate to this directory again
- Run ```python tester.py``` to check if all of the tests pass

To change the response open ```findARestaurant.py``` and change the code at the bottom to search for different types of food in different locations.