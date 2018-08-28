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

import requests
API_KEY = '2a069deb98184191ba6b519100b33edf'

type_options = {'current': 'current', \
				'for5': 'forecast/3hourly', \
				'for16': 'forecast/daily'}

def __init__():
	print("am i a module")

def get_weather_data(type='current', city_name=None, coordinates=None):
	print('I got %s type for %s or at %s' % (type, city_name, coordinates))
	
	if not city_name and not coordinates:
		coordinates = where_am_i()
		
	payload = {}
	if city_name:
		payload['q'] = city_name
		
	if coordinates:
		lat, lon = coordinates
		payload['lat'] = lat
		payload['lon'] = lon
	
	payload['key'] = API_KEY
		
	url_prefab = 'https://api.weatherbit.io/v2.0/'+type_options[type]
	print(url_prefab+str(payload))
	r = requests.get(url_prefab, params=payload)
	return r.json()
	
def where_am_i():
	import geocoder
	
	g = geocoder.ip('me')
	return g.latlng
	
def print_weather_data(data):

	count = len(data['data'])
	for entry in data['data']:
		print_weather_entry(entry)
		
def print_weather_entry(entry):
	what_to_show = {
		'temp': 'Temperature: {} C',
		'app_temp': 'Feels like: {} C',
		'wind_spd': 'Wind speed: {} m/s',
		'wind_cdir': 'Wind direction: {}',
		'pop': 'Probability of precipitation: {}%',
		'vis': 'Visibility: {}km',
		'max_temp': 'Maximum temperature: {} C',
		'min_temp': 'Minimum temperature: {} C',
	}
	
	datetime = entry['datetime'].split(':')
	date = datetime[0]
	time = ' ' if len(datetime) == 1 else datetime[1] + ":00 "
	
	print('----- %s %s-----' % (date, time))
	for thing in what_to_show:
		if thing in entry:
			print(what_to_show[thing].format(entry[thing]))
	print()

if (__name__=='__main__'):
	import argparse
	parser = argparse.ArgumentParser()
	
	parser.add_argument('-t', '--type', help='Type of weather data', choices=list(type_options.keys()), default='current')
	group = parser.add_mutually_exclusive_group()
	group.add_argument('-n', '--city_name', help='City name')
	group.add_argument('-c', '--coordinates', type=float, nargs=2, help='Coordinates of the location of your interest', metavar=('LATITUDE', 'LONGITUDE'))
	
	args = parser.parse_args()
	
	data = get_weather_data(args.type, args.city_name, args.coordinates)
	print_weather_data(data)