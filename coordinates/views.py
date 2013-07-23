from django.shortcuts import *
from django.http import *
import urllib2
import json
from coordinates.forms import *

def coords(request):
	form = Address(request.POST)
	address_data = []
	coo = ""
	formatted_address = ""
	if request.method == "POST":
		if form.is_valid():
			clean = form.cleaned_data
			address = clean['address']
			city = clean['city']
			state = clean['state']
			split_address = address.split()
			for i in split_address:
				address_data.append(i+"+")
			address_data.append(city+",+")
			address_data.append(state)
			for j in address_data:
				formatted_address += j
			url = "http://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false" % formatted_address
			response = urllib2.urlopen(url)
			coord_data = json.load(response)
			coordinates = coord_data[u'results'][0][u'geometry'][u'location']
			lat = str(coordinates[u'lat'])
			lon = str(coordinates[u'lng'])
			coo = "Latitude: "+lat+". Longitude: "+lon+"."
	return render(request, "coords.html", {"coo": coo, "form":form})
