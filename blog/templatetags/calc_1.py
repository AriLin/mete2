import re
import os
import math
from django import template
register = template.Library()
from dataclasses import dataclass

# Staatttiset taulukkoarvot
exec(compile(source=open('/home/ari1/Eco-App/myenv/mete_project/mete_project/Taulukot.py').read(), filename='Taulukot.py', mode='exec'))

#ALASVETOVALIKOT * * * * * * * *
@register.filter
def mete_bool_(data):
    if data == True:
        return "Kyllä"
    elif data == False:
        return "Ei"
    else:
        return "ERROR"


@register.filter
def meteAreas_(data):
    if data == 1:
        return "Alue 1"
    elif data == 2:
        return "Alue 2"
    elif data == 3:
        return "Alue 3"
    elif data == 4:
        return "Alue 4"
    else :
        return "ERROR"

@register.filter
def meteHeating_(data):
    if data == 1:
        return "Kaukolämpö"
    elif data == 2:
        return "Sähkö"
    elif data == 3:
        return "Maalämpö"
    elif data == 4:
        return "Öljy"
    elif data == 5:
        return "IVLP + sähkö"
    elif data == 6:
        return "PILP + sähkö"
    elif data == 7:
        return "Pelletti"
    elif data == 8:
        return "IVLP + öljy"
    else :
        return "ERROR"

@register.filter
def kayttotarkoitus_(data):
    return Kluokat[data].luokka

@register.filter
def Lampokapasiteetti(data):
    return Kluokat[data].ominais_C

@register.filter
def lupavuosi_(data):
    return Uarvot[data].yy
    
@register.filter
def Lto_h(data):
    return Uarvot[data].Lto_h

@register.filter
def Vuotoluku(data):
    return Uarvot[data].vuoto

@register.filter
def Vuotokerroin(data):
    if data == 1:
        kerroin = 35
    elif data == 2:
        kerroin = 24
    elif data == 3:
        kerroin = 20
    elif data == 4:
        kerroin = 15
    else:
        kerroin = 0
    return kerroin

@register.filter
def Ulkovaippa(data):
    EC10 = data.pinta_ala
    EC8 = data.kerrosmaara
    ulkoseinä = (math.sqrt(EC10)*huonekorkeus*EC8*4)-((math.sqrt(EC10)*huonekorkeus*EC8*4)*0.15)-((math.sqrt(EC10)*huonekorkeus*EC8*4)*0.05)
    ovet = ((math.sqrt(EC10)*huonekorkeus*EC8*4)*0.05)
    ikkunat = ((math.sqrt(EC10)*huonekorkeus*EC8*4)*0.15)
    ulkovaippa = ulkoseinä + ikkunat + ovet + data.pinta_ala + data.yläpohja_ala
#    print(ulkoseinä , ikkunat , ovet , data.pinta_ala , data.yläpohja_ala, ulkovaippa)
    return round(ulkovaippa,1)

@register.filter
def Tilavuus(data):
    tilavuus = data.pinta_ala * 2.8 * data.kerrosmaara
    return tilavuus

@register.filter
def lkv_tila_(data):
    return LKV_h[data].teksti
    
@register.filter
def l_tuotto_(data):
    if data == 1:
        return "Öljylämpökattila"
    elif data == 2:
        return "Kaasulämpökattila"
    elif data == 3:
        return "Öljykondenssikattila"
    elif data == 4:
        return "Kaasukondenssikattila"
    elif data == 5:
        return "Pellettikattila"
    elif data == 6:
        return "Puukattila"
    elif data == 7:
        return "Sähkölämpökattila"
    elif data == 8:
        return "Kaukolämpö"
    elif data == 9:
        return "Sähkölämmitys"
    else:
        return "ERROR"

