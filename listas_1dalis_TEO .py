informacija = [] # tuscias listas
# Sąrašas su duomenimis:

# saraso_pavadinimas = [reikšmė, reikšmė, reikšmė, ...]
skaiciai = [7, 4, 5, 8, 3, 1]
zmones = ['Jonas', 'Petras', 'Ona', 'Birutė']
# Viso sąrašo atvaizdavimas
# Jeigu norime atvaizduoti viso sąrašo informaciją, tai galime padaryti taip:
skaiciai = [7, 5, 6, 9, 7, 5]
print(skaiciai)
zmones = ['Ona', 'Petras', 'Birutė', 'Jonas']
print(zmones)
# Sąrašo papildymas
# Jeigu norima papildyti jau egzistuojantį sąrašą, tam galima naudoti append() arba extend() metodus.

# Pavyzdžiui:
skaiciai = [1, 2, 3, 4]

skaiciai.append(5)
skaiciai.append(6)
print(skaiciai)

skaiciai.extend([7, 8, 9])
print(skaiciai)
# Sąrašo elementų kiekis
# Norėdami išsiaiškinti kiek sąraše yra elementų, mes galima naudoti len() funkciją:

# len(saraso_pavadinimas)
# Pavyzdžiui:
skaiciai = [5, 2, 3, 5, 4]
print( len(skaiciai) )
# Indeksavimas
# Jeigu sąraše yra duomenų, tai kiekvienas elementas tame sąraše turi savo indeksą. Šio indekso pagalba galima tą informaciją pasiekti arba pakeisti.

# Indeksai yra skaičiuojami pradedant nuo 0.
pazymiai = [7, 8, 5, 9, 10, 6]
print(pazymiai[3])
# pavyzdziai
# Pasižiūrėkime, kaip pateikiami įvairių tipų sąrašai.
list = [1, 2, 3, 4, 5, 6]
list_2 = ['a', 'b', 'c']
list_3 = [1, 2, 'a', True]

print(list)
print(list_2)
print(list_3)

# Pasižiūrėkite į programą ir mintyse įvardinkite išvedamas reikšmės. Paleiskite programą ir pasitikrinkite.

skaiciai = [78, 65, 95, 21, 23, 14, 74, 147]

print(skaiciai[0])
print(skaiciai[2])
print(skaiciai[4])
print(skaiciai[5])

# Čia parodytos įvairios manipuliacijos indeksais.

skaiciai = [47, 54, 25, 36, 87]

print('Sąrašas:', skaiciai)
print('Pirmas sąrašo skaičius:', skaiciai[0])
print('Narių kiekis sąraše:', len(skaiciai))
print('Paskutinis sąrašo skaičius:', skaiciai[-1])
print('Paskutinis sąrašo skaičius:', skaiciai[len(skaiciai) - 1])

# Pažiūrėkite, kaip galime papildyti sąrašus.

skaiciai = []

print(skaiciai)

# sąrašo papildymas nurodyta reikšme, pridedama į galą
skaiciai.append(87)
skaiciai.append(95)

print(skaiciai)

# sąrašo papildymas keliomis nurodytomis reikšmėmis, pridedama į galą
skaiciai.extend([147, 258, 399])

print(skaiciai)

# Paprastas sąrašo elementų vidurkio skaičiavimas. Pagalvokite, kaip tai galima padaryti ciklo pagalba.

pazymiai = [8, 7, 9, 9, 8]

print('Studento pažymiai:', pazymiai)

suma = pazymiai[0] + pazymiai[1] + pazymiai[2] + pazymiai[3] + pazymiai[4]
vidurkis = suma / len(pazymiai)

print('Gauta suma:', suma)
print('Pažymių vidurkis:', vidurkis)

# vardai = ['Agnė', 'Tomas', 'Gintarė', 'Petras']

vardai = ['Agnė', 'Tomas', 'Gintarė', 'Petras']
print(vardai)

vardai[0] = 'Paulina'
vardai[3] = 'Justas'

print(vardai)

# ['Agnė', 'Tomas', 'Gintarė', 'Petras']
# ['Paulina', 'Tomas', 'Gintarė', 'Justas']

# Kai naudojam range(), tai gauname range objektą. Norėdami gauti skaičių eilutę, turime range objektą paversti į sąrašą.

print(range(1, 100))
print(list(range(1, 100)))


# Čia parodytas sąrašo formavimas iš atsitiktinių skaičių.

from random import randint

skaiciai = []
print(skaiciai)

naujas_sk = randint(1, 10)
naujas_sk2 = randint(1, 15)

skaiciai.append(naujas_sk)
skaiciai.append(naujas_sk2)

print(skaiciai)


#  Sąrašo išplėtimas keliom atsitiktinėm reikšmėm.

# Ši eilutė bus veiksni jeigu būsite įvykdę ankstesnį langelį.
# from random import randint

skaiciai = []
print(skaiciai)

skaiciai.extend([ randint(1, 10), randint(1, 10), randint(1, 10) ])
print(skaiciai)
