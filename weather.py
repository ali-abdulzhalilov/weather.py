import sys
import urllib.request

def do_magic():
	response = urllib.request.urlopen('https://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22')
	return response
	

if (__name__=='__main__'):


	print("my name is: %s" % (sys.argv[0]))
	print("i have %i args" % (len(sys.argv)))
	print("my args are: %s" % (sys.argv))
	#this = do_magic()
	#print(this.read())