import os
import sys
from datetime import datetime, timezone
import traceback
from Logger.logger import *
from DBConnection.SQLConnect import *
from SeleniumHelper.webdriver import *
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options

def SearchEdreams(proxy,origin,destination,direct,fromDate,toDate):
	try:
		print ("** Begin Edreams **")

		url="https://www.edreams.com/travel/#results/type=R;dep="+GetDateForUrl(fromDate)+";from="+origin+";to="+destination+";ret="+GetDateForUrl(toDate)+";collectionmethod=false;airlinescodes=false;internalSearch=true"
		if direct=="true":
			url=url+";direct=true"
		
		browser=getGoogleChromeDriver(proxy)
		browser.get(url)
		waitForWebdriver(browser,".flights_filters_summary_panel")
		prices = browser.find_elements_by_xpath("//a[@class=’text-bold’]")
		# use list comprehension to get the actual repo titles and not the selenium objects.
		titles = [x.text for x in prices]
		# print out all the titles.
		print('titles:')
		print(titles, '\n')	
		
		print ("** End Edreams **")
	except Exception:
		LogError(''.join(traceback.format_exc()),"proxy = "+proxy+" and origin = "+origin+" and destination = "+destination+" and fromDate = "+fromDate+" and toDate = "+toDate+" and direct = "+direct)
	return

def GetDateForUrl(date):
	result=""
	try:
		result=date[6:10]+"-"+date[3:5]+"-"+date[0:2]
	except Exception:
		LogError(''.join(traceback.format_exc()),"date = "+date)
	return	result

