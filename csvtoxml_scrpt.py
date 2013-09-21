import csv
with open('cta_L_stops.csv', newline='') as f:
	reader = csv.reader(f)
	stopsRed = ['Howard','Jarvis','Morse','Loyola','Granville','Thorndale','Bryn Mawr','Berwyn','Argyle','Lawrence','Wilson','Sheridan','Addison','Belmont','Fullerton','North/Clybourn','Clark/Division','Chicago','Grand','Lake','Monroe','Jackson','Harrison','Roosevelt','35th-Bronzeville-IIT','Indiana','43rd','47th','51st','Garfield','Halsted','Ashland/63rd']
	stopsBlue = ['O\'Hare','Rosemont','Cumberland','Harlem','Jefferson Park','Montrose','Irving Park','Addison','Belmont','Logan Square','California','Western','Damen','Division','Chicago','Grand','Clark/Lake','Washington','Monroe','Jackson','LaSalle','Clinton','UIC-Halsted','Racine','Illinois Medical District','Western','Kedzie-Homan','Pulaski','Cicero','Austin','Oak Park','Harlem','Forest Park']
	stopsBrn = ['Kimball','Kedzie','Francisco','Rockwell','Western','Damen','Montrose','Irving Park','Addison','Paulina','Southport','Belmont','Wellington','Diversey','Fullerton','Armitage','Sedgwick','Chicago','Merchandise Mart','Washington/Wells','Quincy/Wells','LaSalle/Van Buren','Harold Washington Library-State/Van Buren','Adams/Wabash','Madison/Wabash','Randolph/Wabash','State/Lake','Clark/Lake']
	stopsG = ['Harlem/Lake','Oak Park','Ridgeland','Austin','Central','Laramie','Cicero','Pulaski','Conservatory','Kedzie','California','Ashland','Morgan','Clinton','Washington/Wells','Quincy/Wells','LaSalle/Van Buren','Harold Washington Library-State/Van Buren','Clark/Lake','State/Lake','Randolph/Wabash','Madison/Wabash','Adams/Wabash','Roosevelt','35th-Bronzeville-IIT','Indiana','43rd','47th','51st','Garfield','King Drive','Cottage Grove']
	stopsOrg = ['Midway','Pulaski','Kedzie','Western','35th/Archer','Ashland','Halsted','Roosevelt','Harold Washington Library-State/Van Buren','LaSalle/Van Buren','Quincy/Wells','Washington/Wells','Clark/Lake','State/Lake','Randolph/Wabash','Madison/Wabash','Adams/Wabash']
	stopsP = ['Linden','Central','Noyes','Foster','Davis','Dempster','Main','South Boulevard','Howard','Belmont','Wellington','Diversey','Fullerton','Armitage','Sedgwick','Chicago','Merchandise Mart','Clark/Lake','State/Lake','Randolph/Wabash','Madison/Wabash','Adams/Wabash','Harold Washington Library-State/Van Buren','LaSalle/Van Buren','Quincy/Wells','Washington/Wells']
	stopsPink = ['54th/Cermak','Cicero','Kostner','Pulaski','Central Park','Kedzie','California','Damen','18th','Polk','Ashland','Morgan','Clinton','Clark/Lake','State/Lake','Randolph/Wabash','Madison/Wabash','Adams/Wabash','Harold Washington Library-State/Van Buren','LaSalle/Van Buren','Quincy/Wells','Washington/Wells']
	stopsY = ['Skokie','Oakton-Skokie','Howard']
	print('Red stops:',len(stopsRed))
	print('Blue stops:',len(stopsBlue))
	print('Brown stops:',len(stopsBrn))
	print('Green stops:',len(stopsG))
	print('Orange stops:',len(stopsOrg))
	print('Purple stops:',len(stopsP))
	print('Pink stops:',len(stopsPink))
	print('Yellow stops:',len(stopsY))
	indices = []
	row1 = reader.__next__()
	indices.append(row1.index('LAT'))
	indices.append(row1.index('LON'))
	indices.append(row1.index('STATION_NAME'))
	indices.append(row1.index('PARENT_STOP_ID'))
	print(indices)
	f.seek(0)
	for stop in stopsY:
		for row in reader:
			if stop == row[indices[2]]:
				print(row[indices[2]],row[indices[3]],row[indices[0]],row[indices[1]])
				f.seek(0)
				break
		else:
			print(stop,'does not exist!')
#for row in reader:
#    print row
#print(len(stops))