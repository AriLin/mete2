import math
from django import template
register = template.Library()

#Staattiset taulukkoarvot
exec(compile(source=open('/home/ari1/Eco-App/myenv/mete_project/mete_project/Taulukot.py').read(), filename='Taulukot.py', mode='exec'))



@register.filter
def KL_ominaisteho(data):
    Kuluttaja_teho = Kluokat[data.kayttotarkoitus].laitteet
    return Kuluttaja_teho
    
@register.filter
def Valaistus_ominaisteho(data):
    Valo_teho = Kluokat[data.kayttotarkoitus].valaistus
    return Valo_teho

@register.filter
def KL_teho(data):
    Kuluttaja_teho = Kluokat[data.kayttotarkoitus].laitteet * data.pinta_ala * data.kerrosmaara
    return Kuluttaja_teho

@register.filter
def Valaistus_teho(data):
    Valo_teho = Kluokat[data.kayttotarkoitus].valaistus * data.pinta_ala * data.kerrosmaara
    return Valo_teho

@register.filter
def KL_energia(data):
    Kuluttaja_teho = Kluokat[data.kayttotarkoitus].laitteet * data.pinta_ala * data.kerrosmaara
    EC71 = data.kul_h_pv / 24 # vuorokausi käyttösuhde
    EC72 = data.kul_pv_vko / 7 # viikoittainen käyttösuhde
    if (EC71 * EC72 == 1): # käyttöasteen suhde
        EC79 = 1
    else:
        EC79 = EC71 * EC72
    EC74 = Kluokat[data.kayttotarkoitus].kuorma
    EE83 = (Kuluttaja_teho / 1000) * EC79 * EC74 * 8760
    return round(EE83,0)

@register.filter
def Valaistus_energia(data):
    Valo_teho = Kluokat[data.kayttotarkoitus].valaistus * data.pinta_ala * data.kerrosmaara
    EC71 = data.val_h_pv / 24 # vuorokausi käyttösuhde
    EC72 = data.val_pv_vko / 7 # viikoittainen käyttösuhde
    if (EC71 * EC72 == 1): # käyttöasteen suhde
        EC79 = 1
    else:
        EC79 = EC71 * EC72
    if(data.kayttotarkoitus < 3):
        EC76 = 0.1
    else:
        EC76 =Kluokat[data.kayttotarkoitus].kuorma # Valaistuksen käyttöaste
    EE84 = (Valo_teho / 1000) * EC79 * EC76 * 8760
    return round(EE84,0)
