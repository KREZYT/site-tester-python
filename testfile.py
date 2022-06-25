import requests
import time

site = input("сайт для проверки: ")

respone = requests.get(site)

reults = None

if respone:
	reults = ("сайт роботает")
	


else:
	reults = ("сайт не роботает")
	



while respone:
	time.sleep(0.2)
	print(reults)
