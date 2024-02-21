marke = 'Citroen'
modelis = 'Xsara'
metai = 2002 
rida = 148974
print(marke, modelis, 'buvo pagaminta', metai, 'metais ir nuvažiavo', rida, 'km.')
print()
print()
marke = 'Citroen'
modelis = 'Xsara'
metai = 2002
rida = 148974

# Šis kodas neveiks (rodys klaidą), nes Pitonas nemokės sujungti eilutės ir skaičiaus.
# Galite šią eilutę nukomentuoti ir pažiūrėti.  
# sakinys = marke + " " + modelis + " buvo pagaminta " + metai + " metais ir nuvažiavo " + rida + " km."

# O šis kodas geras, nes jis konvertuoja skaičius į eilutės tipą
sakinys = marke + " " + modelis + " buvo pagaminta " + str(metai) + " metais ir nuvažiavo " + str(rida) + " km."

print(sakinys)
print()
print()
# format metodas
marke = 'Citroen'
modelis = 'Xsara'
metai = 2002
rida = 148974

print("{1} {0} buvo pagaminta {2} metais ir nuvažiavo {3} km.".format(modelis, marke, metai, rida))
# f - eilute naujesnis(3.6v)
print()
print()
marke = 'Citroen'
modelis = 'Xsara'
metai = 2002
rida = 148974

print(f'{marke} {modelis} buvo pagaminta {metai} metais ir nuvažiavo {rida} km.')