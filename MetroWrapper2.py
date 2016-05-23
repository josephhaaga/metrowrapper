from firebase import firebase;
from bs4 import BeautifulSoup;
import sys;
import urllib2;
import datetime;
import time;

stations = {
	'Addison Road-Seat Pleasant':92,
	'Anacostia':85,
	'Archives-Navy Memorial-Penn Quarter':81,
	'Arlington Cemetery':42,
	'Ballston-MU':99,
	'Benning Road':90,
	'Bethesda':12,
	'Braddock Road':47,
	'Branch Ave':89,
	'Brookland-CUA':27,
	'Capitol Heights':91,
	'Capitol South':59,
	'Cheverly':66,
	'Clarendon':97,
	'Cleveland Park':8,
	'College, Park-U of MD':79,
	'Columbia Heights':75,
	'Congress Heights':86,
	'Court House':96,
	'Crystal City':45,
	'Deanwood':65,
	'Dunn Loring-Merrifield':102,
	'Dupont Circle':6,
	'East, Falls Church':100,
	'Eastern Market':60,
	'Eisenhower Avenue':49,
	'Farragut North':4,
	'Farragut, West':38,
	'Federal Center SW':58,
	'Federal Triangle':53,
	'Foggy Bottom-GWU':40,
	'fb':40,
	'Forest Glen':32,
	'Fort Totten':28,
	'Franconia-Springfield':95,
	'Friendship Heights':11,
	'Gallery Pl-Chinatown':21,
	'Georgia Ave-Petworth':76,
	'Glenmont':34,
	'Greenbelt':80,
	'Greensboro':113,
	'Grosvenor-Strathmore':14,
	'Huntington':50,
	'Judiciary Square':23,
	'King St-Old Town':48,
	'LEnfant Plaza':82,
	'Landover':67,
	'Largo Town Center':109,
	'McLean':111,
	'McPherson Square':36,
	'Medical Center':13,
	'Metro Center':1,
	'Minnesota, Ave':64,
	'Morgan Boulevard':110,
	'Mt Vernon Sq 7th St-Convention Center':70,
	'Navy Yard-Ballpark':84,
	'Naylor Road':87,
	'New Carrollton':68,
	'NoMa-Gallaudet U':108,
	'Pentagon':43,
	'Pentagon City':44,
	'Potomac Ave':61,
	'Prince Georges Plaza':78,
	'Rhode Island Ave-Brentwood':26,
	'Rockville':17,
	'Ronald Reagan Washington National Airport':93,
	'Rosslyn':41,
	'Shady Grove':18,
	'Shaw-Howard U':72,
	'Silver Spring':31,
	'Silver Spring Transit Center':122,
	'Smithsonian':54,
	'Southern Avenue':107,
	'Spring Hill':114,
	'Stadium-Armory':63,
	'Suitland':88,
	'Takoma':29,
	'Tenleytown-AU':10,
	'Twinbrook':16,
	'Tysons Corner':112,
	'U Street/African-Amer Civil War Memorial/Cardozo':73,
	'Union Station':25,
	'Van Dorn Street':94,
	'Van Ness-UDC':9,
	'Vienna,/Fairfax-GMU':103,
	'Virginia Square-GMU':98,
	'Waterfront':83,
	'West Falls Church-VT/UVA':101,
	'West Hyattsville':77,
	'Wheaton':33,
	'White Flint':15,
	'Wiehle-Reston East':115,
	'Woodley Park-Zoo/Adams Morgan':7,
}

firebase = firebase.FirebaseApplication('https://flickering-heat-5765.firebaseio.com', None)

url = 'http://www.wmata.com/rider_tools/pids/showpid.cfm?station_id='+str(stations[sys.argv[1]]);

page = urllib2.urlopen(url);
ts=time.time();
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S');
soup = BeautifulSoup(page.read());

current_station=sys.argv[1];
print current_station;


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
			trains.append({'line':line_color,'number_of_cars':number_of_cars,'destination':destination,'minutes_to_arrival':minutes_to_arrival,'time':st,'current_station':current_station});
		except:
##			print "Skipped empty row";
			print;

for train in trains:
	print train;
	result = firebase.post('/trains/'+str(current_station), train);
