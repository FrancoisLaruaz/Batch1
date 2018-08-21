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
from Model.Trip import *
from Helper.providerHelper import *
import re
from DBConnection.trip import *
from Helper.dateHelper import *

def SearchEdreams(proxy,searchTripProviderId,origin,destination,direct,fromDate,toDate):
	result="KO|"
	try:
		print ("** Begin Edreams **")

		url="https://www.edreams.com/travel/#results/type=R;dep="+GetDateForUrl(fromDate)+";from="+origin+";to="+destination+";ret="+GetDateForUrl(toDate)+";collectionmethod=false;airlinescodes=false;internalSearch=true"
		if direct=="true":
			url=url+";direct=true"
		
		browser=getGoogleChromeDriver(proxy)
		browser.get(url)
		result=waitForWebdriver(searchTripProviderId,browser,".od-resultpage-highlight-title",".dialog_error")
		
		if result=="OK":	
			if checkExistsByXpath(browser,"//div[@class='od-ui-dialog dialog dialog_error dialog-undefined od-center-dialogs']") :
				SetTripProviderAsSuccess(searchTripProviderId)
				result="OK"
				print ("** End Edreams : no resuld founds **\n")
				browser.quit()
				return result
			
			elements = browser.find_elements_by_xpath("//div[@class='result od-resultpage-wrapper    ']")
			for element in elements:
				ExtractData(element,url,fromDate,toDate,searchTripProviderId)
			elements = browser.find_elements_by_xpath("//div[@class='result od-resultpage-wrapper highlighted odf-box  ']")
			for element in elements:
				ExtractData(element,url,fromDate,toDate,searchTripProviderId)		
			result="OK"
		browser.quit()
		print ("** End Edreams **\n")
	except Exception:
		result="KO|"+''.join(traceback.format_exc())	
		LogError(traceback,"proxy = "+proxy+" and searchTripProviderId = "+searchTripProviderId+" and origin = "+origin+" and destination = "+destination+" and fromDate = "+fromDate+" and toDate = "+toDate+" and direct = "+direct)
		browser.quit()
	return result

def GetDateForUrl(date):
	result=""
	try:
		result=date[6:10]+"-"+date[3:5]+"-"+date[0:2]
	except Exception:
		LogError(traceback,"date = "+date)
	return	result
	
def ExtractData(element,url,fromDate,toDate,searchTripProviderId):
	try:
		print("*** Begin study element ***")
		text=element.text				
		flightNumber=0
		#itinerary_group
		#data-itinerary-group-id
		if not checkExistsByXpath(element,".//span[@class='odf-icon odf-icon-combination-fl-train-a ficon-2xl']"):	
			OneWayTrips=[]
			ReturnTrips=[]
			ways=element.find_elements_by_xpath(".//div[@class='itinerary_group']");
			for way in ways:
				wayId=way.get_attribute("data-itinerary-group-id");
				print("\n wayId = "+wayId)
				flightNumber=0
				flights=way.find_elements_by_xpath(".//div[@class='odf-row-fluid odf-space-inner-top-s odf-space-inner-bottom-s sp_container']");
				for flight in flights:
					flightNumber=flightNumber+1
					print("Flight number :"+str(flightNumber))
					rightDiv=flight.find_element_by_xpath(".//div[@class='odf-row-fluid odf-text-left odf-text-sm od-secondary-flight-info-time-stops-wrapper']")
					time=flight.find_element_by_xpath(".//div[@class='odf-row odf-h3']").text.replace(" ", "");
					print("time = "+time)
					hours=time.split('-')[0]
					if wayId=="1":
						baseDate=fromDate
					elif wayId=="2":
						baseDate=toDate
					if len(hours.split('+'))==2:
						departureTime=addDay(baseDate,hours.split('+')[1][0:1])+' '+hours.split('+')[0]
					else:
						departureTime=baseDate+' '+hours
					hours=time.split('-')[1]	
					if len(hours.split('+'))==2:						
						arrivalTime=addDay(baseDate,hours.split('+')[1][0:1])+' '+hours.split('+')[0]
					else:
						arrivalTime=baseDate+' '+hours
					print("departureTime = "+departureTime)
					print("arrivalTime = "+arrivalTime)
					duration=getDurationMinute(rightDiv.find_element_by_xpath(".//span[@class='odf-text-nowrap']").text);
					print("duration = "+str(duration))
					if checkExistsByXpath(rightDiv,".//span[@class='odf-text-nowrap number_stop ']"):
						stopNumber=rightDiv.find_element_by_xpath(".//span[@class='odf-text-nowrap number_stop ']").text.split(' ')[0];
						print("stop Number = "+stopNumber)
					else :
						stopNumber="0";
						print("stop Number = "+stopNumber)
					airline="*Unkwown*";
					airlineSrc=""					
					if checkExistsByXpath(flight,".//img[@class='od-resultpage-segment-itinerary-title-carrier-logo od-primary-description-carrier-icon']"):
						airlineLogo=flight.find_element_by_xpath(".//img[@class='od-resultpage-segment-itinerary-title-carrier-logo od-primary-description-carrier-icon']");
						airlineSrc=airlineLogo.get_attribute("src");
						airline=airlineLogo.get_attribute("alt");
					else :
						if checkExistsByXpath(flight,".//div[@class='odf-grid-col odf-col-span1 odf-tooltip-container odf-text-mono-color-03 hover-active-tooltip od-primary-info-airline ficon-condensed']"):
							airline="*Multiples*";

					print("airline = "+airline)
					print("airlineSrc = "+airlineSrc)
						
					cities=flight.find_element_by_xpath(".//div[@class='odf-row odf-text-sm od-primary-flight-info-cities hover-active-tooltip odf-text-mono-color-03 flight_info_cities odf-text-nowrap']").text;
					print("cities = "+cities)
					fromAirport=cities.split('(')[1].split(')')[0]
					toAirport=cities.split('(')[2].split(')')[0]
					print("fromAirport = "+fromAirport)
					print("toAirport = "+toAirport+"\n")
					trip=Trip(fromAirport,toAirport,duration,departureTime,arrivalTime,airline,airlineSrc,stopNumber)
					if wayId=="1":
						OneWayTrips.append(trip)
					elif wayId=="2":
						ReturnTrips.append(trip)				
			price=element.find_element_by_xpath(".//div[@class='od-price-container  ']").text.replace(" ", "").replace("*", "");
			currency=price[0:1]
			price=price[1:]
			print("currency = "+currency)
			print("price = "+price)
			for OneWayTrip in OneWayTrips :
				if len(ReturnTrips)>0 :
					for ReturnTrip in ReturnTrips :
						InsertTrip(searchTripProviderId,price,currency,url,OneWayTrip,ReturnTrip)
		else:
			print("Train spotted")

		print("*** End study element ***\n")
	except Exception:
		LogError(traceback,"url = "+url+" and element = "+element.text+" and fromDate = "+fromDate+" and toDate = "+toDate+" and searchTripProviderId = "+searchTripProviderId)
	return
	
	
	

