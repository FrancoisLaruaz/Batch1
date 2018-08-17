import pypyodbc
from DBConnection.SQLConnect import *
from Logger.logger import *

def InsertTrip(provider,fromDate,toDate,price,url,OneWayTrip,ReturnTrip):
	returnvalue=0
	try:
		#query="execute [dbo].[InsertTripWithTransaction] '"+provider+"', '"+fromDate"', '"+toDate+"', '"+price+"'"+"', '"+url+"'"
		#query=query+", '"+fromDate+"'"
		#print(query) 
		returnvalue=CallStoredProc('[dbo].[InsertTripWithTransaction]',provider)
		#ExecuteQuery(query)
	except Exception:
		LogError(traceback,"provider = "+provider+" and fromDate =" +fromDate+" and  toDate = "+toDate+" and  price = "+price+" and url = "+url)	
	return returnvalue