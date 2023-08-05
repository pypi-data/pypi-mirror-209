# klasa która pobiera wartości i wypisuje ją

import random
import math


class ExamAngel:
    def __init__(self):
        self.x = 1
        self.y = 2

    def dodaj(self):
        return self.x + self.y


def czy_pierwsza(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def napisz_czy_pierwsza():
    print("""def czy_pierwsza(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True""")
    errors()


def dzielniki(n):
    dzielniki = []
    if n < 1:
        return dzielniki
    for i in range(1, n + 1):
        if n % i == 0:
            dzielniki.append(i)
    return dzielniki


def napisz_dzielniki():
    print("""def dzielniki(n):
    dzielniki = []
    if n < 1:
        return dzielniki
    for i in range(1, n + 1):
        if n % i == 0:
            dzielniki.append(i)
    return dzielniki""")
    errors()


def dzielniki_pierwsze(n):
    dzielniki = []
    if n < 2:
        return dzielniki
    for i in range(2, n + 1):
        if n % i == 0 and czy_pierwsza(i):
            dzielniki.append(i)
    return dzielniki


def napisz_dzieliki_pierwsze():
    print("""def dzielniki_pierwsze(n):
    dzielniki = []
    if n < 2:
        return dzielniki
    for i in range(2, n + 1):
        if n % i == 0 and czy_pierwsza(i):
            dzielniki.append(i)
    return dzielniki""")
    errors()


def najwiekszy_wspolny_dzielnik(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def napisz_najwiekszy_wspolny_dzielnik():
    print("""def najwiekszy_wspolny_dzielnik(a, b):
    while b != 0:
        a, b = b, a % b
    return a""")
    errors()


def najmniejsza_wspolna_wielokrotnosc(a, b):
    nwd = najwiekszy_wspolny_dzielnik(a, b)
    return (a * b) // nwd


def napisz_najmniejsza_wspolna_wielokrotnosc():
    print("""def najmniejsza_wspolna_wielokrotnosc(a, b):
    nwd = najwiekszy_wspolny_dzielnik(a, b)
    return (a * b) // nwd""")
    errors()


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def napisz_fibonacci():
    print("""def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)""")
    errors()


def fibonacci_array(n):
    fib_array = []
    for i in range(n):
        fib_array.append(fibonacci(i))
    return fib_array


def napisz_fibonacci_array():
    print("""def fibonacci_array(n):
    fib_array = []
    for i in range(n):
        fib_array.append(fibonacci(i))
    return fib_array""")
    errors()


def otworz_plik():
    print("""tab = []
with open('plik.txt', 'r') as f:
    for line in f:
        tab.append(line.strip())
print(tab)""")
    errors()


def zapisz_do_pliku():
    print("""with open('wynik4.txt', 'w/a') as f:
    f.write(f'''Zadanie 4.3:\n''')
    f.write(f'''{zmienna}, {zmienna}\n''')""")
    errors()


def tablice():
    print("""    print(arr[::2]) # co drugi element
    print(arr[::3]) # co trzeci element
    print(arr[2:6:1]) # od 2 do 6 co 1
    print('kajak'[::-1] == 'kajak')

# pop -> wyciąga i usuwa element z listy
# insert -> wstawia element na danym indexie
# index -> na jakim indexie wstępuje podana wartość, UWAGA błędy gdy wartości nie ma
# remove -> usuwa dany element na podstawie wartości
# copy -> kopia listy nie jest związana z pierwotną""")
    errors()


def zbory():
    print("""# zbiory - set - nieuporządkowane, niepowtarzalne elementy
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4}
# część wspólna zbiorów, ogólnie działania na zbiorach
print(set1.intersection(set2))""")
    errors()


def slowniki():
    print("""# słowniki - dict
dict1 = {'a': 1, 'b': 2, 'c': 3}
print(dict1['a'])
dict1['d'] = 4
print(dict1)
print(dict1.keys())
print(dict1.values())
for key in dict1:
    print(key, dict1[key])""")
    errors()


def ile_liter():
    print("""losowy_ciag = 'ATAAKBTMX'
litery = {}
for litera in losowy_ciag:
    litery[litera] = 0

for litera in losowy_ciag:
    litery[litera] += 1

print(litery)
""")
    errors()


def matematyka():
    print("""min(1, 2, 3) | max(1, 2, 3) | abs(-5) | sum([1, 2, 3])
math.sqrt(4) | math.pow(2, 3) | math.log(2, 2) | math.factorial(5)
round(3.141592, 2) | math.floor(3.141592) | math.ceil(3.141592)
math.gcd(4, 6) #największy wspólny dzielnik
math.lcm(4, 6) # najmniejsza wspólna wielokrotność
math.dist((0, 0), (3, 4)) # odległość między punktami w przestrzeni kartezjańskiej""")
    errors()


def systemy_liczbowe():
    print("""bin -> dz
int('101', 2) | bin(5)  na bin
int('11', 8) | oct(10) na oct
int('11', 16) | hex(10)  na hex
print(str(bin(5))[2:])""")
    errors()


def stringi():
    print("""ascii od 65 do 90
print(ord('a'))  # zamiana znaku na kod ASCII
print(chr(97))  # zamiana kodu ASCII na znak

x = 'Ala ma kota'
x[2:8]  # a ma k
x[2:8:2]  # am
x[-1:-7:-1]  # atok a
x[::-1]  # atok am alA
x[::]  # Ala ma kota""")
    errors()


def errors():
    prints = [
        """Traceback (most recent call last):
  File 'c:\\Users\\Egzamin\\Pulpit\\EGZAMIN\\egzamin.py', line 13, in <module>
    intiger = int(string)
ValueError: invalid literal for int() with base 10: '011001'
                                                    ^^^^^^^^
SyntaxError: invalid syntax""",
        """Traceback (most recent call last):
  File 'example.py', line 27, in <module>
    result = 10 / 0
ZeroDivisionError: division by zero""",
        """Traceback (most recent call last):
  File 'main.py', line 42, in <module>
    value = my_dict['key']
KeyError: 'key'""",
        """Traceback (most recent call last):
  File 'script.py', line 15, in <module>
    index = my_list[10]
IndexError: list index out of range""",
        """Traceback (most recent call last):
  File 'module.py', line 55, in <module>
    open(file_name, 'r')
FileNotFoundError: [Errno 2] No such file or directory: 'myfile.txt'""",
        """Traceback (most recent call last):
  File 'code.py', line 34, in <module>
    import non_existent_module
ModuleNotFoundError: No module named 'non_existent_module'""",
        """Traceback (most recent call last):
  File 'program.py', line 21, in <module>
    raise Exception("Custom error message")
Exception: Custom error message""",
        """Traceback (most recent call last):
  File 'app.py', line 16, in <module>
    value = int('abc')
ValueError: invalid literal for int() with base 10: 'abc'""",
        """Traceback (most recent call last):
  File 'script.py', line 8, in <module>
    name = unknown_variable
NameError: name 'unknown_variable' is not defined""",
        """Traceback (most recent call last):
  File 'file.py', line 12, in <module>
    json_data = json.loads(invalid_json)
JSONDecodeError: Expecting property name enclosed in double quotes: line 2 column 3 (char 4)"""
    ]

    random_print = random.choice(prints)
    print(random_print)


def licz_wystapienia(napis):
    wystapienia = {}
    for znak in napis:
        if znak not in wystapienia:
            wystapienia[znak] = 1
        else:
            wystapienia[znak] += 1
    return wystapienia


def napisz_licz_wystapienia():
    print("""def licz_wystapienia(napis):
    wystapienia = {}
    for znak in napis:
        if znak not in wystapienia:
            wystapienia[znak] = 1
        else:
            wystapienia[znak] += 1
    return wystapienia""")
    errors()


def sprawdz_palindrom(napis):
    napis = napis.lower()
    napis = ''.join(e for e in napis if e.isalnum())
    odwrocony_napis = napis[::-1]
    return napis == odwrocony_napis


def napisz_sprawdz_palindrom():
    print("""def sprawdz_palindrom(napis):
    napis = napis.lower()
    napis = ''.join(e for e in napis if e.isalnum())
    odwrocony_napis = napis[::-1]
    return napis == odwrocony_napis""")
    errors()


def sprawdz_anagram(napis1, napis2):
    napis1 = ''.join(filter(str.isalnum, napis1)).lower()
    napis2 = ''.join(filter(str.isalnum, napis2)).lower()
    return sorted(napis1) == sorted(napis2)


def napisz_sprawdz_anagram():
    print("""def sprawdz_anagram(napis1, napis2):
    napis1 = ''.join(filter(str.isalnum, napis1)).lower()
    napis2 = ''.join(filter(str.isalnum, napis2)).lower()
    return sorted(napis1) == sorted(napis2)""")
    errors()


def sprawdz_palindrom(napis):
    napis = ''.join(e for e in napis if e.isalnum()).lower()
    return napis == napis[::-1]


def napisz_sprawdz_palindrom():
    print("""def sprawdz_palindrom(napis):
    napis = ''.join(e for e in napis if e.isalnum()).lower()
    return napis == napis[::-1]""")
    errors()


def najczestszy_znak(napis):
    liczniki = {}
    for znak in napis:
        if znak in liczniki:
            liczniki[znak] += 1
        else:
            liczniki[znak] = 1
    najczestszy = None
    max_wystapienia = 0
    for znak, wystapienia in liczniki.items():
        if wystapienia > max_wystapienia:
            max_wystapienia = wystapienia
            najczestszy = znak
    return najczestszy


def napisz_najczestszy_znak():
    print("""def najczestszy_znak(napis):
    liczniki = {}
    for znak in napis:
        if znak in liczniki:
            liczniki[znak] += 1
        else:
            liczniki[znak] = 1
    najczestszy = None
    max_wystapienia = 0
    for znak, wystapienia in liczniki.items():
        if wystapienia > max_wystapienia:
            max_wystapienia = wystapienia
            najczestszy = znak
    return najczestszy""")
    errors()


def szyfruj_cezar(napis, przesuniecie):
    zaszyfrowany_napis = ""
    for znak in napis:
        if znak.isalpha():
            if znak.islower():
                kod_znaku = ord(znak) - ord('a')
                zaszyfrowany_kod = (kod_znaku + przesuniecie) % 26
                zaszyfrowany_znak = chr(zaszyfrowany_kod + ord('a'))
            else:
                kod_znaku = ord(znak) - ord('A')
                zaszyfrowany_kod = (kod_znaku + przesuniecie) % 26
                zaszyfrowany_znak = chr(zaszyfrowany_kod + ord('A'))
            zaszyfrowany_napis += zaszyfrowany_znak
        else:
            zaszyfrowany_napis += znak
    return zaszyfrowany_napis


def napisz_szyfruj_cezar():
    print("""def szyfruj_cezar(napis, przesuniecie):
    zaszyfrowany_napis = ""
    for znak in napis:
        if znak.isalpha():
            if znak.islower():
                kod_znaku = ord(znak) - ord('a')
                zaszyfrowany_kod = (kod_znaku + przesuniecie) % 26
                zaszyfrowany_znak = chr(zaszyfrowany_kod + ord('a'))
            else:
                kod_znaku = ord(znak) - ord('A')
                zaszyfrowany_kod = (kod_znaku + przesuniecie) % 26
                zaszyfrowany_znak = chr(zaszyfrowany_kod + ord('A'))
            zaszyfrowany_napis += zaszyfrowany_znak
        else:
            zaszyfrowany_napis += znak
    return zaszyfrowany_napis""")
    errors()


def odszyfruj_cezar(napis, przesuniecie):
    odszyfrowany_napis = ""
    for znak in napis:
        if znak.isalpha():
            if znak.islower():
                kod_znaku = ord(znak) - ord('a')
                odszyfrowany_kod = (kod_znaku - przesuniecie) % 26
                odszyfrowany_znak = chr(odszyfrowany_kod + ord('a'))
            else:
                kod_znaku = ord(znak) - ord('A')
                odszyfrowany_kod = (kod_znaku - przesuniecie) % 26
                odszyfrowany_znak = chr(odszyfrowany_kod + ord('A'))
            odszyfrowany_napis += odszyfrowany_znak
        else:
            odszyfrowany_napis += znak
    return odszyfrowany_napis


def napisz_odszyfruj_cezar():
    print("""def odszyfruj_cezar(napis, przesuniecie):
    odszyfrowany_napis = ""
    for znak in napis:
        if znak.isalpha():
            if znak.islower():
                kod_znaku = ord(znak) - ord('a')
                odszyfrowany_kod = (kod_znaku - przesuniecie) % 26
                odszyfrowany_znak = chr(odszyfrowany_kod + ord('a'))
            else:
                kod_znaku = ord(znak) - ord('A')
                odszyfrowany_kod = (kod_znaku - przesuniecie) % 26
                odszyfrowany_znak = chr(odszyfrowany_kod + ord('A'))
            odszyfrowany_napis += odszyfrowany_znak
        else:
            odszyfrowany_napis += znak
    return odszyfrowany_napis""")
    errors()


def czy_zaszyfrowane(napis1, napis2):
    for przesuniecie in range(1, 26):
        odszyfrowany_napis2 = odszyfruj_cezar(napis2, przesuniecie)
        if napis1 == odszyfrowany_napis2:
            return True
    return False


def napisz_czy_zaszyfrowane():
    print("""def czy_zaszyfrowane(napis1, napis2):
    for przesuniecie in range(1, 26):
        odszyfrowany_napis2 = odszyfruj_cezar(napis2, przesuniecie)
        if napis1 == odszyfrowany_napis2:
            return True
    return False""")
    errors()


def najdluzszy_podciag(ciag):
    dlugosc = 1
    max_dlugosc = 1
    indeks_poczatkowy = 0

    for i in range(1, len(ciag)):
        if ciag[i] > ciag[i-1]:
            dlugosc += 1
        else:
            if dlugosc > max_dlugosc:
                max_dlugosc = dlugosc
                indeks_poczatkowy = i - dlugosc
            dlugosc = 1

    if dlugosc > max_dlugosc:
        max_dlugosc = dlugosc
        indeks_poczatkowy = len(ciag) - dlugosc

    najdluzszy_podciag = ciag[indeks_poczatkowy:indeks_poczatkowy+max_dlugosc]
    return najdluzszy_podciag


def napisz_najdluzszy_podciag():
    print("""def najdluzszy_podciag(ciag):
    dlugosc = 1
    max_dlugosc = 1
    indeks_poczatkowy = 0

    for i in range(1, len(ciag)):
        if ciag[i] > ciag[i-1]:
            dlugosc += 1
        else:
            if dlugosc > max_dlugosc:
                max_dlugosc = dlugosc
                indeks_poczatkowy = i - dlugosc
            dlugosc = 1

    if dlugosc > max_dlugosc:
        max_dlugosc = dlugosc
        indeks_poczatkowy = len(ciag) - dlugosc

    najdluzszy_podciag = ciag[indeks_poczatkowy:indeks_poczatkowy+max_dlugosc]
    return najdluzszy_podciag""")
    errors()


def najkrotszy_podciag(ciag):
    dlugosc = 1
    min_dlugosc = 1
    indeks_poczatkowy = 0

    for i in range(1, len(ciag)):
        if ciag[i] < ciag[i-1]:
            dlugosc += 1
        else:
            if dlugosc < min_dlugosc:
                min_dlugosc = dlugosc
                indeks_poczatkowy = i - dlugosc
            dlugosc = 1

    if dlugosc < min_dlugosc:
        min_dlugosc = dlugosc
        indeks_poczatkowy = len(ciag) - dlugosc

    najkrotszy_podciag = ciag[indeks_poczatkowy:indeks_poczatkowy+min_dlugosc]
    return najkrotszy_podciag


def napisz_najkrotszy_podciag():
    print("""def najkrotszy_podciag(ciag):
    dlugosc = 1
    min_dlugosc = 1
    indeks_poczatkowy = 0

    for i in range(1, len(ciag)):
        if ciag[i] < ciag[i-1]:
            dlugosc += 1
        else:
            if dlugosc < min_dlugosc:
                min_dlugosc = dlugosc
                indeks_poczatkowy = i - dlugosc
            dlugosc = 1

    if dlugosc < min_dlugosc:
        min_dlugosc = dlugosc
        indeks_poczatkowy = len(ciag) - dlugosc

    najkrotszy_podciag = ciag[indeks_poczatkowy:indeks_poczatkowy+min_dlugosc]
    return najkrotszy_podciag""")
    errors()


def wyszukiwanie_binarne(lista, element):
    poczatek = 0
    koniec = len(lista) - 1

    while poczatek <= koniec:
        srodek = (poczatek + koniec) // 2

        if lista[srodek] == element:
            return srodek
        elif lista[srodek] < element:
            poczatek = srodek + 1
        else:
            koniec = srodek - 1

    return -1


def napisz_wyszukiwanie_binarne():
    print("""def wyszukiwanie_binarne(lista, element):
    poczatek = 0
    koniec = len(lista) - 1

    while poczatek <= koniec:
        srodek = (poczatek + koniec) // 2

        if lista[srodek] == element:
            return srodek
        elif lista[srodek] < element:
            poczatek = srodek + 1
        else:
            koniec = srodek - 1

    return -1""")
    errors()
