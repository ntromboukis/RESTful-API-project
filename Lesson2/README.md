#Using the app

You first want to have a vm installed. I would suggest following [these](https://www.udacity.com/wiki/ud088/vagrant) instructions. You should only be concerned with installing VirtualBox and Vagrant.

Open geocode.py in your favorite text editor and put in your Google Maps API key on line 5.

Now ssh into your VM and cd into the directory with the geocode.py file. 
*Should be under ```/vagrant```*

Now get into a python shell and paste the following code
```
from geocode import getGeocodeLocation
geoGeocodeLocation("New York, NY")
```

You can change the location but you get the idea. This will return the latitude and longitude of the param.