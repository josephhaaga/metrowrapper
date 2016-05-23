from firebase import firebase;
from bs4 import BeautifulSoup;
import sys;
import urllib2;

url = 'http://www.wmata.com/rider_tools/pids/showpid.cfm?station_id=42';

page = urllib2.urlopen(url);

soup = BeautifulSoup(page.read());


tables = soup.find_all("tbody");
print "Metro train arrivals";
trains = [];
for table in tables:
	for row in table.find_all("tr"):
		cellsInCurrentRow = row.find_all('td');
		try:
			line_color=cellsInCurrentRow[0].img.get("alt");
			number_of_cars = cellsInCurrentRow[1].string;
			destination = cellsInCurrentRow[2].string;
			minutes_to_arrival = int(cellsInCurrentRow[3].string);
##			print;
			trains.append({'line':line_color,'number_of_cars':number_of_cars,'destination':destination,'minutes_to_arrival':minutes_to_arrival});
		except:
##			print "Skipped empty row";
			# print;

for train in trains:
	print train;