@register.filter
def l_jako_(data):
    if data == 1:
        return "Vesipatteri 45/35"
    elif data == 2:
        return "Vesipatteri 70/40"
    elif data == 3:
        return "Vesipatteri 90/70"
    elif data == 4:
        return "Vesipatteri 70/40 jakotukilla"
    elif data == 5:
        return "Vesipatteri 45/35 jakotukilla"
    elif data == 6:
        return "Lattia vesilämmitys 40/30"
    elif data == 7:
        return "Kattolämmitys (sähkö)"
    elif data == 8:
        return "Ikkunalämmitys (sähkö)"
    elif data == 9:
        return "Ilmanvaihtolämmitys"
    elif data == 10:
        return "Sähköpatterit"
    elif data == 11:
        return "Lattialämmitys (sähkö)"
    elif data == 12:
        return "Muu lämmönjakotapa"
    else:
        return "ERROR"

@register.filter
def lkv_heat_(data):
    if data == 1:
        return "Öljylämpökattila"
    elif data == 2:
        return "Kaasulämpökattila"
    elif data == 3:
        return "Öljykondenssikattila"
    elif data == 4:
        return "Kaasukondenssikattila"
    elif data == 5:
        return "Pellettikattila"
    elif data == 6:
        return "Puukattila"
    elif data == 7:
        return "Sähkölämpökattila"
    elif data == 8:
        return "Kaukolämpö"
    elif data == 9:
        return "Sähkölämmitys"
    else:
        return "ERROR"

@register.filter
def ilmanvaihto_(data):
    if data == 1:
        return "Painovoimainen"
    elif data == 2:
        return "Koneellinen poisto"
    elif data == 3:
        return "Koneellinen tulo/poisto"
    else:
        return "ERROR"

@register.filter
def LKVeriste_(data):
    if data == 1:
        return "40mm"
    elif data == 2:
        return "100mm"
    elif data == 3:
        return "Muu paksuus"
    else:
        return "ERROR"

@register.filter
def putkieriste_(data):
    if data == 0:
        return "Ei tietoa"
    if data == 1:
        return "0.5 D"
    elif data == 2:
        return "1.5 D"
    elif data == 3:
        return "Suojaputki"
    elif data == 4:
        return "Suojaputki + 0.5 D"
    elif data == 5:
        return "Suojaputki + 1.5 D"
    else:
        return "ERROR"

@register.filter
def pumppu_(data):
    if data == 0:
        return "Ei tietoa"
    if data == 1:
        return "MLP"
    elif data == 2:
        return "IVLP"
    elif data == 3:
        return "PILP"
    else:
        return "ERROR"

#ALAPOHJAN ENERGIAHUKKA VUODESSA
@register.filter
def alapohja(data):
    m_alapohja = data.pinta_ala
    q_alapohja = 0
    for kk in range(1,13):
        t_ulko = säätaulu[kk].maa_t
        q_alapohja +=  Uarvot[data.rakennusvuosi].U[1] * m_alapohja * (Kluokat[data.kayttotarkoitus].l_raja - t_ulko) * KkData[kk].tunnit
        #print("Ua:", Uarvot[data.rakennusvuosi].U[1], "Ala",m_alapohja,"lraja", (Kluokat[data.kayttotarkoitus].l_raja - t_ulko), "Q_:", Uarvot[data.rakennusvuosi].U[1] * m_alapohja * (Kluokat[data.kayttotarkoitus].l_raja -t_ulko) * KkData[kk].tunnit)
    if q_alapohja == 0:
        return ("ERROR: päivitä rakennustiedot!!")
    else:
        return (round(q_alapohja/1000,0))


