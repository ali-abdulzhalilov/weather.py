#  `weather.py`
smol ~~useless~~ weather script which pulls data from weatherbit.io

## Installion

Just drop it in whatever folder where you want to use it

## Usage
### As script
```
D:\pthn\wthr>python weather.py -h
usage: weather.py [-h] [-t {current,hourly,3hourly,daily}]
                  [-n CITY_NAME | -c LATITUDE LONGITUDE | -ip IP_ADDRESS]
                  [-k KEY]

optional arguments:
  -h, --help            show this help message and exit
  -t {current,hourly,3hourly,daily}, --type {current,hourly,3hourly,daily}
                        Type of weather data
  -n CITY_NAME, --city_name CITY_NAME
                        City name
  -c LATITUDE LONGITUDE, --coordinates LATITUDE LONGITUDE
                        Coordinates of the location of your interest
  -ip IP_ADDRESS, --ip_address IP_ADDRESS
                        IP address
  -k KEY, --key KEY     Your key form weatherbit.io
```
### As module
```
import weather

data = weather.get(city_name='London')
weather.print_data(data)
```
## Todos

 - Make output beautiful (icons?, description, etc.)
 - Add more weather data types (historical?)
 - Add more weather providers (?)

## License
[MIT](https://choosealicense.com/licenses/mit/)