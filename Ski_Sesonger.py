import csv
import matplotlib.pyplot as plt
from datetime import date


def les_csv(filnavn):
    with open(filnavn, encoding="utf-8") as fil:
        leser = csv.reader(fil, delimiter=";")
        return list(leser)


oslo = les_csv("Oppgaver/Innlevering10/flere_vaerstasjoner_med_makstemperatur/oslo_blindern_1954_2025_med_makstemperatur.csv")
roeros = les_csv("Oppgaver/Innlevering10/flere_vaerstasjoner_med_makstemperatur/roeros_1954_2025_med_makstemperatur.csv")
tromsoe = les_csv("Oppgaver/Innlevering10/flere_vaerstasjoner_med_makstemperatur/tromsoe_1954_2025_med_makstemperatur.csv")
vaernes = les_csv("Oppgaver/Innlevering10/flere_vaerstasjoner_med_makstemperatur/vaernes_1954_2025_med_makstemperatur.csv")
venabu = les_csv("Oppgaver/Innlevering10/flere_vaerstasjoner_med_makstemperatur/venabu_1954_2025_med_makstemperatur.csv")
sinnes = les_csv("Oppgaver/Innlevering10/flere_vaerstasjoner_med_makstemperatur/sinnes_2014_2025 .csv")


def finn_skisesonger(data, snoekolonne):
    snoedybder_per_sesong = {}

    for rad in data[1:]:
        dato = rad[2]
        snoedybde = rad[snoekolonne]

        if snoedybde == "" or snoedybde == "-":
            continue

        dag, maaned, aar = map(int, dato.split("."))

        # Bare november til april
        if maaned not in [11, 12, 1, 2, 3, 4]:
            continue

        # November og desember tilhører startåret
        if maaned == 11 or maaned == 12:
            sesong = aar
        else:
            sesong = aar - 1

        if sesong not in snoedybder_per_sesong:
            snoedybder_per_sesong[sesong] = {}

        # Lagrer en snødybde per dato
        snoedybder_per_sesong[sesong][dato] = float(
            snoedybde.replace(",", ".")
        )

    sesonger = []
    skidager = []

    for sesong in sorted(snoedybder_per_sesong):
        snoedybder = snoedybder_per_sesong[sesong]

        start = date(sesong, 11, 1)
        slutt = date(sesong + 1, 4, 30)
        antall_dager = (slutt - start).days + 1

        # Minst halvparten av dagene må ha målinger
        if len(snoedybder) >= antall_dager / 2:
            antall_skidager = 0

            for snoedybde in snoedybder.values():
                if snoedybde >= 20:
                    antall_skidager += 1

            sesonger.append(sesong)
            skidager.append(antall_skidager)

    return sesonger, skidager


stasjoner = {
    "Oslo Blindern": oslo,
    "Røros": roeros,
    "Tromsø": tromsoe,
    "Værnes": vaernes,
    "Venabu": venabu,
    "Sinnes": sinnes
}


for navn, data in stasjoner.items():
    snoekolonne = data[0].index("Snødybde")
    sesonger, skidager = finn_skisesonger(data, snoekolonne)

    plt.plot(sesonger, skidager, label=navn)


plt.xlabel("Skisesong (startår)")
plt.ylabel("Antall dager med skiføre")
plt.title("Antall skidager per skisesong (minst 20 cm snø)")
plt.legend()
plt.grid()
plt.show()