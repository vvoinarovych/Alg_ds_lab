#Zadanie 1
def fibonacci(n):
    # Tworzymy tablicę dla przechowywania obliczonych elementów ciągu
    fibTable = [0] * (n + 1)

    # Bazowe przypadki
    fibTable[0] = 0
    fibTable[1] = 1

    # Obliczamy kolejne elementy ciągu
    for i in range(2, n + 1):
        fibTable[i] = fibTable[i - 1] + fibTable[i - 2]

    return fibTable[n]

n = 10
wynik = fibonacci(n)
print("Element", n, "ciągu Fibonacciego:", wynik)


#Zadanie 3
def oblicz(n):
    # Tworzymy tablicę dla przechowywania obliczonych wartości
    wyrazy = [0] * (n + 1)

    # Bazowe przypadki
    wyrazy[0] = 1
    wyrazy[1] = 1

    # Obliczamy kolejne wyrazy
    for i in range(2, n + 1):
        wyrazy[i] = 2 * wyrazy[i - 1] - wyrazy[i - 2]

    return wyrazy[n]

n = 5
wynik = oblicz(n)
print("Wyraz", n, "ciągu:", wynik)


#Zadanie 4
def wspolczynnikDwumianowy(n, m):
    # Twórzymy tablicę dwuwymiarową i wypełniamy ją wartościami 0
    tablica = [[0] * (m+1) for _ in range(n+1)]

    # Ustawiamy wartości na głównej przekątnej na 1
    for i in range(n+1):
        tablica[i][0] = 1

    # Obliczamy wartości dla pozostałych elementów tablicy
    for i in range(1, n+1):
        for j in range(1, m+1):
            tablica[i][j] = tablica[i-1][j-1] + tablica[i-1][j]

    return tablica[n][m]

n = 5
m = 2
wynik = wspolczynnikDwumianowy(n, m)
print("Współczynnik dwumianowy dla n =", n, "i m =", m, "wynosi:", wynik)

