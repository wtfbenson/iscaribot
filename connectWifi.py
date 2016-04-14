from wifi import Cell, Scheme

networks = Cell.all('wlan0')
for x in networks:
	if (getattr(x, "encrypted") == False):
		print x		

