import csv
import os
import matplotlib.pyplot as plt

mappe = os.path.dirname(os.path.abspath(__file__))


def tell_dager(filnavn):
    data = {}

    with open(os.path.join(mappe, filnavn), newline="", encoding="utf-8-sig") as fil:
        leser = csv.reader(fil, delimiter=";")
        next(leser)

        for rad in leser:
            if len(rad) < 4:
                continue

            try:
                aar = int(rad[2][-4:])
                maks = float(rad[3].replace(",", "."))
            except ValueError:
                continue

            if aar not in data:
                data[aar] = [0, 0, 0, 0]

            data[aar][0] = data[aar][0] + 1
            if maks > 20:
                data[aar][1] = data[aar][1] + 1
            if maks > 25:
                data[aar][2] = data[aar][2] + 1
            if maks > 30:
                data[aar][3] = data[aar][3] + 1

    aar_liste = []
    sommerdager = []
    hoysommerdager = []
    tropedager = []

    for aar in sorted(data):
        if data[aar][0] >= 350:
            aar_liste.append(aar)
            sommerdager.append(data[aar][1])
            hoysommerdager.append(data[aar][2])
            tropedager.append(data[aar][3])

    return aar_liste, sommerdager, hoysommerdager, tropedager


alle_stasjoner = [
    ["Oslo - Blindern", "oslo_blindern_1954_2025_med_makstemperatur.csv"],
    ["Tromsø", "tromsoe_1954_2025_med_makstemperatur.csv"],
    ["Værnes", "vaernes_1954_2025_med_makstemperatur.csv"],
    ["Røros", "roeros_1954_2025_med_makstemperatur.csv"],
    ["Venabu", "venabu_1954_2025_med_makstemperatur.csv"],
]

# Ta bare med stasjoner der filen finnes i mappen
stasjoner = []
for stasjon in alle_stasjoner:
    if os.path.exists(os.path.join(mappe, stasjon[1])):
        stasjoner.append(stasjon)
    else:
        print("Finner ikke", stasjon[1], "- hopper over", stasjon[0])

# Plott 1: Oslo - Blindern
navn = stasjoner[0][0]
aar, sommer, hoysommer, tropedager = tell_dager(stasjoner[0][1])

plt.figure(1)
plt.plot(aar, sommer, label="Sommerdager (> 20 °C)")
plt.plot(aar, hoysommer, label="Høysommerdager (> 25 °C)")
plt.plot(aar, tropedager, label="Tropedager (> 30 °C)")
plt.title(navn)
plt.xlabel("År")
plt.ylabel("Antall dager")
plt.legend()
plt.grid(True)

# Plott 2: alle stasjoner som ble funnet
plt.figure(2, figsize=(12, 9))
for i in range(len(stasjoner)):
    navn = stasjoner[i][0]
    aar, sommer, hoysommer, tropedager = tell_dager(stasjoner[i][1])

    plt.subplot(3, 2, i + 1)
    plt.plot(aar, sommer, label="Sommerdager")
    plt.plot(aar, hoysommer, label="Høysommerdager")
    plt.plot(aar, tropedager, label="Tropedager")
    plt.title(navn)
    plt.xlabel("År")
    plt.ylabel("Antall dager")
    plt.legend()
    plt.grid(True)

plt.tight_layout()
plt.show()