# ULKOSEINIEN ENERGIAHUKKA VUODESSA
@register.filter
def ulkoseina(data):
    if data.seinä_ala == 0:
        m_ulkoseina = math.sqrt(data.pinta_ala) * 2.8 * data.kerrosmaara * 4 * 0.85
    else:
        m_ulkoseina = data.seinä_ala
    q_ulkoseina = 0
    for kk in range(1,13):
        t_ulko = säätaulu[kk].A[data.alue]
        q_ulkoseina += Uarvot[data.rakennusvuosi].U[0] * m_ulkoseina * (Kluokat[data.kayttotarkoitus].l_raja - t_ulko) * KkData[kk].tunnit * data.kerrosmaara
        #print("U:", Uarvot[data.rakennusvuosi].U[0], "Ala",m_ulkoseina,"lraja", (Kluokat[data.kayttotarkoitus].l_raja - t_ulko), "Tunnit",KkData[kk].tunnit )
        #print("ulkolanpö",t_ulko,"U_ulko", u_ulkoseinä, "m2_uko", m_ulkoseina ,"lraja", Kluokat[data.kayttotarkoitus].l_raja)
    if q_ulkoseina == 0:
        return ("ERROR: päivitä rakennustiedot!!")
    else:
        return (round(q_ulkoseina/1000,0))

# YLÄPOHJAN ENERGIAHUKKA VUODESSA
@register.filter
def yläpohja(data):
    if data.yläpohja_ala == 0:
        m_yläpohja = data.pinta_ala / data.kerrosmaara
    else:
        m_yläpohja = data.yläpohja_ala
    q_yläpohja = 0
    for kk in range (1,13):
        t_ulko = säätaulu[kk].A[data.alue]
        q_yläpohja += Uarvot[data.rakennusvuosi].U[4] * m_yläpohja * (Kluokat[data.kayttotarkoitus].l_raja -t_ulko) * KkData[kk].tunnit
        #print("U:", Uarvot[data.rakennusvuosi].U[4], "Ala",m_yläpohja,"lraja", (Kluokat[data.kayttotarkoitus].l_raja - t_ulko), "Q_:", Uarvot[data.rakennusvuosi].U[4] * m_yläpohja * (Kluokat[data.kayttotarkoitus].l_raja -t_ulko) * KkData[kk].tunnit)

    #print("tulko",t_ulko,"u_ylä", u_yläpohja, "m_ylä", m_yläpohja )
    if q_yläpohja == 0:
        return ("ERROR: päivitä rakennustiedot!!")
    else:
        return (round(q_yläpohja/1000,0))

# IKKUNOIDEN ENERGIAHUKKA VUODESSA
@register.filter
def ikkunat(data):
    if data.ikkuna_ala == 0:
        m_ikkunat = math.sqrt(data.pinta_ala) * 2.8 * data.kerrosmaara * 0.15  # 15% seinäpinta-alasta
    else:
        m_ikkunat = data.ikkuna_ala
    q_ikkunat = 0
    for kk in range(1,13):
        t_ulko = säätaulu[kk].A[data.alue]
        q_ikkunat += Uarvot[data.rakennusvuosi].U[5] * m_ikkunat * (Kluokat[data.kayttotarkoitus].l_raja - t_ulko) * KkData[kk].tunnit
        #print("U:", Uarvot[data.rakennusvuosi].U[5], "Ala",m_ikkunat,"lraja", (Kluokat[data.kayttotarkoitus].l_raja - t_ulko), "Q_:", Uarvot[data.rakennusvuosi].U[5] * m_ikkunat * (Kluokat[data.kayttotarkoitus].l_raja -t_ulko) * KkData[kk].tunnit)
    if q_ikkunat == 0:
        return ("ERROR: päivitä rakennustiedot!!")
    else:
        return (round(q_ikkunat/1000,0))


# OVIEN ENERGIAHUKKA VUODESSA
@register.filter
def ovet(data):
    if data.ovet_ala == 0:
        m_ovet = 5 * 0.8 * 2 * data.kerrosmaara
    else:
        m_ovet = data.ovet_ala
    q_ovet = 0
    for kk in range(1,13):
        t_ulko = säätaulu[kk].A[data.alue]
        q_ovet += Uarvot[data.rakennusvuosi].U[6] * m_ovet * (Kluokat[data.kayttotarkoitus].l_raja - t_ulko) * KkData[kk].tunnit
        #print("U:", Uarvot[data.rakennusvuosi].U[6], "Ala",m_ovet,"lraja", (Kluokat[data.kayttotarkoitus].l_raja - t_ulko), "Q_:", Uarvot[data.rakennusvuosi].U[6] * m_ovet * (Kluokat[data.kayttotarkoitus].l_raja -t_ulko) * KkData[kk].tunnit)
    if q_ovet == 0:
        return ("ERROR: päivitä rakennustiedot!!")
    else:
        return (round(q_ovet/1000,0))

