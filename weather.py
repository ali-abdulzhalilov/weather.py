import requests
API_KEY = '2a069deb98184191ba6b519100b33edf'

type_options = {'current': 'current', \
				'hourly': 'forecast/hourly', \
				'3hourly': 'forecast/3hourly', \
				'daily': 'forecast/daily'}

def get(type='current', city_name=None, coordinates=None, ip=None, key=None):
	
	payload = {}
	if city_name:
		payload['city'] = city_name
	elif coordinates:
		lat, lon = coordinates
		payload['lat'] = lat
		payload['lon'] = lon
	elif ip:
		payload['ip'] = ip
	else:
		payload['ip'] = requests.get('https://api.ipify.org').text
	
	payload['key'] = key if key else API_KEY
	print(payload)
	url_prefab = 'https://api.weatherbit.io/v2.0/'+type_options[type]
	r = requests.get(url_prefab, params=payload)
	return r.json()
	
def print_data(data):
	if 'error' in data:
		print(data['error'])
	else:
		if 'city_name' in data:
			print(data['city_name'])
		#count = len(data['data'])
		for entry in data['data']:
			print_entry(entry)
		
def print_entry(entry):
	what_to_show = {
		'temp': 'Temperature: {} °C',
		'app_temp': 'Feels like: {} °C',
		'wind_spd': 'Wind speed: {} m/s',
		'wind_cdir': 'Wind direction: {}',
		'pop': 'Probability of precipitation: {}%',
		'vis': 'Visibility: {} km',
		'max_temp': 'Maximum temperature: {} °C',
		'min_temp': 'Minimum temperature: {} °C',
		'sunrise' : 'Sunrise: {}',
		'sunset' : 'Sunset: {}',
	}
	
	
	if 'valid_date' in entry:
		datetime = entry['valid_date']
	elif 'timestamp_local' in entry:
		datetime = ' '.join(entry['timestamp_local'].split('T'))
	else:
		datetime = 'current'
		
	"""
	datetime = entry['datetime'].split(':')
	datetime = entry['timestamp_local'].split(':')
	date = datetime[0]
	time = '' if len(datetime) == 1 else datetime[1] + ":00 "
	
	print('----- %s %s-----' % (date, time))
	"""
	print('----- %s -----' % datetime)
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
	group.add_argument('-ip', '--ip_address', help='IP address')
	parser.add_argument('-k', '--key', help='Your key form weatherbit.io')
	
	args = parser.parse_args()
	
	data = get(args.type, args.city_name, args.coordinates, args.ip_address, args.key)
	print_data(data)