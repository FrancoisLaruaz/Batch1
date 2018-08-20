# -*-coding:Latin-1 -*

#Mian program :
# How to execute it : 
# work : C:\Users\franc\AppData\Local\Programs\Python\Python37-32\python.exe D:\DEV\Batch1\WebScraper\Main.py "213.157.62.137" "1" "Edreams" "RNS" "TYO" "false" "10/10/2018" "18/10/2018"
# perso : C:\Users\franc\AppData\Local\Programs\Python\Python37\python.exe C:\DEV\Batch1\WebScraper\Main.py "137.74.254.242:3128 FR-H +" "1" "Edreams" "RNS" "TYO" "false" "09/10/2018" "20/10/2018"
# Packages to install (in C:\Users\franc\AppData\Local\Programs\Python\Python37-32) : 
#==>  python -m pip install pypyodbc
#==>  python -m pip install selenium
#==>  python -m pip install chromedriver
#==> download https://chromedriver.storage.googleapis.com/index.html?path=2.31/  and follow https://www.youtube.com/watch?v=dz59GsdvUF8

#Take proxy : https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list.txt
# or http://pubproxy.com/api/proxy?limit=1000&format=txt&http=true&country=TH&type=https

import os # On importe le module os
import sys
import traceback
from Logger.logger import LogError
from Provider.Kayak import SearchKayak
from Provider.Edreams import SearchEdreams
from datetime import datetime, timezone

try:

	print("\n*** Start Web Scraper *** : " +datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]+"\n")
	if len(sys.argv) < 7 or  len(sys.argv) > 9:
		print("Arguments missing")
	proxy=sys.argv[1]
	searchTripProviderId=sys.argv[2]
	provider=sys.argv[3]
	origin=sys.argv[4]
	destination=sys.argv[5]
	direct=sys.argv[6]
	fromDate=sys.argv[7]
	toDate=sys.argv[8]
	print("provider = "+provider+" and searchTripProvider= "+searchTripProviderId+" and origin= "+origin+" and destination = "+destination+" and fromDate = "+fromDate+" and toDate = "+toDate+" and direct = "+direct+"\n")
	
	if provider=="Kayak":
		SearchKayak(proxy,searchTripProviderId,origin,destination,direct,fromDate,toDate)
	elif  provider=="Edreams":
		SearchEdreams(proxy,searchTripProviderId,origin,destination,direct,fromDate,toDate)		
	
except Exception:
	LogError(traceback)
print("*** End Web Scraper *** : " +datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
os.system("pause")