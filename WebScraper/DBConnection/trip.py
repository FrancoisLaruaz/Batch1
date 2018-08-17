import pypyodbc
from DBConnection.SQLConnect import *
from Logger.logger import *

def InsertTrip(provider,fromDate,toDate,price,url,OneWayTrip,ReturnTrip):
	returnvalue=0
	try:
		#query="execute [dbo].[InsertTripWithTransaction] '"+provider+"', '"+fromDate"', '"+toDate+"', '"+price+"'"+"', '"+url+"'"
		#query=query+", '"+fromDate+"'"
		#print(query) 
		returnvalue=CallStoredProc('[dbo].[InsertTripWithTransaction]',provider,fromDate,toDate,price,url,OneWayTrip.fromAirportCode,OneWayTrip.toAirportCode,OneWayTrip.departureDate,OneWayTrip.arrivalDate,OneWayTrip.duration,OneWayTrip.airlineName,OneWayTrip.airlineLogo,OneWayTrip.stops)
		#ExecuteQuery(query)
	except Exception:
		LogError(traceback,"provider = "+provider+" and fromDate =" +fromDate+" and  toDate = "+toDate+" and  price = "+price+" and url = "+url)	
	return returnvalue