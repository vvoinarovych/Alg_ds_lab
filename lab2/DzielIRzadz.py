#Zadanie 3
def najwiekszyElementWektora(wektor):
    # Sprawdzamy, czy wektor jest pusty
    if len(wektor) == 0:
        return None

    # Sprawdzamy, czy wektor zawiera tylko jeden element
    if len(wektor) == 1:
        return wektor[0]

    # Dzielimy wektor na dwie części
    srodek = len(wektor) // 2
    lewaCzesc = wektor[:srodek]
    prawaCzesc = wektor[srodek:]

    # Rekurencyjnie sukamy największy element w obu częściach
    najwiekszyL = najwiekszyElementWektora(lewaCzesc)
    najwiekszyP = najwiekszyElementWektora(prawaCzesc)

    # Porównaj wyniki i zwróć większy element
    return max(najwiekszyL, najwiekszyP)


wektor = [4, 9, 2, 6, 5, 1, 8, 3, 7]
najwiekszy = najwiekszyElementWektora(wektor)
print("Największy element wektora:", najwiekszy)


#Zadanie 4
def obliczSume(tablica):
    # Sprawdzamy, czy tablica jest pusta
    if len(tablica) == 0:
        return 0

    # Sprawdzamy, czy tablica zawiera tylko jeden element
    if len(tablica) == 1:
        return tablica[0]

    # Dzielimy tablicę na dwie części
    srodek = len(tablica) // 2
    lewaCzesc = tablica[:srodek]
    prawaCzesc = tablica[srodek:]

    # Oblicz sumę pierwszej połowy rekurencyjnie
    sumaLewa = obliczSume(lewaCzesc)

    # Oblicz sumę drugiej połowy rekurencyjnie
    sumaPrawa = obliczSume(prawaCzesc)

    # Zsumuj obie części i zwróć wynik
    return sumaLewa + sumaPrawa

tablica = [1, 2, 3, 4, 5]
suma = obliczSume(tablica)
print("Suma elementów w tablicy:", suma)
