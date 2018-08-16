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
		waitForWebdriver(browser,".od-resultpage-highlight-title")		
		elements = browser.find_elements_by_xpath("//div[@class='result od-resultpage-wrapper    ']")

		for element in elements:
			ExtractData(element)
		
		print ("** End Edreams **\n")
	except Exception:
		LogError(traceback,"proxy = "+proxy+" and origin = "+origin+" and destination = "+destination+" and fromDate = "+fromDate+" and toDate = "+toDate+" and direct = "+direct)
	return

def GetDateForUrl(date):
	result=""
	try:
		result=date[6:10]+"-"+date[3:5]+"-"+date[0:2]
	except Exception:
		LogError(traceback,"date = "+date)
	return	result
	
def ExtractData(element):
	try:
		print("*** Begin study element ***")
		text=element.text				
		flightNumber=0
		
		flights=element.find_elements_by_xpath(".//div[@class='odf-row-fluid odf-space-inner-top-s odf-space-inner-bottom-s sp_container']");
		for flight in flights:
			flightNumber=flightNumber+1
			print("Flight number :"+str(flightNumber))
			rightDiv=flight.find_element_by_xpath(".//div[@class='odf-row-fluid odf-text-left odf-text-sm od-secondary-flight-info-time-stops-wrapper']")
			time=flight.find_element_by_xpath(".//div[@class='odf-row odf-h3']").text.replace(" ", "");
			print("time = "+time)
			duration=rightDiv.find_element_by_xpath(".//span[@class='odf-text-nowrap']").text.replace(" ", "");
			print("duration = "+duration)
			cities=flight.find_element_by_xpath(".//div[@class='odf-row odf-text-sm od-primary-flight-info-cities hover-active-tooltip odf-text-mono-color-03 flight_info_cities odf-text-nowrap']").text;
			print("cities = "+cities)
			airlineLogo=flight.find_element_by_xpath(".//img[@class='od-resultpage-segment-itinerary-title-carrier-logo od-primary-description-carrier-icon']");
			airline=airlineLogo.get_attribute("alt");
			print("airline = "+airline+"\n")
		
		price=element.find_element_by_xpath(".//div[@class='od-price-container  ']").text.replace(" ", "").replace("*", "");
		print("price = "+price)

		print("*** End study element ***\n")
	except Exception:
		LogError(traceback,"element = "+element.text)
	return
	
	
	

