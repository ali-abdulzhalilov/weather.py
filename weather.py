""" 
	smol weather script, which can be used as module or as standalone script
	
	Usage:
		As script:
			python weather.py [<type> [<city_name> | <latitude> <longitude>]
	
	Todo:
		TODO: Properly read console arguments
		TODO: Contruct request string
		TODO: Receive response
		TODO: Display result
"""

import urllib.request
import requests

type_options = {'current': 'weather', \
				'for5': 'forecast', \
				'for16': 'forecast/daily'}

def __init__():
	print("am i a module")

def do_magic():
	response = urllib.request.urlopen('https://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22')
	return response
	
def do_a_thing(type, city_name=None, coordinates=None):
	print('I got %s type for %s or at %s' % (type, city_name, coordinates))
	
	if !city_name and !coordinates:
		coordinates = where_am_i()
	
def where_am_i():
	import geocoder
	
	g = geocoder.ip('me')
	return g.latlng
	

if (__name__=='__main__'):
	import argparse
	parser = argparse.ArgumentParser()
	
	parser.add_argument('-t', '--type', help='Type of weather data', choices=list(type_options.keys()), default='current')
	group = parser.add_mutually_exclusive_group()
	group.add_argument('-n', '--city_name', help='City name')
	group.add_argument('-c', '--coordinates', type=float, nargs=2, help='Coordinates of the location of your interest', metavar=('LATITUDE', 'LONGITUDE'))
	
	args = parser.parse_args()
	
	do_a_thing(args.type, args.city_name, args.coordinates)