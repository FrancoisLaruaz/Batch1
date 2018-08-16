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

def SearchKayak(proxy,origin,destination,direct,fromDate,toDate):
	try:
		print ("** Begin Kayak **")
		url="https://ca.edreams.com/travel/#results/type=R;dep=2018-12-19;from=YVR;to=DUB;ret=2019-01-06;collectionmethod=false;airlinescodes=false;internalSearch=true"
		browser=getGoogleChromeDriver(proxy)
		browser.get(url)
		print ("** End Kayak **")
	except Exception:
		LogError(traceback,"proxy = "+proxy+" and origin = "+origin+" and destination = "+destination+" and fromDate = "+fromDate+" and toDate = "+toDate+" and direct = "+direct)
	return	

