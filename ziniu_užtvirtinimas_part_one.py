# Žinių užtvirtinimas (1)
# Suskaičiuoti kiek duonos kepalų kepykla sugebės iškepti per dieną, ar spės įgyvendinti visus dienos užsakymus ir suskaičiuoti kiek iš jų uždirbs pelno.
# Duomenys
# Apibrėžti duomenys:

# Darbo valandų per dieną - 8 val.
# Jūsų įvedami duomenys:

# Kiek darbuotojas gali iškepti kepalų per valandą.
# Kiek darbuotojų turi kepykla.
# Vieno kepalo savikaina.
# Vieno kepalo pardavimo kaina.
# Kiek kepykla turi tą dieną iškepti kepalų (užsakymai).
# Susikurkite kintamuosius ir priskirkite informaciją jiems...
import random
darbo_valandos = 8
kepalai_per_valanda = 3
darbuotojų_skaicius = 10
kepalo_savikaina = 0.82
kepalo_pardavimo_kaina = 1.56
uzsakymai = random.randint(0 , 333)
print('uzsakymu skaicius = ' , uzsakymai)

# Skaičiavimai

# Suskaičiuoti kiek kepykla per vieną darbo dieną spės iškepti duonos kepalų.
darbuotojo_kepalai = int(darbo_valandos) * int(kepalai_per_valanda)
print(darbuotojo_kepalai)
kepalai_per_darbo_diena = int(darbuotojo_kepalai) * int(darbuotojų_skaicius)
print(kepalai_per_darbo_diena)


# Apskaičiuoti visų kepalų savikainą, gautas pajamas pardavus ir iš to gauto pelno dalį.
visu_savikaina = float(kepalai_per_darbo_diena) * float(kepalo_savikaina)
viso_pajamu = float(kepalai_per_darbo_diena) * float(kepalo_pardavimo_kaina)
print(visu_savikaina)
print(viso_pajamu)
pelnas = float(viso_pajamu) - float(visu_savikaina)
print('Pelnas lygus = ', pelnas)

# Patikrinti ar kepykla spės iškepti visus tos dienos užsakymus. Jei ne, suskaičiuoti kiek kepalų nespės iškepti.

if int(kepalai_per_darbo_diena) > int(uzsakymai):
    print('Kepykla spes atlikti uzsakymus')
else:
     trukumas = int(uzsakymai) - int(kepalai_per_darbo_diena) 
     print(f"Truksta " , trukumas , 'kepalu.')  


# Papildomai įvertinkite tai, kad pajamas ir pelną galite gauti tik iš parduotų kepalų.


parduota_kepalu = random.randint(0 , 240)
kepalo_pelnas =  float(kepalo_pardavimo_kaina) - float(kepalo_savikaina)
print(kepalo_pelnas)
dienos_pelnas =  float(parduota_kepalu) * float(kepalo_pelnas)
print('Dienos pelnas yra = ' , dienos_pelnas)