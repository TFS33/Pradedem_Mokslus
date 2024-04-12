# Parašyti for ciklą, kuris išvestų kiekvieną skaičių pradedant nuo 0 ir baigiant 10 (pvz: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10).

for i in range(0, 11):
    print(i)

# Parašyti for ciklą, kuris išvestų kas antrą skaičių pradedant 0 ir baigiant 15 (pvz: 0, 2, 4, 6, 8, 10, 12, 14).

for i in range(0, 15, 2):
    print(i)

# Parašyti for ciklą, kuris išvestų kas trečią skaičių, pradedant 1 ir baigiant 20.
#  Kiekvieną skaičių apskliausti laužtiniais skliaustais. Pvz.: [1][4][7]...

for i in range(0, 20, 3):
    print(f'[{i}]')

# for ciklo pagalba penkis kartus išveskite savo vardą.

for i in range(4):
    print('Tomas')

# Parašyti for ciklą, kuris eitų pro kiekvieną skaičių nuo 1 iki 20.
# Jame apsirašyti if sąlygą, kuri patikrintų ar dabartinis skaičius dalinasi iš 4. Jei taip tai šį skaičių išvesti.

for i in range(1,21):
    if i % 2 == 0:
        print(i)

# Išveskite visus skaičius nuo 1 iki 15, prie kiekvieno jų nurodant tai lyginis ar nelyginis skaičius. Pvz:

for i in range(1, 16):
    if i % 2 == 0:
        print(f' skaicius {i} yra lyginis')
    if i % 2 !=0:
        print(f' skaicius {i} yra nelyginis')

# Apibrėžkite kintamuosius rėžių pradžiai ir pabaigai. Patikrinkite, kad tai būtų validu (pradžia turi būti mažesnė nei pabaiga).
#  Jei rėžiai tinkami, tuomet vykdyti for ciklą, kuris atskirose eilutėse išvestų kiekvieną skaičių. 
# Po kiekvieno skaičiaus padėti tarpą ir išvesti to skaičiaus kvadratą.

a = 100
b = 20

if a < b :
    for i in range(a , b +1):
        print(i , i ** 2 )
else:
    print('Pirmas skaicius turi buti mazesnis uz antra')

# Apibrėžkite kintamuosius rėžių pradžiai ir pabaigai. Patikrinkite, kad tai būtų validu (pradžia turi būti mažesnė nei pabaiga).
#  Jei rėžiai tinkami, tuomet vykdyti for ciklą, kuris išvestų visus nelyginius skaičius arba tuos, kurie dalinasi iš 8.

x = 10
y = 50

if x < b:
    for i in range(x, y):
        if i % 8 ==0 or i % 2 != 0:
            print(i)
else:
    print('Netinkami skaiciai')