# YHDISTETTY ENERGIAHUKKA VUODESSA
@register.filter
def kaikki(data):
    q_alapohja = 0
    q_ikkunat = 0
    q_ovi = 0
    q_yläpohja = 0
    q_ulkoseina = 0
    q_kylmasilta = 0
    for kk in range(1,13):
        t_ulko = säätaulu[kk].A[data.alue]
        q_alapohja  += Uarvot[data.rakennusvuosi].U[1] * data.pinta_ala  * (Kluokat[data.kayttotarkoitus].l_raja - säätaulu[kk].maa_t) * KkData[kk].tunnit
        q_ikkunat   += Uarvot[data.rakennusvuosi].U[5] * data.ikkuna_ala * (Kluokat[data.kayttotarkoitus].l_raja - t_ulko) * KkData[kk].tunnit
        q_ovi       += Uarvot[data.rakennusvuosi].U[6] * data.ovet_ala   * (Kluokat[data.kayttotarkoitus].l_raja - t_ulko) * KkData[kk].tunnit
        q_yläpohja  += Uarvot[data.rakennusvuosi].U[4] * data.pinta_ala  * (Kluokat[data.kayttotarkoitus].l_raja - t_ulko) * KkData[kk].tunnit
        q_ulkoseina += Uarvot[data.rakennusvuosi].U[0] * data.seinä_ala  * (Kluokat[data.kayttotarkoitus].l_raja - t_ulko) * KkData[kk].tunnit
        q_kylmasilta = (q_alapohja * 0.1) + (q_ikkunat * 0.1) + (q_ovi * 0.1) + (q_yläpohja * 0.1) + (q_ulkoseina * 0.1)
        #print("seinat: U-arvo:", Uarvot[data.rakennusvuosi].U[0], "pinta-ala:", data.seinä_ala, "Lämmitysraja:",Kluokat[data.kayttotarkoitus].l_raja, "Ulkolämpö", säätaulu[kk].A[data.alue], "Tunnit:", KkData[kk].tunnit )
        #print("ulkolämpö", t_ulko, "Q_ulkos", q_ulkoseina/1000,"Q_ylä", q_yläpohja/1000, "Q_apohja",q_alapohja/1000, "Q_ikkuna", q_ikkunat/1000, "Q_ovi", q_ovi/1000, "Kylmasilta", q_kylmasilta/1000 )
        #print("U_seinä", Uarvot[data.rakennusvuosi].U[0], "U_alap", Uarvot[data.rakennusvuosi].U[1],"U_yläp", Uarvot[data.rakennusvuosi].U[4],"U_ikkuna", Uarvot[data.rakennusvuosi].U[5],"U_ovi", Uarvot[data.rakennusvuosi].U[6])
    q_kaikki = q_alapohja + q_ikkunat + q_ovi + q_yläpohja + q_ulkoseina + q_kylmasilta
    if q_kaikki == 0:
        return ("ERROR: päivitä rakennustiedot!!")
    else:
        return (round(q_kaikki/1000,0))

# IV ENERGIAHUKKA VUODESSA
@register.filter
def q_iv(data):
    t_ulko = säätaulu[0].A[data.alue]
    q_iv = 1.2 * 1 * (0.5*data.pinta_ala)/1000 * (18 - t_ulko) * 8760

    if q_iv == 0:
        return ("ERROR: päivitä rakennustiedot!!")
    else:
        return (round(q_iv,0))

