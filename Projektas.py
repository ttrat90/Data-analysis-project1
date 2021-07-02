import glob
from Projektas_reader import Reader
import matplotlib.pyplot as pl


def skaiciuoti_vidurki(sarasas):
        suma = 0
        for elementas in sarasas:
            suma = suma + float(elementas)
        return suma / len(sarasas)


failu_sarasas_1 = glob.glob("* asmenys.csv")
failu_sarasas_2 = glob.glob("* namu ukiai.csv")
metu_sarasas = []
zmones_aukst_m = []
zmones_aukst_k = []
alytus_gyv = []
kaunas_gyv = []
klaipeda_gyv = []
marijampole_gyv = []
panevezys_gyv = []
siauliai_gyv = []
taurage_gyv = []
telsiai_gyv = []
utena_gyv = []
vilnius_gyv = []
algos_alytus = []
algos_kaunas = []
algos_klaipeda = []
algos_marijampole = []
algos_panevezys = []
algos_siauliai = []
algos_taurage = []
algos_telsiai = []
algos_utena = []
algos_vilnius = []
alytus_alg_vid = []
kaunas_alg_vid = []
klaipeda_alg_vid = []
marijampole_alg_vid = []
panevezys_alg_vid = []
siauliai_alg_vid = []
taurage_alg_vid = []
telsiai_alg_vid = []
utena_alg_vid = []
vilnius_alg_vid = []
zmones_santechnika = []
zmones_lauko_tualetas = []
zmones_kompiuteris = []


for failas in failu_sarasas_1:
    abu_failai = Reader(failas, failu_sarasas_2[failu_sarasas_1.index(failas)])
    metai = failas[0:4]
    metu_sarasas.append(metai)
    zmones_aukst_k.append(abu_failai.auks_is_zmones_kaime)
    zmones_aukst_m.append(abu_failai.auks_is_zmones_mieste)
    alytus_gyv.append(abu_failai.alytaus_g)
    kaunas_gyv.append(abu_failai.kauno_g)
    klaipeda_gyv.append(abu_failai.klaipedos_g)
    marijampole_gyv.append(abu_failai.marijampoles_g)
    panevezys_gyv.append(abu_failai.panevezio_g)
    siauliai_gyv.append(abu_failai.siauliu_g)
    taurage_gyv.append(abu_failai.taurages_g)
    telsiai_gyv.append(abu_failai.telsiu_g)
    utena_gyv.append(abu_failai.utenos_g)
    vilnius_gyv.append(abu_failai.vilniaus_g)
    algos_alytus.append(abu_failai.algos_alytus) 
    algos_kaunas.append(abu_failai.algos_kaunas) 
    algos_klaipeda.append(abu_failai.algos_klaipeda) 
    algos_marijampole.append(abu_failai.algos_marijampole) 
    algos_panevezys.append(abu_failai.algos_panevezys)
    algos_siauliai.append(abu_failai.algos_siauliai) 
    algos_taurage.append(abu_failai.algos_taurage)
    algos_telsiai.append(abu_failai.algos_telsiai)
    algos_utena.append(abu_failai.algos_utena)
    algos_vilnius.append(abu_failai.algos_vilnius)
    zmones_santechnika.append(abu_failai.zmoniu_kiekis_su_kanalizacija)
    zmones_lauko_tualetas.append(abu_failai.zmoniu_kiekis_su_lauko_tualetu)
    zmones_kompiuteris.append(abu_failai.zmoniu_kiekis_su_kompiuteriu)


for alga in algos_alytus:
    alytus_alg_vid.append(skaiciuoti_vidurki(alga))
for alga in algos_kaunas:
    kaunas_alg_vid.append(skaiciuoti_vidurki(alga))
for alga in algos_klaipeda:
    klaipeda_alg_vid.append(skaiciuoti_vidurki(alga))
for alga in algos_marijampole:
    marijampole_alg_vid.append(skaiciuoti_vidurki(alga))
for alga in algos_panevezys:
    panevezys_alg_vid.append(skaiciuoti_vidurki(alga))
for alga in algos_siauliai:
    siauliai_alg_vid.append(skaiciuoti_vidurki(alga))
for alga in algos_taurage:
    taurage_alg_vid.append(skaiciuoti_vidurki(alga))
for alga in algos_telsiai:
    telsiai_alg_vid.append(skaiciuoti_vidurki(alga))
for alga in algos_utena:
    utena_alg_vid.append(skaiciuoti_vidurki(alga))
for alga in algos_vilnius:
    vilnius_alg_vid.append(skaiciuoti_vidurki(alga))


