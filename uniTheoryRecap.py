# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 12:07:11 2022

@author: Rafał
"""

#University quick theory recap

#Podstawy Pythona
#Wyswietlanie wiadomosci
print("Hello")

# Zmienne 
i = 1 #int
d = 1.0 #float
s = "tekst" #string
b1 = True
b2 = False


#Wyswietlanie typów zmiennych
type(i)
type(d)
type(s)

#Zmiana typów zmiennych
f = float(i)
type(f)
ks = str(i)
type(ks)

#Zmienne w pythonie powinny być nazywane w systemie snake case. Nazwy zmiennych złożone z wielu słów powinny być 
#łączone przy użyciu znaku '_'"

#Wyswietlanie zmiennych w tekscie
print("Variable i is equal to {0}".format(i))
print("Variable i is equal to {0} and variable d is equal to {1}".format(i, d))
#lub
print("Variable i is equal to "+str(i)+" and variable d is equal to "+str(d))

#Operacje matematyczne
sums = i + i
subtraction = i - i
multiplication = i * i
Division = i/d

2 ** 3 #potęgowanie 
13 % 5 # reszta z dzielenia
13//5  #częsć całkowita z dzielenia

##############################################################################
#Instrukcje warunkowe
##Ważnym jest aby używać znaku ':' po warunku. 
##Python nie używa nawiastów. Zamiast tego stosowane są wcięcia. Należy zwracać uwaagę na spacje i tabulatory
if (i == 1):
    print("This is one")
elif (i > 1):
    print("This is more then one")
else:
    print("This is less then one")

#Różne operatory porównywania
if (i > 1):
    print("This is more than one")
else:
    print("This is less than or equal to one")

if (i >= 1):
    print("This is more than or equal to one")
else:
    print("This is less than one")

if (i != 2):
    print("This number is not equal to two")
else:
    print("This number is equal to two")

#Operacje logiczne
print((4>3) and (3>1))
print((4>3) and (0>1))
print((0>3) and (0>1))

print((4>3) or (3>1))
print((4>3) or (0>1))
print((0>3) or (0>1))

print(not 0>3)

##############################################################################
#Listy
lista = [] #pusta lista
#W jednej liscie mogą występować elementy róznych typów 
lista = [1, 2, 'a', [3, 4]]
type(lista)

len(lista) # Długosć listy

#Dostęp do poszczególnych wartosci
lista[0]
lista[3]

#Dostęp do ostatnich wartosci listy
lista[-1]
lista[-2]


#Rozszerzenie listy o element podany jako argument 
lista.append([5,6])

#Rozszerzenie listy o wiele elementów 
lista.extend([5,6])

#Zmiana wartosci na liscie
lista[0] = 10

#Krotki (tuples)
tup = (1,2,'a')
type(tup)

len(tup)

#Zmiana wartosci w krotce
tup[0] = 10 # Powinien wystąpić błąd. Nie można zmieniać elementu krotki

##############################################################################
#Słowniki 
dic = {0 : "zero", 1 : "one", 2 : "two"}

#Dostęp do wartosci
dic[0]
dic.get(0)

#Lista kluczy
dic.keys()

#Lista elementów
dic.items()

##############################################################################
#Pętle
#for
for i in range(5,10,2):
    print(i)

#Pętla po listach/krotkach
for i in range(0,len(lista)):
    print(lista[i])

for i in lista:
    print(i)

#Pętla po liscie z indeksem elementu
for i in enumerate(lista):
    print(i)
    
for idi, i in enumerate(lista):
    print("Wartosc dla indeksu {0} to {1}".format(idi, i))

#Pęta po wielu listach
l1 = [1, 2, 3]
l2 = [4, 5, 6]

for i in zip(l1, l2):
    print(i)

for i, j in zip(l1, l2):
    print("Z pierwszej tablicy: {0}".format(i))
    print("Z drugiej tablicy: {0}".format(j))

#Pętla po listach różnych rozmiarów
l1.append(9)
for i, j in zip(l1, l2):
    print("Z pierwszej tablicy: {0}".format(i))
    print("Z drugiej tablicy: {0}".format(j)) 

#while
i = 0
while(True):
    print(i)
    i = i + 1
    if (i>10):
        break

##############################################################################
#Lista atrybutów i metod w srodowisku roboczym
dir()

##############################################################################
#Definiowanie funkcji
def New_function():
    print("Hello")

#Wywołanie funkcji
New_function()

#Funkcja z parametrem
def square(x):
    return x*x

#Wywołanie funkcji z argumentem
square(4)

#Funkcja z parametrami domyslnymi
def power(x, w=2):
    return x**w

#Wywołanie funkcji z argumentami (i bez)
power(2,3)
power(8)

#Funkcaja zwracająca wiele wartosci
def following_powers(x):
    return x, x*x, x**3

zz = following_powers(2)
print(zz)
#Jaki jest typ zwróconej zmiennej

#kolejnosć domyslnych parametrów
def following_powers(x, w1=1, w2=2, w3=3):
    return x**w1, x**w2, x**w3

following_powers(2)

following_powers(2, 10) #jeżeli argumenty występują w takiej kolejnosci jak w definicji funkcji, nie trzeba podawać ich nazw

following_powers(2, w3=10) #jeżeli argumenty występują w innej kolejnosci niż w definicji funkcji, trzeba podawać ich nazwy

##############################################################################
#Klasy
class Rectangle:
    def __init__(self, a, b, co="Rectangle"): #Konstruktor
        self.a = a                          #pole
        self.b = b                          #pole
        self.name = co                      #pole
        
    def circuit(self, ):                   #metoda
        return self.a * self.b
    
    def obw(self, ):                    #metoda
        return self.a*2+self.b*2

#Tworzenie obiektu
pro = Rectangle(3,5)
        
#Wywołanie metod
pro.circuit()
pro.field()  

##############################################################################
#Import pakietów
#numpy
import numpy as np 

lis = [-1, 2, 4]

#Zmiana listy na tablice
tab = np.array(lis)
type(tab)

#Zmiana listy na tablice o okreslonym typie elementów
tab = np.array(lis, dtype=np.float)

#liczba elementów w tablicy ( również wielowymiarowej)
tab.size

#kształt tablicy
tab.shape

#Tworzenie tablicy kolejnych liczb
tab2 = np.arange(0, 100)

#Zmiana kształtu tablicy
tab2 = tab2.reshape((50, 2))
tab2.shape

#Dostęp do elementów tablicy wielowymiarowej 
tab2[1,1]
tab2[1][1]

#Dostęp do pojedynczego wiersza
tab2[1]

#Dosęp do zakresu wierszy
tab2[0:3]

#Dosęp do zakresu wierszy, tylko pierwsza kolumna
tab2[0:3, 0]

#Wyswietlenie wszystkich rekordów w pierwszej kolumnie
tab2[:, 0]

#Wyswietlenie wszystkich rekordów w ostatniej kolumnie
tab2[:, -1]

#Wyswietlenie ostatniej kolumny z zakresu ostatnich wierszy 
tab2[-10:-1, -1]


#Wybrane operacje arytmentyczne zwracające tablice
np.abs(tab) #wartosci bezwzględne elementów
np.power(tab,2) #potęgi elementów
np.cumsum(tab) #Kolejne sumy elementów w tablicy

#Wybrane operacje na tablicahc zwracające liczbę
np.sum(tab)     #Suma elementów tablicy
np.prod(tab)    #Iloczyn elementów tablicy

#Tworzenie 100 elementowej tablicy równo oddalonych liczby w zakresie od 10 do 20
np.linspace(10, 20, 100)

#Generowanie całkowitych liczb losowych
np.random.randint(0, 10)

#Generowenie trzech liczb losowych z zakresu od 0 do 9
np.random.randint(0, 10, 3)

#Generowanie liczby losowej pomiędzy 0 a 1
np.random.random()

#Tworzenie tablic liczb losowych
np.random.random_sample(10)
np.random.random_sample((10,2))

#Tworzenie 5 elementowej tablicy złożonej z samych zer
np.zeros(5)

#Tworzenie 5 elementowej tablicy złożonej z samych jedynek
np.ones(5)

#Tworzenie 2 wymiarowej tablicy z 10 elementami w pierwszej osi i 5 w drugiej złożonej z samych zer
np.zeros((10, 5))
np.zeros(50).reshape((10, 5))


temp = np.random.randint(0, 8, 20)
#Tablica unikalnych wartosci w tablicy temp
np.unique(temp)

#Maksymalna wartosć tablicy
np.max(temp)

#Indeks maksymalnej wartosci tablicy
np.argmax(temp)

#Iloczyn kartezjański dwóch wektorów (tablic)
np.dot([1, 2, 3], [2, 3, 4])
np.inner([1, 2, 3], [2, 3, 4])

#Brakujące wartosci
np.NaN
np.nan

#Tablica stworzona z powtórzeń każdej wartosci 3 razy
np.repeat([1,2,3], 3)

#Tablica stworzona z 3 kronego powtórzenia całej tabliby
np.tile([1,2,3], 3)

#praca z plikami
#Zapis do pliku
file = open("nazwa_pliku.txt", 'w')
file.write("To działa")
file.close()

#Zapis do pliku z kodowaniem
file = open("nazwa_pliku.txt", 'w', encoding="utf-8")
file.write("To działa")
file.close()

#Dopisywanie do pliku z kodowaniem
file = open("nazwa_pliku.txt", 'a')
file.write("To dopisuje")
file.close()

#Odczyt z pliku 
file = open("nazwa_pliku.txt", 'r')
s=file.read()
file.close()

#Odczyt z pliku z kodowaniem
file = open("nazwa_pliku.txt", 'r', encoding="utf-8")
s=file.read()
file.close()

# Operacja z wieloma liniami
file = open("nazwa_pliku.txt", 'w')
file.write("Linia 1 \n Linia 2")
file.close()

#Odczyt całego pliku
file = open("nazwa_pliku.txt", 'r', encoding="utf-8")
s=file.read()
file.close()
print(s)

#Odczyt pojedynczej lini
file = open("nazwa_pliku.txt", 'r', encoding="utf-8")
s=file.readline()
file.close()
print(s)

#Odczyt listy linii
file = open("nazwa_pliku.txt", 'r', encoding="utf-8")
s=file.readlines()
file.close()
print(s)

#Zapis zmiennej ndarray
#do pliku tekstowego
temp = np.random.randint(0, 8, 20)
np.savetxt('plik.txt', temp)
#do pliku .npy
np.save("plik", temp)
#odczyt .npy
reload = np.load("plik.npy")

#bibliotego do wykresów
import matplotlib.pyplot as plt 

#Wykres liniowy
ax_x = np.linspace(-5, 5, 100)
ax_y = np.power(ax_x, 2)
plt.plot(ax_x, ax_y)

#Wykres liniowy z legendą
ax_x = np.linspace(-5, 5, 100)
ax_y1 = np.power(ax_x, 2)
ax_y2 = np.power(ax_x, 3)
plt.plot(ax_x, ax_y1, label="second power")
plt.plot(ax_x, ax_y2, label="third power")
plt.legend()

#Wykres rozrzutu
os_x = np.random.sample(100)
os_y = np.random.sample(100)
plt.scatter(os_x, os_y)