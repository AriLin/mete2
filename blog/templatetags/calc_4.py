import re
from django import template
register = template.Library()

# ESIMERKKI PAIKALLISESTA TIETOTAULUSTA / MUUTTUJISTA

from dataclasses import dataclass

@dataclass
class Sääalue:
    kk: str
    A: []

säätaulu = []

säätaulu.append(Sääalue("keskiarvo", [0,6.968, 5.325, 4.1771, 1.533]))
säätaulu.append(Sääalue("tammikuu", [0,-2.04, -4.92, -7.875, -11]))
säätaulu.append(Sääalue("helmikuu", [0,-1.5, -3.76, -5.725, -10.5]))
säätaulu.append(Sääalue("maaliskuu", [0,3.1, -0.78, -2.425, -3.6]))
säätaulu.append(Sääalue("huhtikuu", [0,3.52, 1.56, 1.1, -0.15]))
säätaulu.append(Sääalue("toukokuu", [0,9.36, 9.3, 8.35, 6.16]))
säätaulu.append(Sääalue("kesäkuu", [0,16.6, 16.24, 15.525, 13.65]))
säätaulu.append(Sääalue("heinäkuu", [0,17.6, 17.36, 17.525, 16.05]))
säätaulu.append(Sääalue("elokuu", [0,18.32, 17.66, 16.775, 14.45]))
säätaulu.append(Sääalue("syyskuu", [0,9.22, 8.66, 8.45, 6.65]))
säätaulu.append(Sääalue("lokakuu", [0,6.36, 6.36, 5.25, 2.05]))
säätaulu.append(Sääalue("marraskuu", [0,3.14, 0.8, -1.375, -4.9]))
säätaulu.append(Sääalue("joulukuu", [0,-2.7, -4.58, -5.45, -10.45]))

#print (säätaulu[0].kk,"Alue3:",säätaulu[0].A[1])


@register.filter
def calc_4a(data):
    Korjattu_vuosi = data.rakennusvuosi * 2
    return (Korjattu_vuosi)

@register.filter
def calc_4b(data):
    korjattu_pinta_ala = data.pinta_ala * 5
    return (korjattu_pinta_ala)

