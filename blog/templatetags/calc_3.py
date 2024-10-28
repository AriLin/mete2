import os
import re
import math
from django import template
from dataclasses import dataclass

register = template.Library()

# ESIMERKKI PAIKALLISESTA TIETOTAULUSTA / MUUTTUJISTA

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


@dataclass
class vilp_data:
    luokka: int
    suhdeluku: int
    A: []

vilp_taulu = []

# luokka = 3-10 (as range 0.3 - 1.0)
# suhdeluku = 1-4 (1= 0.5,2 = 1, 3= 2, 4 = 4)
# A = [[V1-2 30,V1-2 40,V1-2 50,V1-2 60], [V3 30,V3 40,V3 50,V3 60], [V4 30,V4 40,V4 50,V4 60]]

vilp_taulu.append(vilp_data(3,1, [[0.33,0.33,0.33,0.33],[0.31,0.31,0.31,0.31],[0.28,0.28,0.28,0.28]]))
vilp_taulu.append(vilp_data(3,2, [[0.39,0.39,0.39,0.39],[0.37,0.37,0.37,0.37],[0.33,0.33,0.33,0.33]]))
vilp_taulu.append(vilp_data(3,3, [[0.49,0.48,0.47,0.46],[0.46,0.45,0.44,0.44],[0.40,0.39,0.39,0.38]]))
vilp_taulu.append(vilp_data(3,4, [[0.56,0.54,0.52,0.50],[0.53,0.51,0.49,0.48],[0.46,0.44,0.43,0.41]]))
vilp_taulu.append(vilp_data(4,1, [[0.44,0.44,0.44,0.44],[0.42,0.42,0.42,0.42],[0.38,0.38,0.38,0.38]]))
vilp_taulu.append(vilp_data(4,2, [[0.52,0.52,0.52,0.52],[0.50,0.50,0.49,0.49],[0.44,0.44,0.44,0.44]]))
vilp_taulu.append(vilp_data(4,3, [[0.63,0.61,0.60,0.58],[0.60,0.58,0.57,0.56],[0.52,0.51,0.50,0.49]]))
vilp_taulu.append(vilp_data(4,4, [[0.68,0.65,0.63,0.61],[0.64,0.62,0.60,0.58],[0.56,0.54,0.52,0.51]]))
vilp_taulu.append(vilp_data(5,1, [[0.54,0.54,0.54,0.54],[0.52,0.52,0.52,0.52],[0.47,0.47,0.47,0.47]]))
vilp_taulu.append(vilp_data(5,2, [[0.65,0.64,0.64,0.63],[0.62,0.61,0.61,0.60],[0.55,0.54,0.54,0.53]]))
vilp_taulu.append(vilp_data(5,3, [[0.73,0.71,0.69,0.68],[0.70,0.68,0.66,0.64],[0.61,0.60,0.58,0.57]]))
vilp_taulu.append(vilp_data(5,4, [[0.78,0.75,0.72,0.70],[0.74,0.71,0.68,0.66],[0.64,0.62,0.60,0.58]]))
vilp_taulu.append(vilp_data(6,1, [[0.64,0.64,0.64,0.64],[0.62,0.62,0.62,0.61],[0.55,0.55,0.55,0.55]]))
vilp_taulu.append(vilp_data(6,2, [[0.75,0.74,0.72,0.72],[0.72,0.70,0.69,0.69],[0.64,0.63,0.62,0.61]]))
vilp_taulu.append(vilp_data(6,3, [[0.82,0.79,0.77,0.75],[0.72,0.70,0.69,0.69],[0.64,0.63,0.62,0.61]]))
vilp_taulu.append(vilp_data(6,4, [[0.84,0.82,0.80,0.77],[0.81,0.78,0.76,0.73],[0.71,0.69,0.66,0.64]]))
vilp_taulu.append(vilp_data(7,1, [[0.73,0.73,0.73,0.73],[0.70,0.70,0.70,0.70],[0.63,0.63,0.63,0.63]]))
vilp_taulu.append(vilp_data(7,2, [[0.83,0.81,0.80,0.78],[0.79,0.78,0.76,0.75],[0.71,0.69,0.68,0.67]]))
vilp_taulu.append(vilp_data(7,3, [[0.87,0.85,0.83,0.82],[0.84,0.82,0.80,0.78],[0.75,0.73,0.71,0.69]]))
vilp_taulu.append(vilp_data(7,4, [[0.89,0.87,0.85,0.83],[0.86,0.84,0.81,0.79],[0.76,0.74,0.72,0.70]]))
vilp_taulu.append(vilp_data(8,1, [[0.81,0.80,0.80,0.79],[0.80,0.80,0.79,0.78],[0.72,0.71,0.71,0.70]]))
vilp_taulu.append(vilp_data(8,2, [[0.88,0.87,0.85,0.84],[0.86,0.85,0.84,0.82],[0.77,0.76,0.74,0.73]]))
vilp_taulu.append(vilp_data(8,3, [[0.90,0.89,0.88,0.86],[0.88,0.86,0.85,0.84],[0.79,0.77,0.76,0.74]]))
vilp_taulu.append(vilp_data(8,4, [[0.91,0.90,0.88,0.87],[0.88,0.87,0.85,0.84],[0.79,0.77,0.76,0.74]]))
vilp_taulu.append(vilp_data(9,1, [[0.89,0.88,0.88,0.87],[0.86,0.85,0.84,0.83],[0.77,0.76,0.76,0.75]]))
vilp_taulu.append(vilp_data(9,2, [[0.92,0.91,0.90,0.89],[0.89,0.88,0.87,0.86],[0.81,0.80,0.78,0.77]]))
vilp_taulu.append(vilp_data(9,3, [[0.92,0.91,0.90,0.89],[0.90,0.89,0.88,0.87],[0.81,0.80,0.79,0.77]]))
vilp_taulu.append(vilp_data(9,4, [[0.92,0.91,0.90,0.89],[0.89,0.88,0.87,0.86],[0.81,0.80,0.78,0.77]]))
vilp_taulu.append(vilp_data(10,1, [[0.92,0.92,0.91,0.90],[0.90,0.89,0.88,0.88],[0.82,0.81,0.80,0.79]]))
vilp_taulu.append(vilp_data(10,2, [[0.93,0.92,0.92,0.91],[0.91,0.90,0.90,0.89],[0.83,0.82,0.81,0.80]]))
vilp_taulu.append(vilp_data(10,3, [[0.93,0.92,0.92,0.91],[0.91,0.90,0.89,0.89],[0.83,0.82,0.81,0.80]]))
vilp_taulu.append(vilp_data(10,4, [[0.93,0.92,0.91,0.90],[0.90,0.90,0.89,0.88],[0.82,0.81,0.80,0.79]]))


