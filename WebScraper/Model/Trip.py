class Trip(object):
	def __init__(self, fromAirportCode,toAirportCode,duration,fromDate,toDate,airlineName,airlineLogo,stops):
		self.fromAirportCode = fromAirportCode
		self.toAirportCode= toAirportCode
		self.duration=duration
		self.fromDate=fromDate
		self.toDate=toDate
		self.airlineName=airlineName
		self.airlineLogo=airlineLogo
		self.stops=stops
