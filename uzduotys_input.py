# uzduotys input
# Paprašykite naudotojo įvesti savo vardą, amžių ir kodėl panoro išmokti Pitoną. 
# Įvestą informaciją išveskite tvarkingai, vienu sakiniu ar atskirose eilutėse su prierašais.
vardas = input('iveskite varda ')
amzius = input('iveskite amziu ')
noras = input("kodel norite ismokti PYTHON? ")
print(f' VARDAS: {vardas} AMZIUS: {amzius} PRIEZASTIS: {noras} ')
print()
# Paprašykite vartotojo įvesti norimą simbolį. Iš šio simbolio atspausdinkite laiptus. Pvz.:
# * 
# **
# ***
simbolis = input('iveskite norima simboli: ')
print(f"""
{simbolis}
{simbolis}{simbolis}
{simbolis}{simbolis}{simbolis}
    """)
print()
# Paprašykite vartotojo įvesti norimą simbolį. Iš šio simbolio atspausdinkite inicialus. Pvz.:
# *** *
#  *  *
#  *  ***
# Užduočiai atlikti galite naudoti daugelio eilučių išvedimą.
simbolis = input('iveskite norima simboli: ')
tarpas = " "
print(f"""
    {simbolis}{simbolis}{simbolis}{tarpas}{simbolis}
    {tarpas}{simbolis}{tarpas}{tarpas}{simbolis}
    {tarpas}{simbolis}{tarpas}{tarpas}{simbolis}{simbolis}{simbolis}
    """)
print()
# Paprašykite vartotojo įvesti vardą, amžių, ūgį (metais) (nepamirškite ką reikia iškonvertuoti iš str į int ar float).
#  Išveskite gautus duomenis ir jų tipus.
vardas = input("iveskite varda: ")
amzius = int(input("iveskite amziu: "))
ugis = float(input("ugis metrais: "))
svoris = int(input("svoris kg: "))
print(f"Vardas:" , vardas , type(vardas))
print(f"Amzius : " , amzius , "m." , type(amzius))
print(f'Ugis ' , ugis , 'm.' , type(ugis))
print(f'Svoris' , svoris , 'kg.' , type(svoris))
# Leiskite naudotojui įvesti metrus. Išveskite kiek tai gaunasi centimetrais, milimetrais ir kilometrais.
metrai = int(input('iveskite metrus :'))
print(f'ivesti metrai :' , metrai ,  'm.')
print(f'centimetrai :' , (metrai * 100) , 'cm.')
print(f'milimetrai :' , (metrai * 1000) , 'mm.')
print(f'kilometrai :' , (metrai / 1000) , 'km.')
print()
# Paprašykite vartotojo įvesti 5-is savo pažymius vienoje eilutėje
# Paskaičiuokite pažymių vidurkį. Išveskite atsakymą.
print('iveskite savo 5 pazymius vidurkiui atskiriant tarpu')
paz1, paz2, paz3, paz4, paz5 = input().split() 
paz1 = int(paz1)
paz2 = int(paz2)
paz3 = int(paz3)
paz4 = int(paz4)
paz5 = int(paz5)
print(f'Vidurkis :{(paz1 + paz2 + paz3 + paz4 + paz5) / 5 }')
# Vienoje eilutėje įveskite vardą, pavardę ir amžių. Išveskite informaciją vienu sakiniu.
vardas , pavarde , amzius = input("iveskite varda , pavarde , amziu atskirdami tarpu. ").split()
vardas = vardas
pavarde = pavarde
amzius = int(amzius)
print(f'vardas - ' , vardas , 'pavarde -' , pavarde , 'amzius - ' , amzius , 'm.')
print()
# Leiskite vartotojui įvesti du skaičius. Išveskite šių skaičių sudėtį, skirtumą, sandaugą ir dalmenį.
sk1 = int(input('iveskite pirma skaiciu :'))
sk2 = int(input('iveskite antra skaiciu :'))
sudetis = int(sk1 + sk2)
skirtumas = int(sk1 - sk2)
sandauga = int(sk1 * sk2)
dalmuo = int(sk1 / sk2)
print(f'sudetis :' , sudetis , "skirtumas :" , skirtumas , 'sandauga :' , sandauga , 'dalmuo :' , dalmuo)
print()
# Leiskite vartotojui įvesti du norimus skaičius. Išveskite kokia gaunasi liekana padalinus vieną skaičių iš kito.
sk1 = int(input('iveskite pirma skaiciu :'))
sk2 = int(input('iveskite antra skaiciu :'))
liekana = int(sk1 % sk2)
print(f'liekana :' , liekana )
print()
# Leiskite vartotojui įvesti du skaičius
# Išveskite kiek gautųsi vieną skaičių pakėlus kito skaičiaus laipsniu
# (pvz, pirmas skaičius eina už pagrindą, o antras skaičius yra laipsnis, kuriuo ir keliame).
sk1 = int(input('iveskite pirma skaiciu :'))
sk2 = int(input('iveskite antra skaiciu :'))
laipsnis = int(sk1 ** sk2)
print(f'laipsnis :' , laipsnis )
print()