# LKV ENERGIAHUKKA VUODESSA
@register.filter
def q_lkv(data):
    t_ulko = säätaulu[0].A[data.alue]
    q_lkv = (1000 * 4.2 * (0.9*data.pinta_ala)*0.38 * (58 - 8) )/ 3600

    if q_lkv == 0:
        return ("ERROR: päivitä rakennustiedot!!")
    else:
        return (round(q_lkv,0))

# KOKONAIS ENERGIANKULUTS VUODESSA
@register.filter
def kulutus(data):
    t_ulko = säätaulu[0].A[data.alue]
    q_alapohja =  Uarvot[data.rakennusvuosi].U[1] * data.pinta_ala * (21 - 4) *8760
    q_ikkunat = Uarvot[data.rakennusvuosi].U[5] * data.ikkuna_ala * (21 -t_ulko) *8760
    q_ovi = Uarvot[data.rakennusvuosi].U[6] * data.ovet_ala * (21 -t_ulko) *8760
    q_yläpohja = Uarvot[data.rakennusvuosi].U[4] * data.pinta_ala * (21 -t_ulko) *8760
    q_ulkoseina = Uarvot[data.rakennusvuosi].U[0] * data.seinä_ala * (21 -t_ulko) *8760
    q_kaikki = q_alapohja + q_ikkunat + q_ovi + q_yläpohja + q_ulkoseina
    q_iv = 1.2 * 1 * (0.5*data.pinta_ala)/1000 * (18 - t_ulko) * 8760
    q_lkv = (1000 * 4.2 * (0.9*data.pinta_ala)*0.38 * (58 - 8) )/ 3600
    q_kulutus = (q_kaikki/1000) + q_iv + q_lkv

    if q_kulutus == 0:
        return ("ERROR: päivitä rakennustiedot!!")
    else:
        return (round(q_kulutus,0))

# PERFORMANSSI ILMAN LTO
@register.filter
def performanssi(data):
    try:
        t_ulko = säätaulu[0].A[data.alue]
        q_alapohja =  Uarvot[data.rakennusvuosi].U[1] * data.pinta_ala * (21 - 4) *8760
        q_ikkunat = Uarvot[data.rakennusvuosi].U[5] * data.ikkuna_ala * (21 -t_ulko) *8760
        q_ovi = Uarvot[data.rakennusvuosi].U[6] * data.ovet_ala * (21 -t_ulko) *8760
        q_yläpohja = Uarvot[data.rakennusvuosi].U[4] * data.pinta_ala * (21 -t_ulko) *8760
        q_ulkoseina = Uarvot[data.rakennusvuosi].U[0] * data.seinä_ala * (21 -t_ulko) *8760
        q_kaikki = q_alapohja + q_ikkunat + q_ovi + q_yläpohja + q_ulkoseina
        q_iv = 1.2 * 1 * (0.5*data.pinta_ala)/1000 * (18 - t_ulko) * 8760
        q_lkv = (1000 * 4.2 * (0.9*data.pinta_ala)*0.38 * (58 - 8) )/ 3600
        q_kulutus = (q_kaikki/1000) + q_iv + q_lkv
        lto_performanssi = q_kulutus / data.pinta_ala
    except:
        return "Error"
    if lto_performanssi == 0:
        return ("ERROR: päivitä rakennustiedot!!")
    else:
        return (round(lto_performanssi,0))

