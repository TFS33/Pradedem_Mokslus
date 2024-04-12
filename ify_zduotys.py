# Susikurkite tris kintamuosius skaičiams saugoti. Parašykite šias atskiras if sąlygas:
# Ar pirmas ir antras skaičiai yra lygūs?
# Ar antras ir trečias skaičiai yra lygūs?
# Ar pirmas skaičius yra didesnis už antrąjį?
# Ar antras skaičius yra didesnis už dvigubą trečiojo skaičiaus reikšmę?
# Ar pirmas skaičius yra lyginis?
# Ar antras skaičius yra nelyginis?
# Ar trečias skaičius yra teigiamas?
# Ar pirmas skaičius yra neigiamas?
# Ar antras skaičius dalinasi iš 4?
x = int(input('iveskite pirmaji skaiciu :'))
y = int(input('iveskite antraji skaiciu :'))
z = int(input('iveskite treciaji skaiciu :'))
if (x == y):
    print('pirmas ir antras skaicius yra lygus')
    print()
if (y == z) :
        print('trecias ir antras skaicius yra lygus')
print()
if (x > y) :
        print('pirmas skaicius didesnis uz antraji')
print()
if (x > y * 2) :
        print('pirmas ir antras skaicius yra lygus')
print()
if (x % 2 == 0) :
        print('pirmas skaicius yra lyginis')
print()
if (y % 2 == 1) :
        print('antras skaicius yra nelyginis')
print()
if (z > 0) :
        print('trecias skaicius yra teigiamas')
print()
if (z == 0) :
        print('trecias skaicius yra lygus nuliui')
print()
if (x < 0) :
        print('pirmas skaicius yra neigiamas')
print()
if (y % 4 == 0):
        print('antras skaicius dalijasi is keturiu')
# Liepkite vartotojui suvesti savo amžių.
# Patikrinkite ar amžius yra didesnis arba lygus 18-ai, jei taip - išveskite "jūs galite balsuoti".
amzius = int(input('iveskite savo amziu: '))
if (amzius >= 18) :
    print('jūs galite balsuoti')
print()
# Leiskite vartotojui suvesti norimą kiekį pažymių (pavyzdžiui, jūs nusimatote 3-is kintamuosius, tai leidžiate įvykdyti 3 įvedimus)
# Raskite šių pažymių vidurkį. Patikrinkite ar vidurkis teigiamas (daugiau arba lygu 5-iems), jei taip - išveskite "vidurkis teigiamas".
pirmas = int(input('iveskite pirmaji pazymi: '))
antras = int(input('iveskite antraji pazymi: '))
trecias = int(input('iveskite treciaji pazymi: '))
pirmas = int(pirmas)
antras = int(antras)
trecias = int(trecias)
if ( (pirmas + antras + trecias) / 3 >= 5 ):
    print('vidurkis teigiamas')
else :
    print('ups...')
# Parašykite programą, kuri leidžia įvesti išraišką, kurią sudaro du skaičiai ir operacija atskirti tarpais (pvz. 5 * 8).
# Pagal operaciją programa turi apskaičiuoti rezultatą ir jį atspausdinti.
skaicius_1, operacija, skaicius_2 = input("iveskite veiksma (pvz. 5 * 8):").split()
skaicius_1, skaicius_2 = int(skaicius_1), int(skaicius_2)
if (operacija == '*'):
    print(skaicius_1 , operacija , skaicius_2 , "=" , skaicius_1 * skaicius_2)
print()
if (operacija == '/'):
    print(skaicius_1 , operacija , skaicius_2 , "=" , skaicius_1 / skaicius_2)
print()
if (operacija == '+'):
    print(skaicius_1 , operacija , skaicius_2 , "=" , skaicius_1 + skaicius_2)
print()
if (operacija == '-'):
    print(skaicius_1 , operacija , skaicius_2 , "=" , skaicius_1 - skaicius_2)
print()
# Susikurkite skaičiaus kintamąjį arba leiskite šį skaičių įvesti vartotojui. Atlikite šiuos patikrinimus ir veiksmus:
# Jei skaičius dalinasi iš 5, tuomet išveskite šio skaičiaus daugybos lentelę nuo 1 iki 5
# Jei skaičius lyginis, tuomet išveskite šį skaičių, jo kvadratą ir jį padalintą iš 2.
# Jei skaičius nesidalina iš 7, tuomet susikurkite antrąjį kintamąjį, išveskite šių dviejų skaičių sumą, skirtumą, sandaugą, dalmenį.
mememe = input("iveskite skaiciu: ")
mememe = int(mememe)
if (mememe % 5 == 0):
    print('1 *' ,*  {mememe}, '=', 1 * mememe )
    print('2 *' ,*  {mememe}, '=', 2 * mememe )
    print('3 *' ,*  {mememe}, '=', 3 * mememe )
    print('4 *' ,*  {mememe}, '=', 4 * mememe )
    print('5 *' ,*  {mememe}, '=', 5 * mememe )
if (mememe % 2 == 0) :
    print(mememe)
    print(mememe, "kvadratu =" , mememe ** 2)
    print(mememe, "padalinus is dvieju =", int(mememe / 2))
if (mememe % 7 == 1):
    antras = input("iveskite antraji skaiciu: ")
    antras = int(antras)
    suma = int(mememe + antras)
    skirtumas = int(mememe - antras)
    sandauga = int(mememe * antras)
    dalmuo = int(mememe / antras)
    print("suma =" , suma)
    print("skirtumas =" , skirtumas)
    print("sandauga =", sandauga)
    print("dalmuo =" , dalmuo)
