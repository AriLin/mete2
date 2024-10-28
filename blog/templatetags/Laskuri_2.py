import math
from django import template
register = template.Library()

#Staattiset taulukkoarvot
exec(compile(source=open('/home/ari1/Eco-App/myenv/mete_project/mete_project/Taulukot.py').read(), filename='Taulukot.py', mode='exec'))

@register.filter
def Poistoilmavirta(data):
    P_ilmavirta = Kluokat[data.kayttotarkoitus].virta * data.pinta_ala * data.kerrosmaara
    return P_ilmavirta

@register.filter
def Tuloilmavirta(data):
    tulovirta = 0
    EC15 = data.iv_tapa
    if (EC15 > 2):
        tulovirta = Kluokat[data.kayttotarkoitus].virta * data.pinta_ala * data.kerrosmaara
    else:
        tulovirta = 0
    return tulovirta

@register.filter
def Korvausvirta(data):
    poistoilma = Kluokat[data.kayttotarkoitus].virta * data.pinta_ala * data.kerrosmaara
    if (data.iv_tapa > 2):
        tuloilmavirta = Kluokat[data.kayttotarkoitus].virta * data.pinta_ala * data.kerrosmaara
    else:
        tuloilmavirta = 0
    korvausvirta = poistoilma - tuloilmavirta
    return korvausvirta

@register.filter
def SPF_data(data):
    current_value = 0
    if (data.iv_tapa == 1):
        current_value = Uarvot[data.rakennusvuosi].iv_paino
    elif (data.iv_tapa == 2):
        current_value = Uarvot[data.rakennusvuosi].iv_poisto
    elif (data.iv_tapa == 3):
        current_value = Uarvot[data.rakennusvuosi].iv_tulopoisto
    return current_value


@register.filter
def Tsp_temp(data):
    tsp_lampo = 17
    return tsp_lampo


@register.filter
def D_puhallus(data):
    delta_lampo = 0.5
    return delta_lampo


@register.filter
def Kayntiaika_pv(data):
    Pv_kayntiaika = data.h_pv / 24
    return Pv_kayntiaika

@register.filter
def Kayntiaika_vko(data):
    Vko_kayntiaika = data.pv_vko / 7
    return Vko_kayntiaika

@register.filter
def IV_sahko(data):
    if (data.iv_tapa == 1): #SFP
        EC34 = Uarvot[data.rakennusvuosi].iv_paino
    elif (data.iv_tapa == 2):
        EC34 = Uarvot[data.rakennusvuosi].iv_poisto
    else:
        EC34 = Uarvot[data.rakennusvuosi].iv_tulopoisto

    EC31 = Kluokat[data.kayttotarkoitus].virta * data.pinta_ala * data.kerrosmaara # poistoilmavirta
    EC39 = data.h_pv / 24 # Käyntiaikasuhde vrk
    iv_sahko_energia = EC34 * (EC31/1000) * EC39 * 8760
    return round(iv_sahko_energia,2)

@register.filter
def IV_lampo(data):
    iv_lampo_energia = 0
    for kk in range(1,13):
        kk_ivlampo = 0
        EC39 = data.h_pv / 24 # Vuorokausi käyntisuhde
        EC40 = data.pv_vko / 7 # viikkokäyntisuhde
        EC31 = Kluokat[data.kayttotarkoitus].virta * data.pinta_ala * data.kerrosmaara # poistoilmavirta
        EC30 =  Uarvot[data.rakennusvuosi].Lto_h # LTO hyötysuhde
        EC63 = data.sisalampo
        EF3 = KkData[kk].k_lampo[data.alue] # kuukauden keskilämpö/alue
        TC5 = EF3 + EC30 * ( EC63 - EF3)
        EC38 = deltaT
        EC37 = Tsp
        EC8 = data.kerrosmaara
        if (TC5 >= (EC37 - EC8)):
            TE5 = EC37 - EC38 
        else: 
            TE5 = TC5
        if (KkData[kk].lto):
            TF5 = TE5
        else:
            TF5 = EF3
        TG5 = TF5 + 0.5
        if (TG5 > EC37):
            TH5 = TG5
        else:
            TH5 = EC37
        if (TG5 > EC37):
            TH5 = TG5
        else:
            TH5 = EC37
        if (KkData[kk].lto):
            TF5 = TE5
        else:
            TF5 = EF3
        AC94 = KkData[kk].tunnit # kuukauden tunnit
        if (KkData[kk].lto):
            kk_ivlampo = EC39 * EC40 * 1.2 * ( EC31 / 1000 ) * ( TH5 - EC38 - TF5 ) * AC94
        else:
            kk_ivlampo = 0
    iv_lampo_energia += kk_ivlampo
    return round(iv_lampo_energia,1)