# KOKONAIS ENERGIANKULUTS VUODESSA LTO MUKANA
@register.filter
def lto_kulutus(data):
    try:
        t_ulko = säätaulu[0].A[data.alue]
        q_alapohja =  Uarvot[data.rakennusvuosi].U[1] * data.pinta_ala * (21 - 4) *8760
        q_ikkunat = Uarvot[data.rakennusvuosi].U[5] * data.ikkuna_ala * (21 -t_ulko) *8760
        q_ovi = Uarvot[data.rakennusvuosi].U[6] * data.ovet_ala * (21 -t_ulko) *8760
        q_yläpohja = Uarvot[data.rakennusvuosi].U[4] * data.pinta_ala * (21 -t_ulko) *8760
        q_ulkoseina = Uarvot[data.rakennusvuosi].U[0] * data.seinä_ala * (21 -t_ulko) *8760
        q_kaikki = q_alapohja + q_ikkunat + q_ovi + q_yläpohja + q_ulkoseina
        q_lkv = (1000 * 4.2 * (0.9*data.pinta_ala)*0.38 * (58 - 8) )/ 3600
        q_ivlto = 1.2 * 1 * (0.5*data.pinta_ala)/1000 * (18 - (t_ulko+0.75*(21-t_ulko))) * 8760
        q_lto_kulutus = (q_kaikki/1000) + q_ivlto + q_lkv
    except:
        return "Error"
    if q_lto_kulutus == 0:
        return ("ERROR: päivitä rakennustiedot!!")
    else:
        return (round(q_lto_kulutus,0))

# PERFORMANSSI LTON KANSSA
@register.filter
def performanssi2(data):
    try:
        t_ulko = säätaulu[0].A[data.alue]
        q_alapohja =  Uarvot[data.rakennusvuosi].U[1] * data.pinta_ala * (21 - 4) *8760
        q_ikkunat = Uarvot[data.rakennusvuosi].U[5] * data.ikkuna_ala * (21 -t_ulko) *8760
        q_ovi = Uarvot[data.rakennusvuosi].U[6] * data.ovet_ala * (21 -t_ulko) *8760
        q_yläpohja = Uarvot[data.rakennusvuosi].U[4] * data.pinta_ala * (21 -t_ulko) *8760
        q_ulkoseina = Uarvot[data.rakennusvuosi].U[0] * data.seinä_ala * (21 -t_ulko) *8760
        q_kaikki = q_alapohja + q_ikkunat + q_ovi + q_yläpohja + q_ulkoseina
        q_lkv = (1000 * 4.2 * (0.9*data.pinta_ala)*0.38 * (58 - 8) )/ 3600
        q_ivlto = 1.2 * 1 * (0.5*data.pinta_ala)/1000 * (18 - (t_ulko+0.75*(21-t_ulko))) * 8760
        q_lto_kulutus = (q_kaikki/1000) + q_ivlto + q_lkv
        lto_performanssi2 = q_lto_kulutus / data.pinta_ala
    except:
        return "Error"
    if lto_performanssi2 == 0:
        return ("ERROR: päivitä rakennustiedot!!")
    else:
        return (round(lto_performanssi2,0))

# Auringon tuottama säteilykuorma ikkunoiden läpi
@register.filter
def auringon_sateily(data):
    sateily_lapaisy = 0.5
    s_pohj = 0
    s_ita = 0
    s_etela = 0
    s_lansi = 0
    sateily = 0
    for kk in range(1,13):
        s_pohj += Solar[kk].az0 * Solar[kk].az0_lapi * data.ikkuna_ala/4 * sateily_lapaisy * Solar[kk].az0_varj 
        s_ita += Solar[kk].az90 * Solar[kk].az90_lapi * data.ikkuna_ala/4 * sateily_lapaisy * Solar[kk].az90_varj 
        s_etela += Solar[kk].az180 * Solar[kk].az180_lapi * data.ikkuna_ala/4 * sateily_lapaisy * Solar[kk].az180_varj 
        s_lansi += Solar[kk].az270 * Solar[kk].az270_lapi * data.ikkuna_ala/4 * sateily_lapaisy * Solar[kk].az270_varj 
        #print(kk, round(s_pohj,2), round(s_ita,2), round(s_etela,2), round(s_lansi,2),round(sateily,2))
    sateily = s_pohj + s_ita + s_lansi + s_etela
    return round(sateily,0)

