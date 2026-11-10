import csv
import matplotlib.pyplot as plt

vind = [[] for i in range(12)]

# Leser CSV-filen
with open("oslo_blindern_1954_2025_med_makstemperatur.csv",
          encoding="utf-8") as fil:

    leser = csv.reader(fil, delimiter=";")
    next(leser)  

    for rad in leser:

        if len(rad) < 7:
            continue

        dato = rad[2].strip()
        vindstyrke = rad[6].strip()

        if dato != "" and vindstyrke != "" and vindstyrke != "-":

            måned = int(dato[3:5])

            vind[måned - 1].append(
                float(vindstyrke.replace(",", "."))
            )

minimum = []
median = []
maksimum = []

for liste in vind:

    liste.sort()

    if len(liste) > 0:

        minimum.append(min(liste))
        maksimum.append(max(liste))

        midten = len(liste) // 2

        if len(liste) % 2 == 0:
            median.append(
                (liste[midten - 1] + liste[midten]) / 2
            )
        else:
            median.append(liste[midten])

    else:
        minimum.append(float("nan"))
        median.append(float("nan"))
        maksimum.append(float("nan"))


måneder = range(1, 13)

plt.plot(måneder, minimum, label="Minimum")
plt.plot(måneder, median, label="Median")
plt.plot(måneder, maksimum, label="Maksimum")

plt.xlabel("Måned")
plt.ylabel("Vindstyrke (m/s)")
plt.title("Vindstatistikk for Oslo Blindern")

plt.xticks(måneder)
plt.legend()
plt.grid()

plt.show()
