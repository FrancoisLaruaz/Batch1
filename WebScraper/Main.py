# -*-coding:Latin-1 -*

#Mian program :
# How to execute it : 
# work : C:\Users\franc\AppData\Local\Programs\Python\Python37-32\python.exe D:\DEV\Batch1\WebScraper\Main.py "103.220.212.10:8080" "Kayak" "AMS" "BCN" "10/10/2018" "18/10/2018"
# Home : C:\Users\franc\AppData\Local\Programs\Python\Python37\python.exe C:\DEV\Batch1\WebScraper\Main.py "195.64.223.116:3128" "Kayak" "AMS" "BCN" "10/10/2018" "18/10/2018"
# Packages to install (in C:\Users\franc\AppData\Local\Programs\Python\Python37-32) : 
#==>  python -m pip install pypyodbc
#==>  python -m pip install selenium
#==>  python -m pip install chromedriver
#==> download https://chromedriver.storage.googleapis.com/index.html?path=2.31/  and follow https://www.youtube.com/watch?v=dz59GsdvUF8

import os # On importe le module os
import sys
import traceback
from Logger.logger import LogError
from Provider.Kayak import SearchKayak

try:

	print("*** Start Web Scraper ***")
	if len(sys.argv) < 5 or  len(sys.argv) > 7:
		print("Arguments missing")
	proxy=sys.argv[1]
	provider=sys.argv[2]
	origin=sys.argv[3]
	destination=sys.argv[4]
	fromDate=sys.argv[5]
	toDate=sys.argv[6]
	print("provider = "+provider+" and origin= "+origin+" and destination = "+destination+" and fromDate = "+fromDate+" and toDate = "+toDate)
	
	if provider=="Kayak":
		SearchKayak(proxy,origin,destination,fromDate,toDate)
	
except Exception:
	LogError(''.join(traceback.format_exc()))
print("*** End Web Scraper ***")
os.system("pause")