for metai_iki_euro in range(0, 5):
    alytus_alg_vid[metai_iki_euro] = alytus_alg_vid[metai_iki_euro] / 3.4528
    kaunas_alg_vid[metai_iki_euro] = kaunas_alg_vid[metai_iki_euro] / 3.4528
    klaipeda_alg_vid[metai_iki_euro] = klaipeda_alg_vid[metai_iki_euro] / 3.4528
    marijampole_alg_vid[metai_iki_euro] = marijampole_alg_vid[metai_iki_euro] / 3.4528
    panevezys_alg_vid[metai_iki_euro] = panevezys_alg_vid[metai_iki_euro] / 3.4528
    siauliai_alg_vid[metai_iki_euro] = siauliai_alg_vid[metai_iki_euro] / 3.4528
    taurage_alg_vid[metai_iki_euro] = taurage_alg_vid[metai_iki_euro] / 3.4528
    telsiai_alg_vid[metai_iki_euro] = telsiai_alg_vid[metai_iki_euro] / 3.4528
    utena_alg_vid[metai_iki_euro] = utena_alg_vid[metai_iki_euro] / 3.4528
    vilnius_alg_vid[metai_iki_euro] = vilnius_alg_vid[metai_iki_euro] / 3.4528


fig, ax = pl.subplots(2,2)
ax[0,0].plot(metu_sarasas, zmones_aukst_m, label = "Žmonių su aukštuoju skaičius mieste")
ax[0,0].plot(metu_sarasas, zmones_aukst_k, label = "Žmonių su aukštuoju skaičius kaime")
ax[0,1].plot(metu_sarasas, alytus_gyv, label = "Žmonių su aukštuoju kiekis Aytaus aps")
ax[0,1].plot(metu_sarasas, kaunas_gyv, label = "Žmonių su aukštuoju kiekis Kauno aps")
ax[0,1].plot(metu_sarasas, klaipeda_gyv, label = "Žmonių su aukštuoju kiekis Klaipėdos aps")
ax[0,1].plot(metu_sarasas, marijampole_gyv, label = "Žmonių su aukštuoju kiekis Marijampolės aps")
ax[0,1].plot(metu_sarasas, panevezys_gyv, label = "Žmonių su aukštuoju kiekis Panevėžio aps")
ax[0,1].plot(metu_sarasas, siauliai_gyv, label = "Žmonių su aukštuoju kiekis Šiaulių aps")
ax[0,1].plot(metu_sarasas, taurage_gyv, label = "Žmonių su aukštuoju kiekis Tauragės aps")
ax[0,1].plot(metu_sarasas, telsiai_gyv, label = "Žmonių su aukštuoju kiekis Telšių aps")
ax[0,1].plot(metu_sarasas, utena_gyv, label = "Žmonių su aukštuoju kiekis Utenos aps")
ax[0,1].plot(metu_sarasas, vilnius_gyv, label = "Žmonių su aukštuoju kiekis Vilniaus aps")
ax[1,0].plot(metu_sarasas, alytus_alg_vid, label = "Vidutinė alga žm. su aušt. iš. Alytaus aps")
ax[1,0].plot(metu_sarasas, kaunas_alg_vid, label = "Vidutinė alga žm. su aušt. iš. Kauno aps")
ax[1,0].plot(metu_sarasas, klaipeda_alg_vid, label = "Vidutinė alga žm. su aušt. iš. Klaipėdos aps")
ax[1,0].plot(metu_sarasas, marijampole_alg_vid, label = "Vidutinė alga žm. su aušt. iš. Marijampolės aps")
ax[1,0].plot(metu_sarasas, panevezys_alg_vid, label = "Vidutinė alga žm. su aušt. iš. Panevėžio aps")
ax[1,0].plot(metu_sarasas, siauliai_alg_vid, label = "Vidutinė alga žm. su aušt. iš. Šiaulių aps")
ax[1,0].plot(metu_sarasas, taurage_alg_vid, label = "Vidutinė alga žm. su aušt. iš. Tauragės aps")
ax[1,0].plot(metu_sarasas, telsiai_alg_vid, label = "Vidutinė alga žm. su aušt. iš. Telšiai aps")
ax[1,0].plot(metu_sarasas, utena_alg_vid, label = "Vidutinė alga žm. su aušt. iš. Utenos aps")
ax[1,0].plot(metu_sarasas, vilnius_alg_vid, label = "Vidutinė alga žm. su aušt. iš. Vilniaus aps")
ax[1,1].plot(metu_sarasas, zmones_santechnika, label = "Žmonės su aušt. iš. su santechnika")
ax[1,1].plot(metu_sarasas, zmones_lauko_tualetas, label = "Žmonės su aušt. iš. su lauko tualetu")
ax[1,1].plot(metu_sarasas, zmones_kompiuteris, label = "Žmonės su aušt. iš. su kompiuteriu")
ax[0,0].legend(fontsize = 5)
ax[0,1].legend(fontsize = 4)
ax[1,0].legend(fontsize = 5)
ax[1,1].legend(fontsize = 5)
fig.tight_layout()
pl.show()

