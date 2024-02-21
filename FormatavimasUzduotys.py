#pirma uzduotis
vardas = 'Vardenis'
pavarde = 'Pavardenis'
amzius = 22
kursas = 3
vidurkis = 8.7
#norimas tekstas Vardenis Pavardenis (22 m.) mokosi 3-iame kurse, jo vidurkis yra 8.7
# šioje vietoje suformuokite eilutę: eilute = ...
eilute = (f"{vardas} {pavarde} ({amzius} m.) mokosi 3-iame kurse, jo vidurkis yra {vidurkis} ")
print(eilute)
print()
print()
#antra uzduotis
# duotas pradinis kodas
#vienas = 1
#du = 2

# šioje vietoje suformuokite eilutę: eilute = ...

#print(eilute)
#reikia gauti
# Mano batai buvo 2
# 1 dingo - nerandu.
# Aš su 1 batuku,
# Niekur eiti negaliu.
#
#
vienas = 1
du = 2

eilute = f"""
    mano batai buvo {du}
    {vienas} dingo - nerandu
    as su {vienas} batuku
    niekur eiti negaliu
    """
print(eilute)
# trecia uzduotis
print()
print()
#Išveskite 3x3 dydžio tuščiavidurį kvadratą iš * simbolio
sim = "*"
sai = " "
eilute = f"""
    {sim} {sim} {sim}
    {sim} {sai} {sim}
    {sim} {sim} {sim}
"""
print(eilute)
print()

# ketvirta uzduotis
# susikurkite šiuos kintamuosius, saugančius informaciją apie gyvūną: pavadinimas, amžius, kailio spalva, svoris.
# Išveskite šiuos duomenis gražiai suformatuotus vienoje eilutėje, sakinio forma. Pavyzdžiui:
# Gyvūnas - šuo (2 m.) turi rudą kailio spalvą ir sveria 1.4 kg.
pavadinimas = 'suo'
amzius = 2
kailio_spalva = 'ruda'
svoris = 1.4
eilute = f"Gyvunas - {pavadinimas} ({amzius} m.) turi {kailio_spalva} kailio spalva ir sveria {svoris} kg."
print(eilute)
# penkta uzduotis
# Susikurkite skaičiaus kintamąjį, kurį išveskite penkis kartus toje pačioje eilutėje be tarpų tarp šių skaičių
# Pavyzdžiui: skaičius - 25
# išvedimas - 2525252525
kintamasis = 69
eilute = f"{kintamasis}{kintamasis}{kintamasis}{kintamasis}{kintamasis}"
print(eilute)
#tas pats rezultatas
kintamasis = '69'
eilute = kintamasis*5
print()
print(eilute)
print()
print()
# sesta uzduotis
# Susikurkite skaičiaus kintamąjį, kurį išveskite penkis kartus toje pačioje eilutėje su tarpais tarp šių skaičių.
# Pavyzdžiui: skaičius - 25
# rezultatas - 25 25 25 25 25
kintamasis = 69
eilute = f"{kintamasis} {kintamasis} {kintamasis} {kintamasis} {kintamasis}"
print(eilute)
