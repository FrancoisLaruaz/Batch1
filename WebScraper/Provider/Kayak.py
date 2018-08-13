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

def SearchKayak(origin,destination,fromDate,toDate):
	print ("** Begin Kayak **")
	url="https://github.com/TheDancerCodes"
	
	#option = webdriver.ChromeOptions()
	#option.add_argument("--incognito")
	#browser = webdriver.Chrome(executable_path="C:\\webdrivers\\chromedriver.exe", chrome_options=option)
	browser=getFirefoxDriver("189.115.161.38","3128 ")
	browser.get(url)
	print ("** End Kayak **")
	return

