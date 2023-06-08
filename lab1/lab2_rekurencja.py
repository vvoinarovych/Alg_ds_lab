#zadanie 1 (NWD)
#wersja1(nieoptynalna)

#iteracyjnie
def NWD_iter(a,b):
    while a!=b:
        if a>b: a = a-b
        else: b = b-a
    return a


#rekurencja
def NWD_rek(a,b):
    if a!=b:
        if a>b: return NWD_rek(a-b, b)
        else: return NWD_rek(a, b-a)
    return a


#wersja2(optymalna)
def NWD_iter2(a,b):
    while b!=0:
        temp = b
        b = a%b
        a = temp
    return a


def NWD_rek2(a,b):
    if b!=0:
        return NWD_rek2(b, a%b)
    return a

#Zadanie 3

def function(n):
    if n==1:
        return 4
    else:
        return 1/(1-function(n-1))
print("zadanie 3")
print(function(8))
print(function(9))
print(function(10))
print(function(100))

#Zadanie 4
def decimal_to_binary(n):
    if n <= 1:
        return str(n)
    else:
        return decimal_to_binary(n//2) + str(n%2)

print("zadanie 1")
print(NWD_iter(100,20))
print(NWD_rek(100,20))
print(NWD_iter2(101,20))
print(NWD_rek2(101,20))
print("zadanie 4")
print(decimal_to_binary(7))
print(decimal_to_binary(11))