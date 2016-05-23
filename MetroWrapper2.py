
from bs4 import BeautifulSoup;

import urllib2;

url = 'http://www.wmata.com/rider_tools/pids/showpid.cfm?station_id=42';

page = urllib2.urlopen(url);

soup = BeautifulSoup(page.read());


tables = soup.find_all("tbody");

for table in tables:
	for row in table.find_all("tr"):
		cellsInCurrentRow = row.find_all('td');
		try:
			line_color=cellsInCurrentRow[0].img.get("alt");
			print line_color;
			number_of_cars = cellsInCurrentRow[1].string;
			print number_of_cars;
			destination = cellsInCurrentRow[2].string;
			print destination;

			minutes_to_arrival = int(cellsInCurrentRow[3].string);
			print minutes_to_arrival;
			print;
		except:
			print "Skipped empty row";
			print;
