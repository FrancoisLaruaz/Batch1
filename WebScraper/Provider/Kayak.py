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

def SearchKayak(proxy,origin,destination,fromDate,toDate):
	try:
		print ("** Begin Kayak **")
		#https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list.txt
		url="https://kayak.com"

		browser=getGoogleChromeDriver(proxy)
		browser.get(url)
		print ("** End Kayak **")
	except Exception:
		LogError(''.join(traceback.format_exc()),"proxy = "+proxy+" and origin = "+origin+" and destination = "+destination+" and fromDate = "+fromDate+" and toDate = "+toDate)
	return	

