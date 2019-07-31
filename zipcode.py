import requests
import csv

url="http://api.zippopotam.us/us/"

for x in range(10000,99999):
	url +=str(x)
	print(url)
	r = requests.get(url)
	print(r.text)	
	f = open("zip.txt", "a")	
	f.write(r.text)
	f.write("\n")
	f.close()
	url="http://api.zippopotam.us/us/"
