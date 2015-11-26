MetroWrapper
Joseph Haaga 2015

A simple Python wrapper for the WMATA Real-Time train Arrivals.
(http://www.wmata.com/rider_tools/pids/real_time_arrivals.cfm)

Done
- HTTP Request station info
- gather dictionary of station/id pairs

To Do
- parse http response
- finish CLI
	- write aliases (run CLI on Foggy Bottom station w/ 'metro fb')

Methods:
	getNextTrains(station) 
	handleResponse(response_text) ~INCOMPLETE
