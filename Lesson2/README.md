#Using the app

You first want to have a vm installed. I would suggest following [these](https://www.udacity.com/wiki/ud088/vagrant) instructions. You should only be concerned with installing VirtualBox and Vagrant.

You need obtain a Google Maps API key, and  Foursquare API key for this application to run.

Open api.py in your favorite text editor and paste your Google Maps API key, Foursquare client ID and Foursquare client secret in the appropriate sections.

Now ssh into your VM and cd into the directory with the geocode.py file. 
*Should be under ```/vagrant```*

Now get into a python shell and paste the following code
```
from geocode import getGeocodeLocation
from findARestaurant import findARestaurant
findARestaurant("Pizza", New York, NY")
```

You can change the location and venue type as you wish but you get the idea. This will return the Name, Address, and the url of the 'Best Picture' of the venue.

*Features to come: If the venue does not have any photos the application will return a default image url*