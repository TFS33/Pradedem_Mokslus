# Parašyti for ciklą, kuris išvestų kiekvieną skaičių pradedant nuo 0 ir baigiant 10 (pvz: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10).
for i in range(10):
    print(i)
print()
# Parašyti for ciklą, kuris išvestų kas antrą skaičių pradedant 0 ir baigiant 15 (pvz: 0, 2, 4, 6, 8, 10, 12, 14).
for i in range(0 , 16 , 2):
    print(i)
print()
# Parašyti for ciklą, kuris išvestų kas trečią skaičių, pradedant 1 ir baigiant 20. 
# Kiekvieną skaičių apskliausti laužtiniais skliaustais. Pvz.: [1][4][7]...
for i in range(1 , 19 , 3):
    print('[',i,']')
print()
# for ciklo pagalba penkis kartus išveskite savo vardą.
for i in range(5):
    print('No Name')
print()    
# Parašyti for ciklą, kuris eitų pro kiekvieną skaičių nuo 1 iki 20. 
# Jame apsirašyti if sąlygą, kuri patikrintų ar dabartinis skaičius dalinasi iš 4. Jei taip tai šį skaičių išvesti.
for i in range(20):
    if i // 4 > 0:
        print(i)
print()
# Išveskite visus skaičius nuo 1 iki 15, prie kiekvieno jų nurodant tai lyginis ar nelyginis skaičius. Pvz:
# 1 - nelyginis
# 2 - lyginis
# 3 - nelyginis
for i in range(1, 20):
    if i % 2 ==0:
        print(i , '-lyginis')
    if i % 2 ==1:
        print(i , '-nelyginis')
print()
# Apibrėžkite kintamuosius rėžių pradžiai ir pabaigai. Patikrinkite, kad tai būtų validu (pradžia turi būti mažesnė nei pabaiga).
#  Jei rėžiai tinkami, tuomet vykdyti for ciklą, kuris atskirose eilutėse išvestų kiekvieną skaičių. 
# Po kiekvieno skaičiaus padėti tarpą ir išvesti to skaičiaus kvadratą.
pradzia = int(input('Pirmas skaicius = '))
pabaiga = int(input('Antras skaicius = '))
if pradzia > pabaiga:
    print('pirmas skaicius turi buti mazesnis uz antra')
else:
    for x in range(pradzia , pabaiga +1 ):
        print(x , x ** 2)
print()
# Apibrėžkite kintamuosius rėžių pradžiai ir pabaigai. Patikrinkite, kad tai būtų validu (pradžia turi būti mažesnė nei pabaiga).
#  Jei rėžiai tinkami, tuomet vykdyti for ciklą, kuris išvestų visus nelyginius skaičius arba tuos, kurie dalinasi iš 8.
pradzia = int(input('Pirmas skaicius = '))
pabaiga = int(input('Antras skaicius = '))
if pradzia >= pabaiga:
    print('pirmas skaicius turi buti mazesnis uz antra')
else:
    for x in range(pradzia , pabaiga):
        if x % 2 != 0 or x % 8 == 0:
            print(x)
          