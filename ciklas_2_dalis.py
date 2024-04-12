# Leiskite vartotojui įvesti savo vardą. Ciklą for vykdykite tiek kartų, kiek tame varde yra raidžių. Visais atvejais išveskite tą patį pasisveikinimą, 
# pavyzdžiui "Labas, Ieva" (ši eilutė kartotųsi 4 kartus, kadangi varde "Ieva" yra 4 raidės).

vardas = input('Iveskite varda = ')

for i in vardas:
    print("Labas " , vardas)
print()

# Suprogramuokite tokį ciklą: for elementas in [88, 65, 21, 26, 47]
# Iš duotų skaičių išveskite visus skaičius, kurie yra lyginiai.
skaiciai = [88, 65, 21, 26, 47]
for elementas in skaiciai:
    if elementas % 2 ==0:
        print(elementas) 
