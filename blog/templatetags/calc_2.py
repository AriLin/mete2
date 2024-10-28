import re
from math import floor,ceil
from django import template
register = template.Library()

from dataclasses import dataclass

@dataclass
class Solarmap:
    kk: str
    Aurinko: []
    Teho: []

solartaulu = []
# Kuukausi,aurinkoaika/24h,[Alue1,ALue2,Alue3],aurinkoteho[Alue1,Alue2,ALue3]
solartaulu.append(Solarmap("keskiarvo", [52,52,44],[100.9,93.96,86.03]))
solartaulu.append(Solarmap("tammikuu", [26,25,15],[13.1,9.7,2]))
solartaulu.append(Solarmap("helmikuu", [39,37,33],[44.3,45.7,28.0]))
solartaulu.append(Solarmap("maaliskuu", [50,49,49],[106.7,84.5,85.1]))
solartaulu.append(Solarmap("huhtikuu", [54,62,66],[154.9,137.2,181.8]))
solartaulu.append(Solarmap("toukokuu", [74,74,84],[183.0,189.7,141.3]))
solartaulu.append(Solarmap("kesäkuu", [82,83,100],[167.6,163.7,159.7]))
solartaulu.append(Solarmap("heinäkuu", [77,78,93],[189.8,172.5,164.3]))
solartaulu.append(Solarmap("elokuu", [66,66,71],[152.1,143.2,121.5]))
solartaulu.append(Solarmap("syyskuu", [54,54,55],[126.9,113.5,109.3]))
solartaulu.append(Solarmap("lokakuu", [43,41,39],[44.3,47.6,33.2]))
solartaulu.append(Solarmap("marraskuu", [31,29,22],[17.0,14.9,5.8]))
solartaulu.append(Solarmap("joulukuu", [25,21,3],[11.2,5.3,0.3]))

#print (solartaulu[1].kk,"Aika:",solartaulu[1].Aurinko[0],solartaulu[1].Teho[0])

# Static values for calculations
#data.aurinko.korjauskerroin = paneeleiden suuntaus kohti aurinkoa
#solartaulu.Teho = aurigon säteilyteho
#solartaulu.Aurinko = Kuukausden keskimääinen valoisa-aika
hyotysuhde = 0.17 #yleinen aurinkopaneelin sähköntuotannon hyötysuhde

#Tarvittava kennostokoko
@register.filter
def kennostokoko(data):
    koko = round(data.tavoite_teho / data.paneeli_teho) * data.paneelin_ala
    if koko == 0:
        return ("ERROR: päivitä rakennustiedot!!")
    else:
        return (round(koko,2))


# laskettu energiakulutus
@register.filter
def kulutus(data):
    my_kulutus = 0
    my_kulutus += data.aurinko.tammi
    my_kulutus += data.aurinko.helmi
    my_kulutus += data.aurinko.maalis
    my_kulutus += data.aurinko.huhti
    my_kulutus += data.aurinko.touko
    my_kulutus += data.aurinko.kesa
    my_kulutus += data.aurinko.heina
    my_kulutus += data.aurinko.elo
    my_kulutus += data.aurinko.syys
    my_kulutus += data.aurinko.loka
    my_kulutus += data.aurinko.marras
    my_kulutus += data.aurinko.joulu

    if my_kulutus == 0:
        return ("ERROR: päivitä rakennustiedot!!")
    else:
        return (round(my_kulutus,1))

# arvioitu ylijäämä
@register.filter
def ylijaama(data):

    my_kulutus = []
    my_kulutus.append(0)
    my_kulutus.append(data.aurinko.tammi)
    my_kulutus.append(data.aurinko.helmi)
    my_kulutus.append(data.aurinko.maalis)
    my_kulutus.append(data.aurinko.huhti)
    my_kulutus.append(data.aurinko.touko)
    my_kulutus.append(data.aurinko.kesa)
    my_kulutus.append(data.aurinko.heina)
    my_kulutus.append(data.aurinko.elo)
    my_kulutus.append(data.aurinko.syys)
    my_kulutus.append(data.aurinko.loka)
    my_kulutus.append(data.aurinko.marras)
    my_kulutus.append(data.aurinko.joulu)

    my_alue = data.profile.alue -1
    if data.profile.alue > 1:
        my_alue = data.profile.alue -2
    kennosto_koko = (data.aurinko.tavoite_teho / data.aurinko.paneeli_teho) * data.aurinko.paneelin_ala

    tuotto = 0
    tuotto1 = 0
    my_ylituotto = 0
    my_kulutus_paivalla1 = 0
    my_kulutus_paivalla2 = 0
    for x in range(1,13):
        tuotto1 = hyotysuhde * data.aurinko.korjauskerroin * solartaulu[x].Teho[my_alue] * (solartaulu[x].Aurinko[my_alue] / 100 ) * kennosto_koko
        my_kulutus_paivalla1 = my_kulutus[x] * (solartaulu[x].Aurinko[my_alue] /100 )
        if tuotto1 - my_kulutus_paivalla1  > 0:
            my_ylituotto += tuotto1 - my_kulutus_paivalla1
        my_kulutus_paivalla2 += my_kulutus_paivalla1
        tuotto += tuotto1
        
    if tuotto == 0 or my_ylituotto == 0:
        return ("ERROR: päivitä mitoitustiedot!!")
    else:
       my_ylijaama_pros = (my_ylituotto / my_kulutus_paivalla2) * 100
       return (round(my_ylijaama_pros,1))

# arvioitu tuotantomäärä
@register.filter
def tuotanto(data):
    my_alue = data.profile.alue -1
    if data.profile.alue > 1:
        my_alue = data.profile.alue -2
    kennosto_koko = (data.aurinko.tavoite_teho / data.aurinko.paneeli_teho) * data.aurinko.paneelin_ala

    tuotto = 0
    for x in range(1,13):
        tuotto += hyotysuhde * data.aurinko.korjauskerroin * solartaulu[x].Teho[my_alue] * (solartaulu[x].Aurinko[my_alue] / 100 ) * kennosto_koko
    #    print('teho:', solartaulu[x].Teho[my_alue], ' aika:', (solartaulu[x].Aurinko[my_alue] / 100 ), ' kenno:', kennosto_koko)
    if tuotto == 0:
        return ("ERROR: päivitä rakennustiedot!!")
    else:
        return (round(tuotto,1))


@register.filter
def kk_tuotanto(data,data2):
    part1 = int(data2)
    part2 = round((int(data2)-data2)*-10)
    my_alue = data.profile.alue -1
    if data.profile.alue > 1:
        my_alue = data.profile.alue -2

#    print(part1 , "kk-", solartaulu[part1].Teho[my_alue],'Teho' )

    kennosto_koko = (data.aurinko.tavoite_teho / data.aurinko.paneeli_teho) * data.aurinko.paneelin_ala
    tuotto = hyotysuhde * data.aurinko.korjauskerroin * solartaulu[part1].Teho[my_alue] *(solartaulu[data2].Aurinko[my_alue] / 100 ) * 1 * kennosto_koko
    
    if tuotto == 0:
        return ("ERROR: päivitä rakennustiedot!!")
    else:
        return (round(tuotto,1))