spf_taulu = [[0,2.8,2.8,2.8,2.7],[30,2.8,2.8,2.8,2.7],[40,2.5,2.5,2.5,2.4],[50,2.3,2.3,2.3,2.2],[60,2.2,2.2,2.1,2.0],[60,1.8,1.8,1.6,1.3]]
# ilma-ilma, ilma-vesi 30, ilma-vesi 40, ilma-vesi 50, ilma-vesi 60, ilma-lkv-vesi[alue1,alue2,alue3,alue4]

spf_lampo = 3 # 60 astetta

lammonleviamiskerroin = 0.1
tuotto_osuus = 0.85
SPF = 3.0

def VyohykeKerroin(data):
    vilp_suhde = round((data.pumppu.vilp_teho / data.profile.sahkokWh) * 10)
    if vilp_suhde < 3:
        vilp_suhde = 3

    myQlkv = 35 * data.pumppu.ilp_pinta_ala
    lkv_suhde = round(myQlkv / data.profile.sahkokWh)
    saa_rivi = 4*(vilp_suhde-3) + lkv_suhde
    if saa_rivi > 31:
        saa_rivi = 31 # taulukon maksimirivinro
# QUICK FIX - vip_taulu aluedatan taulukko-koon korjaamiseen
    vilp_alue = data.profile.alue
    if data.profile.alue > 2:
        vilp_alue = 2
    Vkerroin = vilp_taulu[saa_rivi].A[(vilp_alue)][spf_lampo]  
    return Vkerroin

@register.filter
def nettotuotto(data):
    n_tuotto = (data.ilp_pinta_ala + lammonleviamiskerroin * (data.ilp_pinta_ala - data.ilp_pinta_ala)) * (data.ilp_kulutuskWh/data.ilp_pinta_ala)
    return (round(n_tuotto,2))

@register.filter
def nettosaasto(data):
    n_tuotto = (data.ilp_pinta_ala + lammonleviamiskerroin * (data.ilp_pinta_ala - data.ilp_pinta_ala)) * (data.ilp_kulutuskWh/data.ilp_pinta_ala)
    n_saasto = n_tuotto * ( 1-(1/SPF * tuotto_osuus))
    return (round(n_saasto,2))

@register.filter
def sahkonkaytto(data):
    n_tuotto = (data.ilp_pinta_ala + lammonleviamiskerroin * (data.ilp_pinta_ala - data.ilp_pinta_ala)) * (data.ilp_kulutuskWh/data.ilp_pinta_ala)
    sahkokaytto = n_tuotto/(SPF * tuotto_osuus)
    return (round(sahkokaytto,2))

@register.filter
def maxtuotto(data):
    max_tuotto = data.ilp_vuosituotto  * SPF
    return (round(max_tuotto,2))

@register.filter
def uno_kattavuus(data):
    uno_riittavyys = ((data.ilp_vuosituotto  * SPF) / data.ilp_kulutuskWh) * 100
    return (round(uno_riittavyys))

@register.filter
def all_kattavuus(data):
    all_riittavyys = ((data.ilp_vuosituotto  * SPF * data.ilp_maara) / data.ilp_kulutuskWh) * 100
    return (round(all_riittavyys))

@register.filter
def pumppu_kpl(data):
    kpl_pumppu = math.ceil(data.ilp_kulutuskWh /  (data.ilp_vuosituotto  * SPF))
    return (round(kpl_pumppu))

@register.filter
def LPtuotto(data):
    tmSuhde = VyohykeKerroin(data)
    myQlisalkv = (1-tmSuhde) * data.profile.sahkokWh
    myQlptila =  (data.profile.sahkokWh - myQlisalkv)
    return (round(myQlptila,2))

@register.filter
def QlisaTila(data):
    tmSuhde = VyohykeKerroin(data)
    myQlisaTila = (1-tmSuhde) * data.profile.sahkokWh
    return (round(myQlisaTila,2))

@register.filter
def QlisaLkv(data):
    tmSuhde = VyohykeKerroin(data)
    myQlkv = 35 * data.pumppu.ilp_pinta_ala
    myQlisaLkv = (1-tmSuhde) * myQlkv
    return (round(myQlisaLkv,2))

@register.filter
def Qlkv(data):
    myQlkv = 35 * data.pumppu.ilp_pinta_ala
    return (round(myQlkv,2))

@register.filter
def Qtila(data):
    myQtila = data.profile.sahkokWh
    return (myQtila)