@register.filter
def ihmislampo(data):
    kayttoaste = (Kluokat[data.kayttotarkoitus].pvm_h / 24) * (Kluokat[data.kayttotarkoitus].vko_p / 7)
    ihmisteho = (data.pinta_ala * Kluokat[data.kayttotarkoitus].ihmiset) / 1000
    l_kuorma = ihmisteho * kayttoaste * Kluokat[data.kayttotarkoitus].kuorma * KkData[13].tunnit
    #print("teho:",ihmisteho, "k_aste:",kayttoaste,"l_o:",Kluokat[data.kayttotarkoitus].kuorma,"tunnit:", KkData[13].tunnit )
    return round(l_kuorma,0)

@register.filter
def lampoenergia(data):
    try:
        lkv_energia = Kluokat[data.kayttotarkoitus].lkv * data.pinta_ala * data.kerrosmaara
        iv_energia = 0
        tila_lammitys = 0
        q_johtuminen = 0
        q_vuotoilma = 0
        q_tuloilma = 0
        q_aurinko = 0
        q_ihmiset = 0
        q_laitteet = 0
        IV_tuloilmavirta = Kluokat[data.kayttotarkoitus].virta * data.pinta_ala
        for kk in range(1,13):
            if data.lto:
                AB69 = Uarvot[data.rakennusvuosi].Lto_h
            else:
                AB69 = 0
            E3= KkData[kk].k_lampo[data.alue] + AB69 * (Kluokat[data.kayttotarkoitus].l_raja - KkData[kk].k_lampo[data.alue])
            #print(AB69, E3, KkData[x].k_lampo[data.alue] , Kluokat[data.kayttotarkoitus].l_raja)
            if E3 > Tsp- 0.5:
                G3 = Tsp - 0.5
            else:
                G3 = E3
            if KkData[kk].lto:
                H3 = G3
            else:
                H3 = KkData[kk].k_lampo[data.alue]
            if H3 < Tsp:
                J3 = Tsp
            else:
                J3 = H3 + 0.5
            if J3 >= Tsp:
                K3 = Tsp - 0.5 - H3
            else:
                K3 = J3 - 0.5 - H3
            if KkData[kk].lto : # LTO käytössä
                if data.lto:
                    #print("LTO on",(Kluokat[data.kayttotarkoitus].pvm_h/24) , (IV_tuloilmavirta) , K3 ,KkData[kk].k_lampo[data.alue], KkData[kk].tunnit, E3, G3, H3, K3, J3)
                    iv_energia += (Kluokat[data.kayttotarkoitus].pvm_h/24) * 1 * 1.2 * 1000 * (IV_tuloilmavirta/1000) * K3 * KkData[kk].tunnit / 1000
                else:
                    #print("LTO off",(Kluokat[data.kayttotarkoitus].pvm_h/24) , (IV_tuloilmavirta) , K3 ,KkData[kk].k_lampo[data.alue], KkData[kk].tunnit, E3, G3, H3,  K3, J3)
                    iv_energia += (Kluokat[data.kayttotarkoitus].pvm_h/24) * 1 * 1.2 * 1000 * (IV_tuloilmavirta/1000) * KkData[kk].k_lampo[data.alue] * KkData[kk].tunnit / 1000
            else:
                iv_energia += 0
            vaippa = data.seinä_ala + data.pinta_ala + data.pinta_ala + data.ikkuna_ala + data.ovet_ala
            if data.kerrosmaara == 1:
                vuotokerroin = 35 
            else:
                if data.kerrosmaara == 2:
                    vuotokerroin = 24
                else: 
                    if data.kerrosmaara in [3,4]:
                        vuotokerroin = 20
                    else:
                        vuotokerroin = 15
            vuotoluku = Uarvot[data.rakennusvuosi].vuoto / vaippa * (data.pinta_ala * 2.8 * data.kerrosmaara)
            q_vuoto =  vuotoluku * vaippa / (3600 * vuotokerroin)
            t_ulko = säätaulu[kk].A[data.alue]
            q_johtuminen += Uarvot[data.rakennusvuosi].U[1] * data.pinta_ala  * (Kluokat[data.kayttotarkoitus].l_raja - säätaulu[kk].maa_t) * KkData[kk].tunnit
            q_johtuminen += Uarvot[data.rakennusvuosi].U[5] * data.ikkuna_ala * (Kluokat[data.kayttotarkoitus].l_raja - t_ulko) * KkData[kk].tunnit
            q_johtuminen += Uarvot[data.rakennusvuosi].U[6] * data.ovet_ala   * (Kluokat[data.kayttotarkoitus].l_raja - t_ulko) * KkData[kk].tunnit
            q_johtuminen += Uarvot[data.rakennusvuosi].U[4] * data.pinta_ala  * (Kluokat[data.kayttotarkoitus].l_raja - t_ulko) * KkData[kk].tunnit
            q_johtuminen += Uarvot[data.rakennusvuosi].U[0] * data.seinä_ala  * (Kluokat[data.kayttotarkoitus].l_raja - t_ulko) * KkData[kk].tunnit
            q_vuotoilma += (1.2 * 1000 * q_vuoto  *  (Kluokat[data.kayttotarkoitus].l_raja - t_ulko) * KkData[kk].tunnit) /1000
            käyttäaikasuhde = (Kluokat[data.kayttotarkoitus].pvm_h / 24) * (Kluokat[data.kayttotarkoitus].vko_p / 7)
            q_tuloilma = ((käyttäaikasuhde * 1.2 * 1000 * (Kluokat[data.kayttotarkoitus].u_ilma * data.pinta_ala)/1000) * (Kluokat[data.kayttotarkoitus].l_raja - Tsp) * KkData[kk].tunnit) / 1000
            q_ihmiset += (data.pinta_ala * Kluokat[data.kayttotarkoitus].ihmiset)
            sateily_lapaisy = 0.5
            q_aurinko += Solar[kk].az0 * Solar[kk].az0_lapi * data.ikkuna_ala/4 * sateily_lapaisy * Solar[kk].az0_varj #pohjoinen
            q_aurinko += Solar[kk].az90 * Solar[kk].az90_lapi * data.ikkuna_ala/4 * sateily_lapaisy * Solar[kk].az90_varj # itä
            q_aurinko += Solar[kk].az180 * Solar[kk].az180_lapi * data.ikkuna_ala/4 * sateily_lapaisy * Solar[kk].az180_varj # etelä
            q_aurinko += Solar[kk].az270 * Solar[kk].az270_lapi * data.ikkuna_ala/4 * sateily_lapaisy * Solar[kk].az270_varj #länsi
            #print("q_johtuminen",q_johtuminen, "q_vuotoilma", q_vuotoilma,"q_tuloilma",q_tuloilma,"aurinko",q_aurinko,"ihmiset",q_ihmiset, "lkv", lkv_energia)
            q_laitteet += (Kluokat[data.kayttotarkoitus].laitteet * data.pinta_ala) / 1000 * käyttäaikasuhde * Kluokat[data.kayttotarkoitus].kuorma * KkData[kk].tunnit #kuluttajalaitteet
            if data.kayttotarkoitus < 3:
                q_laitteet += (Kluokat[data.kayttotarkoitus].valaistus * data.pinta_ala) * 1000 * käyttäaikasuhde * 0.1 * KkData[kk].tunnit #valaistus
            else:
                q_laitteet += (Kluokat[data.kayttotarkoitus].valaistus * data.pinta_ala) * 1000 * käyttäaikasuhde * Kluokat[data.kayttotarkoitus].kuorma * KkData[kk].tunnit #valaistus
        q_johtuminen = (q_johtuminen * 1.1) # kylmäsillat 10%
        q_lampokuorma = q_aurinko + q_ihmiset + lkv_energia
        tila_lammitys = q_johtuminen + q_vuotoilma + q_tuloilma - q_lampokuorma
        #print("lkv:",lkv_energia , " iv:",iv_energia , " laitteet", q_laitteet, " vuoto:",q_vuotoilma," vaippa:", vaippa)
    except:
        return "Error"
    return round(lkv_energia + iv_energia + tila_lammitys,0)
