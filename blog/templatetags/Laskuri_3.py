import math
from django import template
register = template.Library()

#Staattiset taulukkoarvot
exec(compile(source=open('/home/ari1/Eco-App/myenv/mete_project/mete_project/Taulukot.py').read(), filename='Taulukot.py', mode='exec'))


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
def Kayntiaika_pv(data):
    Pv_kayntiaika = data.h_pv / 24
    return Pv_kayntiaika

@register.filter
def Kayntiaika_vko(data):
    Vko_kayntiaika = data.pv_vko / 7
    return Vko_kayntiaika


@register.filter
def LKV_netto(data):
    nettotarve = Kluokat[data.kayttotarkoitus].lkv
    return round(nettotarve,1)


@register.filter
def LKV_havio(data):
    if (data.lkvputken_eristys == 1):
        lkvhavio = LKV_table[data.lkv_tila].havio40
    elif (data.lkvputken_eristys == 2):
        lkvhavio = LKV_table[data.lkv_tila].havio100
    else:
        lkvhavio = 0
    return round(lkvhavio,1)

@register.filter
def LKV_hyotysuhde(data):
    lkvhyoty = 0
    if(data.kayttotarkoitus == 1): # Pientalo
        lkvhyoty = Elahde[data.lkv_lammitys].Vuosihyoty1
    else:
        lkvhyoty = Elahde[data.lkv_lammitys].Vuosihyoty2
    return lkvhyoty

@register.filter
def LKV_siirtohyoty(data):
    lkvsiirto = 0
    #jos vesikeskuslämmitys sitten 
    if (data.lkv_kierto):
#        VLOOKUP(C7;Aloitustaulukot!B77:U88;15;FALSE)
        lkvsiirto = Kluokat[data.kayttotarkoitus].lkv_kierto # kierto
    else:
#        VLOOKUP(C7;Aloitustaulukot!B77:U88;18;FALSE)) # eristys perustaso
        lkvsiirto = Kluokat[data.kayttotarkoitus].lkv_eriste # eristys perustaso
    return lkvsiirto

@register.filter
def LKV_siirto(data):
    if(data.lkv_kierto):
        EC51 = Kluokat[data.kayttotarkoitus].lkv_putki_ominais
        EC49 = Kluokat[data.kayttotarkoitus].lkv_kierto # kierto
    else:
        EC51 = 0
        EC49 = Kluokat[data.kayttotarkoitus].lkv_eriste # eristys perustaso
    Qlkv_siirto = LKV_table[data.lkv_tila].ominaisarvo[1] * EC51 * EC49
    return Qlkv_siirto

@register.filter
def LKV_siirtolampo(data):
    if(data.lkv_kierto):
        EC51 = Kluokat[data.kayttotarkoitus].lkv_putki_ominais
        EC49 = Kluokat[data.kayttotarkoitus].lkv_kierto # kierto
    else:
        EC51 = 0
        EC49 = Kluokat[data.kayttotarkoitus].lkv_eriste # eristys perustaso
    EC87 = LKV_table[data.lkv_tila].ominaisarvo[1] * EC51 * EC49
    EC9 = data.pinta_ala * data.kerrosmaara # kokonaisala
    Qlkv_siirtolampo = EC87 / 1000 * EC9 * 8760
    return round(Qlkv_siirtolampo,0)

@register.filter
def LKV_varastohavio(data):
    if (data.lkv_tila > 0):
        if (data.lkvputken_eristys == 2):
            EC47 = LKV_h[data.lkv_tila].m100
        elif (data.lkvputken_eristys == 1): 
            EC47 = LKV_h[data.lkv_tila].m40
        else:
            EC47 = 0
        Qlkv_varastohavio= EC47
    else:
        Qlkv_varastohavio= 0
    return round(Qlkv_varastohavio,0)

@register.filter
def LKV_lammitys(data):
    EC44 = Kluokat[data.kayttotarkoitus].lkv
    EC9 = data.pinta_ala * data.kerrosmaara # kokonaisala
    
    if(data.lkv_tila > 0):
        if (data.lkvputken_eristys == 2):
            EC47 = LKV_h[data.lkv_tila].m100
        elif (data.lkvputken_eristys == 1): 
            EC47 = LKV_h[data.lkv_tila].m40
        else:
            EC47 = 0
        EE88 = EC47
    else:
        EE88 = 0
    
    if (data.kayttotarkoitus == 1) and ((EC44 * EC9) > 4200):
        EC45 = 4200
    else:
        EC45 = EC44 * EC9 
    if(data.kayttotarkoitus == 1) and ((EC44* EC9) > EC45):
        EE86 =EC45
    else: 
        EE86 = EC44*EC9
    
    Tuloasarvo = EE86 + EE88
    return round(Tuloasarvo,0)
