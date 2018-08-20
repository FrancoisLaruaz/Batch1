import pypyodbc
from DBConnection.SQLConnect import *
from Logger.logger import *

def SetTripProviderAsSuccess(searchTripProviderId):
	returnvalue=0
	try: 
		ExecuteQuery("update dbo.SearchTripProvider set SearchSuccess=1 where id="+searchTripProviderId)
	except Exception:
		LogError(traceback,"searchTripProviderId = "+searchTripProviderId)	
	return 

def InsertTrip(searchTripProviderId,price,currency,url,OneWayTrip,ReturnTrip):
	returnvalue=0
	try: 
		returnvalue=CallStoredProc('[dbo].[InsertTripWithTransaction]',searchTripProviderId,price.replace(',',''),currency,url,OneWayTrip.fromAirportCode,OneWayTrip.toAirportCode,OneWayTrip.departureDate,OneWayTrip.arrivalDate,OneWayTrip.duration,OneWayTrip.airlineName,OneWayTrip.airlineLogo,OneWayTrip.stops,ReturnTrip.fromAirportCode,ReturnTrip.toAirportCode,ReturnTrip.departureDate,ReturnTrip.arrivalDate,ReturnTrip.duration,ReturnTrip.airlineName,ReturnTrip.airlineLogo,ReturnTrip.stops)
	except Exception:
		LogError(traceback,"searchTripProviderId = "+searchTripProviderId+" and fromDate =" +fromDate+" and  toDate = "+toDate+" and  price = "+price+" and url = "+url)	
	return returnvalue