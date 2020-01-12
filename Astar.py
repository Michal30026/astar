import time
from queue import PriorityQueue

def pobierz_wejscie():

	wczytane = open('wejscie.txt').read().split('\n')[:-1]
	
	poczatek = wczytane[0].split()
	koniec   = wczytane[1].split()
	
	poczatek = (
		int(poczatek[0]),
		int(poczatek[1]) 
	)
	
	koniec = (
		int(koniec[0]),
		int(koniec[1])
	)
    
	return (
		poczatek,
		koniec,
		wczytane[2:]
	)

def legalna_pozycja(pozycja, mapa):
	
	if pozycja[0] < 0 or pozycja[1] < 0:
		return False
	if pozycja[0] >= len(mapa):
		return False
	if pozycja[1] >= len(mapa[0]):
		return False
	
	return mapa[pozycja[0]][pozycja[1]] == '0'	


def wykonaj_algorytm():
	
	poczatek, koniec, mapa = pobierz_wejscie()	
	
	kolejka     = PriorityQueue()
	odwiedzone  = set()
	poprzednicy = dict()
	
	# na kolejce -> (dystans + h_value(), pozycja)
	kolejka.put((-100, 0, poczatek))	
	while not kolejka.empty():
		
		top = kolejka.get()	
		dystans = top[1]
		pozycja = top[2]
	
		if pozycja == koniec:
			break
		
		if pozycja not in odwiedzone:
        
			odwiedzone.add(pozycja)
			
            # gora, dol, prawa, lewa
			for kierunek in [(-1, 0), (1, 0), (0, 1), (0, -1)]:

				nowa_pozycja = (
					pozycja[0] + kierunek[0],
					pozycja[1] + kierunek[1]
				)
				if legalna_pozycja(nowa_pozycja, mapa):
				
					if nowa_pozycja not in odwiedzone:
						
						poprzednicy[nowa_pozycja] = pozycja

						kolejka.put((
							dystans + 1 +                     
							abs(koniec[0] - nowa_pozycja[0]) + 
							abs(koniec[1] - nowa_pozycja[1]),
							dystans + 1,
							nowa_pozycja                      
						))
	

	print('Odwiedzone pola zaznaczone @.')
	for i in range(len(mapa)):
		wiersz = ''
		for j in range(len(mapa[0])):
			
			pozycja = (i, j)
			if pozycja in odwiedzone:
				wiersz += '@'
			else:
				wiersz += mapa[i][j]
			
		print(wiersz)
	
				
	if koniec not in poprzednicy.keys():
		print('Nie można dojść do punktu koncowego')
		return
	
	
	wynik = []
	while koniec != poczatek:
		wynik.append(koniec)
		koniec = poprzednicy[koniec]
	wynik = [poczatek] + list(reversed(wynik))
	
	print('Sciezka:\n', wynik)
		
		
wykonaj_algorytm()
	
time.sleep(120)	
	
	
	
	
	
	

