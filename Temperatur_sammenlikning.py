import csv 
import matplotlib.pyplot as plt

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

def finn_gjennomsnitt(data,temperatur_kolonne = 4):

    temperaturer_per_aar = {}

    for rad in data[1:]:
        dato = rad[2]
        temperatur = rad[temperatur_kolonne]

        if temperatur == "" or temperatur == "-":
            continue

        aar = int(dato.split(".")[2])
        temperatur = float(temperatur.replace(",", "."))

        if aar not in temperaturer_per_aar:
            temperaturer_per_aar[aar] = []

        temperaturer_per_aar[aar].append(temperatur)

    aarstall = []
    gjennomsnitt = []

    for aar in sorted(temperaturer_per_aar):
        
        if len(temperaturer_per_aar[aar]) >= 300:   
            snitt = sum(temperaturer_per_aar[aar]) / len(temperaturer_per_aar[aar])

            aarstall.append(aar)
            gjennomsnitt.append(snitt)

    return aarstall, gjennomsnitt

stasjoner = {
    "Oslo Blindern": oslo,
    "Røros": roeros,
    "Tromsø": tromsoe,
    "Værnes": vaernes,
    "Venabu": venabu,
    "Sinnes": sinnes
}

for navn, data in stasjoner.items():    

    if navn == "Sinnes":
        aarstall, gjennomsnitt = finn_gjennomsnitt(data, 3)
    else:
        aarstall, gjennomsnitt = finn_gjennomsnitt(data, 4)

    plt.plot(aarstall, gjennomsnitt, label=navn)

plt.xlabel("År")
plt.ylabel("Gjennomsnittstemperatur (°C)")
plt.title("Årlig gjennomsnittstemperatur")
plt.legend()
plt.grid()
plt.show()

