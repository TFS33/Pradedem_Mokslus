# Sukurkite žodyną studento duomenims saugoti. 
# Į šį žodyną sudėkite tokias savybes su reikšmėmis: vardas, pavardė, amžius, studijų programa, atsiskaitytų kreditų skaičius, 
# pažymiai, ūgis, kelintame kurse mokosi, kurioje mokykloje mokosi. Šiuos duomenis galite grupuoti į vidinius žodynus arba visus išrašyti atskirai. 
# Išveskite šią informaciją per vieną print().
# Taip pat, pamėginkite išvesti atskirose eilutėse tris skirtingas pasirinktas savybes.

studentas = { 'vardas': "Haris" ,
 'pavarde' : "Simanivic" ,
  'amzius' : "20" ,
   'programa' : "Agronomija" ,
   'kreditai' : 15,
   'pažymiai' : [ 10 , 4 , 7 , 5 , 10 , 8] ,
   'ugis' : 185 ,
   'kursas' : 2 ,
   'mokykla' : "Gatvinis" }
print(studentas)

print(studentas.get('vardas'))
print(studentas.get('pažymiai'))
print(studentas.get('?'))
print(studentas['programa'])
print()
raktai = studentas.keys()
vertes = studentas.values()
x = studentas.items()
print(raktai)
print(vertes)
print(x)
studentas.update({'Pravarde' : "Pops"}) # adds
print(studentas)
studentas.pop('Pravarde') # pasalina konkreciai
print(studentas)
studentas.popitem() # pasalina paskutini
print(studentas)
