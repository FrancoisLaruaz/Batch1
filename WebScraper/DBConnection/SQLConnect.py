import pypyodbc
from Logger.logger import *

#connection_string ='Driver={SQL Server Native Client 11.0};Server=LAPTOP-F614BEV0;Database=Template;Trusted_Connection=Yes;'
connection_string ='Driver={SQL Server Native Client 11.0};Server=.;Database=Template;Trusted_Connection=Yes;'

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
		LogError(''.join(traceback.format_exc()),query)	
	return