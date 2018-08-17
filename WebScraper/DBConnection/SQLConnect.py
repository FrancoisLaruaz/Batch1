import pypyodbc
from Logger.logger import LogError
from Helper.constants import *
import traceback

def ExecuteQuery(query):
	try:
		connection = pypyodbc.connect(connection_string)
		cur = connection.cursor()
		cur.execute(query)
		cur.commit()
		cur.close()
		connection.close()
	except Exception:
		print(''.join(traceback.format_exc())+" and query = "+query)	
		LogError(traceback,"query = "+query)	
	return
	
def CallStoredProc(procName, *args):
	returnvalue=0
	try:
		connection = pypyodbc.connect(connection_string)
		cur = connection.cursor()
		sql = """SET NOCOUNT ON;
		DECLARE @ret int
		EXEC  @ret = %s %s
		SELECT @ret""" % (procName, ','.join(['?'] * len(args)))
		returnvalue=int(cur.execute(sql, args).fetchone()[0])
		cur.commit()
		cur.close()
		connection.close()
		print(procName+" executed | returnvalue = "+str(returnvalue))
	except Exception:	
		LogError(traceback,"procName = "+procName+" and args = "+''.join(str(e) for e in args))	
	return returnvalue