
import csv
import matplotlib.pyplot as plt

# Lager 12 tomme lister, en for hver måned
vind = [[] for i in range(12)]

# Leser CSV-filen
with open("oslo_blindern_1954_2025_med_makstemperatur.csv", encoding="utf-8") as fil:
    leser = csv.reader(fil, delimiter=";")
    next(leser)  # Hopper over overskriften

    for rad in leser:
        dato = rad[2]
        vindstyrke = rad[6]

        if vindstyrke != "-":
            måned = int(dato[3:5])
            vind[måned - 1].append(float(vindstyrke.replace(",", ".")))

# Lager lister for resultatene
minimum = []
median = []
maksimum = []

# Går gjennom alle månedene
for liste in vind:
    liste.sort()

    minimum.append(min(liste))

    midten = len(liste) // 2

    if len(liste) % 2 == 0:
        median.append((liste[midten - 1] + liste[midten]) / 2)
    else:
        median.append(liste[midten])

    maksimum.append(max(liste))

# Plotter resultatene
måneder = range(1, 13)

plt.plot(måneder, minimum, label="Minimum")
plt.plot(måneder, median, label="Median")
plt.plot(måneder, maksimum, label="Maksimum")

plt.xlabel("Måned")
plt.ylabel("Vindstyrke (m/s)")
plt.title("Vindstyrke for Oslo Blindern")
plt.xticks(måneder)
plt.legend()
plt.grid()
plt.show()
