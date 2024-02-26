# Kai prašymas įvesti informaciją išvedamas atskirai:
print('Įveskite vardą:')
vardas = input()
print(vardas)
print()
# Kai prašymas įvesti informaciją išvedamas kartu:
vardas = input('Įveskite vardą:')
print(vardas)
print()
#Kokio tipo informaciją gauname iš input?
print('Įveskite kokį nors skaičių:')
skaicius = input()

print('Įvesta:', skaicius, type(skaicius))
print()
# Gauname skaičių iš prieš tai įvykusios įvesties:
skaicius = int(skaicius)
print('Konvertuota:', skaicius, type(skaicius))
print()
# Skaičiaus įvestį galime įgyvendinti ir per vieną eilutę:
skaicius = int(input('Įveskite sveiką skaičių:'))
print(skaicius)
print()
# Kai norime gauti įvestą slankaus kablelio skaičių:
skaicius = float(input('Įveskite skaičių:'))
print(skaicius)
# F-eilučių prisiminimui įvesime du skaičius atskirose eilutėse ir juos sudėsime:
skaicius_1 = input('Įveskite pirmą skaičių')
skaicius_2 = input('Įveskite antrą skaičių')
print(f'{skaicius_1} + {skaicius_2} = {skaicius_1 + skaicius_2}')
print()
# Atkreipkite dėmesį į tai kad praeitame pavyzdyje gauta įvestis yra str tipo, todėl sudėtis (+) atliko teksto sudėtį, o ne matematinę sudėtį.
# Tai ištaisyti būtų galima taip:
skaicius_1 = int(input('Įveskite pirmą skaičių'))
skaicius_2 = int(input('Įveskite antrą skaičių'))
print(f'{skaicius_1} + {skaicius_2} = {skaicius_1 + skaicius_2}')
print()
# Arba taip:
skaicius_1 = input('Įveskite pirmą skaičių')
skaicius_2 = input('Įveskite antrą skaičių')
print(f'{skaicius_1} + {skaicius_2} = {int(skaicius_1) + int(skaicius_2)}')
print()
# Šį kartą įvesime tuos du skaičius vienoje eilutėje:
print('Įveskite du skaičius, juos atskirdami tarpu:')
skaicius_1, skaicius_2 = input().split()
print(f'{skaicius_1} + {skaicius_2} = {int(skaicius_1) + int(skaicius_2)}')
print()
# 2pav.
print('Įveskite du skaičius atskirdami tarpu:')
skaicius_1, skaicius_2 = input().split()
skaicius_1 = int(skaicius_1)
skaicius_2 = int(skaicius_2)
print(f'{skaicius_1} + {skaicius_2} = {skaicius_1 + skaicius_2}')
print()
# 3 pav
print('Įveskite tris skaičius atskirdami tarpu:')
skaicius_1, skaicius_2, skaicius_3 = [ int(skaicius) for skaicius in input().split() ]
print(f'{skaicius_1} + {skaicius_2} + {skaicius_3} = {skaicius_1 + skaicius_2 + skaicius_3}')
print()
# Galima ir taip:
print('Įveskite du skaičius (atskiriant enter paspaudimu):')
pirmas = int(input())
antras = int(input())

suma = pirmas + antras
print('skaičių suma:', suma)
print ()
# Daugiau įvesties:
vardas = input('Įveskite vardą: ')
amzius = int( input('Įveskite amžių: ') )

print('Įvesta informacija:')
print(vardas, type(vardas))
print(amzius, type(amzius))
print()