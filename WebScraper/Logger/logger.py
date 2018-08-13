import os
import sys
from datetime import datetime, timezone
import traceback

from DBConnection.SQLConnect import *

def LogError(error,details=""):
   print ("ERROR CATCHED : "+error+"| details = "+details)
   date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
   query = """INSERT INTO [dbo].[Log4Net]
           ([Thread]
           ,[Level]
           ,[Logger]
           ,[Message]
           ,[Exception]
           ,[UserLogin]
		   ,[Date])
     VALUES
           (1
           ,'ERROR'
           ,'PYTHON ERROR'
           ,'"""+details.replace("'","''")[:8000]+"','"+error.replace("'","''")[:5000]+"','***Batch***','"+date.replace("'","''")+".000')"
   ExecuteQuery(query)
   return

