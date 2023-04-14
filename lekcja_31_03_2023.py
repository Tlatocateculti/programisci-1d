liczby = []


def wykonaj_suma(tablica):
    suma = 0
    for i in range(len(tablica)):
        suma+=tablica[i]
    return suma
    pass

def wykonaj_roznica(tablica):
    suma = tablica[0]
    for i in range(1,len(tablica)):
        suma-=tablica[i]
    return suma
    pass

def wykonaj_iloczyn(tablica):
    suma = 1
    for i in range(len(tablica)):
        suma*=tablica[i]
    return suma
    pass

def wykonaj_iloraz(tablica):
    suma = tablica[0]
    if 0 in tablica:
        print("Nie można uzyskać wartości przy dzieleniu przez zero!")
        return 0
    for i in range(1,len(tablica)):
        suma/=tablica[i]
    return suma
    pass

while True:
    #wartosc -> pobranie z linii od użytkownika
    wartosc = float(input("Podaj dowolną liczbę, zero kończy działanie: "))
    if wartosc != 0:
        liczby.append(wartosc)
    #if warunek_kiedy_wartosc różna od zera:
    #    liczby.dodajemy(wartosc)
    else:
        #przerywamy działanie
        break

znak = input("Podaj działanie, które chcesz wykonać na liczbach (+,-,*,/): ")
wynik = 0
match (znak):
    case '+':
        wynik = wykonaj_suma(liczby)
    case '-':
        wynik = wykonaj_roznica(liczby)
    case '*':
        wynik = wykonaj_iloczyn(liczby)
    case '/':
        wynik = wykonaj_iloraz(liczby)
#jaką operację chcesz wykonać (+,-,*,/)
#wykonujemy operacje w petli na wszystkich elementach

#podajemy wynik
print(wynik)


#
#a = float(input("Podaj dowolną pierwszą liczbę: "))
#b = float(input("Podaj dowolną drugę liczbę: "))
#print("a + b =", a+b)
#print("a - b =", a-b)
#print("a * b =", a*b)
#print("a / b =", a/b)
