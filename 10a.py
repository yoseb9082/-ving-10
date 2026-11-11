import csv
import matplotlib.pyplot as plt
from datetime import datetime

def til_tall(tekst):
    if tekst in ["-", ""]:
     tekst = None
     return tekst
    else:
     tekst = float(tekst.replace(",","."))
     return tekst

def maks_av(liste):
   m_tall= []
   for verdi in liste:
    if verdi is not None:
       m_tall.append(verdi)
   if len(m_tall) == 0:
    return None
   return max(m_tall)

def min_av(liste):
  m_tall= []
  for verdi in liste:
    if verdi is not None:
      m_tall.append(verdi)
  if len(m_tall) == 0:
    return None
  return min(m_tall)

def total_nedbør(liste):
   m_tall= []
   for verdi in liste:
      if verdi is not None:
        m_tall.append(verdi)
   if len(m_tall) <= 20:
    return None
   return sum(m_tall)

  
     

with open("sinnes_2014_2025.csv", encoding="UTF-8") as fil:
    leser = csv.DictReader(fil, delimiter=";")
    
    måneder = []
    maks_snødybde = []
    tot_nedbør = []
    maks_temp = []
    min_temp = []
    maks_mvind = []

    per_måned = {}
    
    for rad in leser:
        if rad["Tid(norsk normaltid)"] in ["-", ""]:
         continue
        dato = datetime.strptime(rad["Tid(norsk normaltid)"], "%d.%m.%Y")
        middeltemperatur = til_tall(rad["Middeltemperatur (døgn)"])
        nedbør = til_tall(rad["Nedbør (døgn)"])
        HMvind = til_tall(rad["Høyeste middelvind (døgn)"]) 
        snødybde = til_tall(rad["Snødybde"])

        nøkkel = (dato.year, dato.month)
        if nøkkel not in per_måned:
           per_måned[nøkkel] = {"Middeltemperatur":[], "Nedbør":[],
            "HMVIND": [], "Snødybde": []}
        per_måned[nøkkel] ["Middeltemperatur"].append(middeltemperatur)
        per_måned[nøkkel] ["Nedbør"].append(nedbør) 
        per_måned[nøkkel] ["HMVIND"].append(HMvind)
        per_måned[nøkkel] ["Snødybde"].append(snødybde)

    for nøkkel in sorted(per_måned):
      data = per_måned[nøkkel]
      år, måned = nøkkel
      måneder.append(datetime(år, måned, 1))
      maks_snødybde.append(maks_av(data["Snødybde"]))
      total = total_nedbør(data["Nedbør"])
      tot_nedbør.append(total)
      if total is None:
          print(f"Total nedbør er ikke registrert for {år}-{måned}")
      maks_temp.append(maks_av(data["Middeltemperatur"]))
      min_temp.append(min_av(data["Middeltemperatur"]))
      maks_mvind.append(maks_av(data["HMVIND"]))

    plt.plot(måneder, maks_snødybde, label="Maks Snødybde")
    plt.plot(måneder, tot_nedbør, label="Total Nedbør")
    plt.plot(måneder, maks_temp, label="Maks middeltemperatur")
    plt.plot(måneder, min_temp, label="Min middeltemperatur")
    plt.plot(måneder, maks_mvind, label="Maks middelvind")
    plt.xlabel("Måned")
    plt.ylabel("Verdi")
    plt.legend()
    plt.show()
    

