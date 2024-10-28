import math
from django import template
register = template.Library()

#Staattiset taulukkoarvot
exec(compile(source=open('/home/ari1/Eco-App/myenv/mete_project/mete_project/Taulukot.py').read(), filename='Taulukot.py', mode='exec'))

Alku_D_81 = 0

def Fun_vaippa(data):
    EC56 = data.seinä_ala # Ulkoseinä pinta-ala
    EC57 = data.yläpohja_ala # Yläpohja pinta-ala
    EC58 = data.pinta_ala # Pinta_ala
    EC59 = data.ikkuna_ala # Ikkuna pinta_ala
    EC60 = data.ovet_ala # Ovet pinta-ala
    vaippa = EC56 + EC57 + EC58 + EC59 + EC60 # vaippa
    return vaippa

def Fun_Tilojen_nettolammitys(data): #EE95
    tila_lammitys = 0
    H_A = 24 * 365 # tuntia vuodessa
    AC93 = Uarvot[data.rakennusvuosi].vuoto
    TC36 = Kluokat[data.kayttotarkoitus].ihmiset * data.pinta_ala * data.kerrosmaara
    EC72 = data.pv_vko/7 # Viikoittainen käytniaikasuhde
    EC71 = data.h_pv/24 # Vuorokautinen kyyntiaikasuhde
    EC78 = Kluokat[data.kayttotarkoitus].kuorma # Ihmisten läsnäoloaste
    EC9 = data.pinta_ala
    EC67 = Kluokat[data.kayttotarkoitus].ominais_C
    EC63 = data.sisalampo
    EC20 = data.varaavatulisija
    EC21 = data.ilmalampopumppu
    EC39 = data.h_pv/24
    EC40 = data.pv_vko/7
    EC32 = Kluokat[data.kayttotarkoitus].virta * data.pinta_ala
    EC37 = Tsp
    EE95 = 0
    for kk in range(1,13):
        EF3 = säätaulu[kk].A[data.alue]
        AC94 = KkData[kk].tunnit # Kuukauden tunnit
        TO20 = (EC39 * EC40 * 1.2 * 1000 * ( EC32 / 1000 ) * ( EC63 - EC37 ) * AC94 ) / 1000
        EC60 = data.ovet_ala # Ovet pinta-ala
        ED60 = Uarvot[data.rakennusvuosi].U[6] # Ovet Uarvo
        TI20 = (EC60 * ED60 * (EC63 - EF3) * AC94)/1000  # Oviem vuoto
        EC59 = data.ikkuna_ala # Ikkuna pinta_ala
        ED59 = Uarvot[data.rakennusvuosi].U[5] # Ikkuna Uarvo
        TH20 = (EC59 * ED59 * (EC63 - EF3) * AC94)/1000 # Ikkunoden vuoto
        AC206 = säätaulu[kk].maa_t # Alapohjan maalämpötila
        EC58 = data.pinta_ala # Pinta_ala
        EE58 = EC58 / 4 # Pinta_ala / 4 
        ED58 = Uarvot[data.rakennusvuosi].U[1] # Ala-pohja U-arvo
        TG20 = ( EE58 * ED58 * (EC63 - AC206 ) * AC94)/1000 # Alapohjan vuoto
        EC57 = data.yläpohja_ala # Yläpohja pinta-ala
        ED57 = Uarvot[data.rakennusvuosi].U[4] # Yläpohja U-arvo
        TF20 = (EC57 * ED57 * (EC63 - EF3) * AC94)/1000 # Yläpohjan vuoto
        EC56 = data.seinä_ala # Ulkoseinä pinta-ala
        ED56 = Uarvot[data.rakennusvuosi].U[0] # Ulkoseinä U-arvo
        TE20 = (ED56 * EC56 * (EC63 - EF3) * AC94)/1000 # Ulkoseinät vuoto
        TJ20 = (TI20 + TH20 + TG20 + TF20 + TE20) * 0.1 # Kylmäsillat
        EC65 = Uarvot[data.rakennusvuosi].vuoto # Rakennuksen ilmanvaihtoluku
        EC10 = data.pinta_ala * data.kerrosmaara
        EC62 = EC10 * huonekorkeus # tilavuus m3
        EC61 = Fun_vaippa(data)
        if (data.rakennusvuosi < 10):
            EF65 = EC65 / EC61 * EC62
        else:
            EF65 = EC65 
        if (data.kerrosmaara == 1): # 1 krs
            EC66 = 35
        elif (data.kerrosmaara == 2): # 2 krs
            EC66 = 24
        elif (data.kerrosmaara == 3): # 3 krs
            EC66 = 20
        elif (data.kerrosmaara == 4): # 4 krs
            EC66 = 20
        else:   # muut kerrokset
            EC66 = 15
        TM19 = (EF65 * EC61)/(3600 * EC66)
        TL20 = (1.2 * 1000 * TM19 * (EC63 - EF3) * AC94)/1000 # Qvuoto
        TQ20 = TO20 + TJ20 + TI20 + TH20 + TG20 + TF20 + TE20 + TL20
        TC38 = (TC36 / 1000) * EC72 * EC71 * EC78 * AC94 #vakio-arvot alussa
        EC73 = Kluokat[data.kayttotarkoitus].laitteet # kuluttajalaite teho
        EC75 = Kluokat[data.kayttotarkoitus].valaistus # valaistuksen ominaisteho
        EC83 = EC73 * EC9
        EC84 = EC75 * EC9
        if (EC71 * EC72 == 1):
            EC79 = 1 # 100%; 
        else :
            EC79 = EC71 * EC72
        EC74 = Kluokat[data.kayttotarkoitus].kuorma #sisäinen lämpökuorma /m2
        EC76 = Kluokat[data.kayttotarkoitus].valaistus #Valaistus käyttöaste
        EE83 = EC83 / 1000 * EC79 * EC74 * H_A # Kuluttajaittet vuodessa
        EE84 = EC84 / 1000 * EC79 * EC76 * H_A # Valasitus vuodessa
        if data.lkv_tila > 0:
            if data.lkvputken_eristys == 1:
                EC87 = LKV_table[data.lkv_tila].havio40
            else: 
                EC87 = LKV_table[data.lkv_tila].havio100
        else:
            EC87 = 0 # OK
        EC47 = 1
        if data.lkv_tila > 1:
            if (data.lkvputken_eristys == 1): # "40mm" 
                EC47 = LKV_table[data.lkv_tila].havio40
            elif  (data.lkvputken_eristys == 2): # "1000mm"
                EC47 = LKV_table[data.lkv_tila].havio100
            else:
                EC47 = 0
            EE88 = EC47
        else:
            EE88 = 0 # Qlkv varasto
        EE87 = EC87 / 1000 * EC9 * H_A # Qlkv siirto
        TD38 = EE83 / H_A * AC93
        TE38 = EE84 / H_A * AC93
        TF38 = EE88 / H_A * AC93 * 0.5
        TG38 = EE87 / H_A * AC93 * 0.5
        AD223 = Solar[kk].az0 # az0 el45
        AE223 = Solar[kk].az90 # az90 el45
        AF223 = Solar[kk].az180 # az180 el45
        AG223 = Solar[kk].az270 # ad270 el45
        AC263 = Solar[kk].az0_lapi # läpäisy pohjinen
        AE263 = Solar[kk].az90_lapi # Läpäisy itä
        AG263 = Solar[kk].az180_lapi # Läpäisy etelä
        AI263 = Solar[kk].az270_lapi # läpäisy länsi
        EE59 = data.ikkuna_ala /4 # pohjoinen ikkunat m2
        EF59 = data.ikkuna_ala /4 # itä ikkuna m2
        EG59 = data.ikkuna_ala /4 # etelä ikkuna m2
        EH59 = data.ikkuna_ala /4 # länsi ikkuna m2
        AC244 = Solar[kk].az0_varj # varjostus pohjoinen 
        AE244 = Solar[kk].az90_varj # varjostus itä
        AG244 = Solar[kk].az180_varj # varjostus etelä
        AI244 = Solar[kk].az270_varj # varjostus länsi
        EC55 = AD223 * AC263 * EE59 * 0.5 * AC244 # aurinkokuorma pohjoinen / kk
        ED55 = AE223 * AE263 * EF59 * 0.5 * AE244 # aurinkokuorma itä / kk
        EE55 = AF223 * AG263 * EG59 * 0.5 * AG244 # aurinkokuorma etelä / kk
        EF55 = AG223 * AI263 * EH59 * 0.5 * AI244 # aurinkokuorma länsi / kk
        AurinkoLampokuorma = EC55 + ED55 + EE55 + EF55
        TH38 = AurinkoLampokuorma
        KuormaLampo = (TC38 + TD38 + TE38 + TF38 + TG38 + TH38)
        TO38 = KuormaLampo
        TJ38 = (TQ20 * 1000) / ((EC63-EF3)*AC93)
        TL38 = EC9 * EC67
        TN38 = TL38 / TJ38
        TP38 = 1 + (TN38 / 15)
        TQ38 = (1-pow(TO38,TP38)) / (1- pow(TO38,(TP38 + 1)))
        TR38 = TQ38 * KuormaLampo 
        TR32 = TQ20 - TR38
        EE95 += TR32
    EG20 = data.tulisija_lkm * 3000 #Oletus_TulisiJAN_ENERGIA
    EG21 = Uarvot[data.rakennusvuosi].ilp_max * 1 # Taulukko_ILP_energia * ILP_kpl
    if EC20 == True:
        EE95 = TR32 - EG20
    elif EC21 == True:
        EE95 = TR32 - EG21
    elif EC20 == True and EC21 == True:
        EE95 = TR32 - EG20 - EG21
    else:
        EE95 = TR32
    tila_lammitys = EE95 
    return round(tila_lammitys,2)

def Fun_TR32(data):
    H_A = 24 * 365 # tuntia vuodessa
    AC93 = Uarvot[data.rakennusvuosi].vuoto
    TC36 = Kluokat[data.kayttotarkoitus].ihmiset * data.pinta_ala * data.kerrosmaara
    EC72 = data.pv_vko/7 # Viikoittainen käytniaikasuhde
    EC71 = data.h_pv/24 # Vuorokautinen kyyntiaikasuhde
    EC78 = Kluokat[data.kayttotarkoitus].kuorma # Ihmisten läsnäoloaste
    EC9 = data.pinta_ala
    EC67 = Kluokat[data.kayttotarkoitus].ominais_C
    EC63 = data.sisalampo
    EC39 = data.h_pv/24
    EC40 = data.pv_vko/7
    EC32 = Kluokat[data.kayttotarkoitus].virta * data.pinta_ala
    EC37 = Tsp
    TR32 = 0
    EE95 = 0
    for kk in range(1,13):
        EF3 = säätaulu[kk].A[data.alue]
        AC94 = KkData[kk].tunnit # Kuukauden tunnit
        TO20 = (EC39 * EC40 * 1.2 * 1000 * ( EC32 / 1000 ) * ( EC63 - EC37 ) * AC94 ) / 1000
        EC60 = data.ovet_ala # Ovet pinta-ala
        ED60 = Uarvot[data.rakennusvuosi].U[6] # Ovet Uarvo
        TI20 = (EC60 * ED60 * (EC63 - EF3) * AC94)/1000  # Oviem vuoto
        EC59 = data.ikkuna_ala # Ikkuna pinta_ala
        ED59 = Uarvot[data.rakennusvuosi].U[5] # Ikkuna Uarvo
        TH20 = (EC59 * ED59 * (EC63 - EF3) * AC94)/1000 # Ikkunoden vuoto
        AC206 = säätaulu[kk].maa_t # Alapohjan maalämpötila
        EC58 = data.pinta_ala # Pinta_ala
        EE58 = EC58 / 4 # Pinta_ala / 4 
        ED58 = Uarvot[data.rakennusvuosi].U[1] # Ala-pohja U-arvo
        TG20 = ( EE58 * ED58 * (EC63 - AC206 ) * AC94)/1000 # Alapohjan vuoto
        EC57 = data.yläpohja_ala # Yläpohja pinta-ala
        ED57 = Uarvot[data.rakennusvuosi].U[4] # Yläpohja U-arvo
        TF20 = (EC57 * ED57 * (EC63 - EF3) * AC94)/1000 # Yläpohjan vuoto
        EC56 = data.seinä_ala # Ulkoseinä pinta-ala
        ED56 = Uarvot[data.rakennusvuosi].U[0] # Ulkoseinä U-arvo
        TE20 = (ED56 * EC56 * (EC63 - EF3) * AC94)/1000 # Ulkoseinät vuoto
        TJ20 = (TI20 + TH20 + TG20 + TF20 + TE20) * 0.1 # Kylmäsillat
        EC65 = Uarvot[data.rakennusvuosi].vuoto # Rakennuksen ilmanvaihtoluku
        EC10 = data.pinta_ala * data.kerrosmaara
        EC62 = EC10 * huonekorkeus # tilavuus m3
        EC61 = Fun_vaippa(data)
        if (data.rakennusvuosi < 10):
            EF65 = EC65 / EC61 * EC62
        else:
            EF65 = EC65 
        EC61 = EC56 + EC57 + EC58 + EC59 + EC60 # vaippa
        if (data.kerrosmaara == 1): # 1 krs
            EC66 = 35
        elif (data.kerrosmaara == 2): # 2 krs
            EC66 = 24
        elif (data.kerrosmaara == 3): # 3 krs
            EC66 = 20
        elif (data.kerrosmaara == 4): # 4 krs
            EC66 = 20
        else:   # muut kerrokset
            EC66 = 15
        TM19 = (EF65 * EC61)/(3600 * EC66)
        TL20 = (1.2 * 1000 * TM19 * (EC63 - EF3) * AC94)/1000 # Qvuoto
        TQ20 = TO20 + TJ20 + TI20 + TH20 + TG20 + TF20 + TE20 + TL20
        TC38 = (TC36 / 1000) * EC72 * EC71 * EC78 * AC94 #vakio-arvot alussa
        EC73 = Kluokat[data.kayttotarkoitus].laitteet # kuluttajalaite teho
        EC75 = Kluokat[data.kayttotarkoitus].valaistus # valaistuksen ominaisteho
        EC83 = EC73 * EC9
        EC84 = EC75 * EC9
        if (EC71 * EC72 == 1):
            EC79 = 1 # 100%; 
        else :
            EC79 = EC71 * EC72
        EC74 = Kluokat[data.kayttotarkoitus].kuorma #sisäinen lämpökuorma /m2
        EC76 = Kluokat[data.kayttotarkoitus].valaistus #Valaistus käyttöaste
        EE83 = EC83 / 1000 * EC79 * EC74 * H_A # Kuluttajaittet vuodessa
        EE84 = EC84 / 1000 * EC79 * EC76 * H_A # Valasitus vuodessa
        if data.lkv_tila > 0:
            if data.lkvputken_eristys == 1:
                EC87 = LKV_table[data.lkv_tila].havio40
            else: 
                EC87 = LKV_table[data.lkv_tila].havio100
        else:
            EC87 = 0 # OK
        EC47 = 1
        if data.lkv_tila > 1:
            if (data.lkvputken_eristys == 1): # "40mm" 
                EC47 = LKV_table[data.lkv_tila].havio40
            elif  (data.lkvputken_eristys == 2): # "1000mm"
                EC47 = LKV_table[data.lkv_tila].havio100
            else:
                EC47 = 0
            EE88 = EC47
        else:
            EE88 = 0 # Qlkv varasto
        EE87 = EC87 / 1000 * EC9 * H_A # Qlkv siirto
        TD38 = EE83 / H_A * AC93
        TE38 = EE84 / H_A * AC93
        TF38 = EE88 / H_A * AC93 * 0.5
        TG38 = EE87 / H_A * AC93 * 0.5
        AD223 = Solar[kk].az0 # az0 el45
        AE223 = Solar[kk].az90 # az90 el45
        AF223 = Solar[kk].az180 # az180 el45
        AG223 = Solar[kk].az270 # ad270 el45
        AC263 = Solar[kk].az0_lapi # läpäisy pohjinen
        AE263 = Solar[kk].az90_lapi # Läpäisy itä
        AG263 = Solar[kk].az180_lapi # Läpäisy etelä
        AI263 = Solar[kk].az270_lapi # läpäisy länsi
        EE59 = data.ikkuna_ala /4 # pohjoinen ikkunat m2
        EF59 = data.ikkuna_ala /4 # itä ikkuna m2
        EG59 = data.ikkuna_ala /4 # etelä ikkuna m2
        EH59 = data.ikkuna_ala /4 # länsi ikkuna m2
        AC244 = Solar[kk].az0_varj # varjostus pohjoinen 
        AE244 = Solar[kk].az90_varj # varjostus itä
        AG244 = Solar[kk].az180_varj # varjostus etelä
        AI244 = Solar[kk].az270_varj # varjostus länsi
        EC55 = AD223 * AC263 * EE59 * 0.5 * AC244 # aurinkokuorma pohjoinen / kk
        ED55 = AE223 * AE263 * EF59 * 0.5 * AE244 # aurinkokuorma itä / kk
        EE55 = AF223 * AG263 * EG59 * 0.5 * AG244 # aurinkokuorma etelä / kk
        EF55 = AG223 * AI263 * EH59 * 0.5 * AI244 # aurinkokuorma länsi / kk
        AurinkoLampokuorma = EC55 + ED55 + EE55 + EF55
        TH38 = AurinkoLampokuorma
        KuormaLampo = (TC38 + TD38 + TE38 + TF38 + TG38 + TH38)
        TO38 = KuormaLampo
        TJ38 = (TQ20 * 1000) / ((EC63-EF3)*AC93)
        TL38 = EC9 * EC67
        TN38 = TL38 / TJ38
        TP38 = 1 + (TN38 / 15)
        TQ38 = (1-pow(TO38,TP38)) / (1- pow(TO38,(TP38 + 1)))
        TR38 = TQ38 * KuormaLampo 
        TR32 = TQ20 - TR38
        EE95 += TR32
    Arvo_TR32 = TR32
    return Arvo_TR32

def Fun_TC78(data):
    EC23 = Lammitys[data.lkv_lammitys].sahko #=VLOOKUP(C14;Aloitustaulukot!A113:H125;5;FALSE)
    EE95 = Fun_Tilojen_nettolammitys(data)
    EG95 = EE95 / EC23
    EC9 = data.pinta_ala
    EC49 = Kluokat[data.kayttotarkoitus].lkv_eriste
    EC44 = Kluokat[data.kayttotarkoitus].lkv
    if (data.kayttotarkoitus == 1) & (EC44 * EC9 > 4200):
        EC45 = 4200
    else:
        EC45 = EC44 * EC9
    if (data.kayttotarkoitus == 1) and (EC44 * EC9) > EC45:
        EE86 = EC45
    else:
        EE86 = EC44 * EC9
    EG86 = EE86 / EC49
    TC73 = EG95 / EG86
    if(TC73 > 0.5):
        TC74 = 0.92 # (VLOOKUP(TC73;AC365:TD368;2;TRUE))
    else:
        TC74 = 0.5
    TC75 = 2.5 # AC320
    TC76 = 2.3 # AC322
    Arvo_TC78 = TC74 * ((EG95 / TC75)+((1 / TC76))+(1-TC74)*(EG95 + EG86))
    return Arvo_TC78

@register.filter
def Tilat_osto(data):
    TC78 = Fun_TC78(data)
    if(data.lkv_lammitys == 7): # "Maalämpö, ym.")
        EE114 = TC78
    else: 
        TR32 = Fun_TR32(data)
        EE20 = data.tulisija_lkm
        EG20 = 3000 * EE20
        EE21 = data.lampopumppu_kpl
        EG21 = Uarvot[data.rakennusvuosi].ilp_max * EE21
        if(data.varaavatulisija) and (data.ilmalampopumppu): #varaava tulisija and ilmalämpöpumppu
            EE95 = TR32 - EG20 - EG21
        elif(data.ilmalampopumppu): #ilmalämpöpumpppu
            EE95 = TR32 - EG21
        elif(data.varaavatulisija): # varaava tulisija
            EE95 = TR32 - EG20
        else:
            EE95 = TR32
        EC23 = Lammitys[data.lkv_lammitys].sahko
        EC98 = EE95 / EC23
        if (data.kayttotarkoitus == 1):
            EC25 = Elahde[data.lkv_lammitys].Vuosihyoty1 #2-sarake
        else:
            EC25 = Elahde[data.lkv_lammitys].Vuosihyoty2 # 4-sarake
        EE114 = EC98 / EC25
    return round(EE114,1)

@register.filter
def Aurinkosateily(kk, data):
    #Lampokuormat_F53
    F53a =Solar[kk].az0*Solar[kk].az0_lapi*(data.ikkuna_ala/4)*0.5*Solar[kk].az0_varj
    F53b =Solar[kk].az90*Solar[kk].az90_lapi*(data.ikkuna_ala/4)*0.5*Solar[kk].az90_varj
    F53c =Solar[kk].az180*Solar[kk].az180_lapi*(data.ikkuna_ala/4)*0.5*Solar[kk].az180_varj
    F53d =Solar[kk].az270*Solar[kk].az270_lapi*(data.ikkuna_ala/4)*0.5*Solar[kk].az270_varj
    F53 = F53a + F53b + F53c + F53d # = "aurinkolampokuorma"
    #print("Aurinkosateily",round(F53,2))
    return F53

@register.filter
def IV_sahko(data):
    iv_sahko_energia = 0
    if (data.iv_tapa == 1): #SFP
        EC34 = Uarvot[data.rakennusvuosi].iv_paino
    elif (data.iv_tapa == 2):
        EC34 = Uarvot[data.rakennusvuosi].iv_poisto
    else:
        EC34 = Uarvot[data.rakennusvuosi].iv_tulopoisto

    EC31 = Kluokat[data.kayttotarkoitus].virta * data.pinta_ala # poistoilmavirta
    EC39 = data.h_pv / 24 # Käyntiaikasuhde vrk
    iv_sahko_energia = EC34 * (EC31/1000) * EC39 * 8760
    return round(iv_sahko_energia,1)

def get_AlkuD81(kk,data):
    if(((Kluokat[data.kayttotarkoitus].pvm_h / 24) * (Kluokat[data.kayttotarkoitus].vko_p / 7)) == 1):
        AlkuD81 = 1 # 100%
    else: 
        AlkuD81 = ((Kluokat[data.kayttotarkoitus].pvm_h / 24) * (Kluokat[data.kayttotarkoitus].vko_p / 7)) 
    return AlkuD81

@register.filter
def Ihmislammitys(kk, data):
#    global Alku_D_81
    # Lampokuormat_C4
#    Alku_D_81 = get_AlkuD81(kk,data)

    Alku_B_88 = Kluokat[data.kayttotarkoitus].kuorma
    _D_2 = Kluokat[data.kayttotarkoitus].ihmiset * data.pinta_ala 
    C4 = (_D_2/1000) * get_AlkuD81(kk,data) * Alku_B_88 * KkData[kk].tunnit
    #print("Ihmislammitys", round(C4,2))
    return C4

@register.filter
def LKV_osto(data): # TODO
    EC9 = data.pinta_ala
    EC49 = Kluokat[data.kayttotarkoitus].lkv_eriste
    EC44 = Kluokat[data.kayttotarkoitus].lkv
    if (data.kayttotarkoitus == 1) & (EC44 * EC9 > 4200):
        EC45 = 4200
    else:
        EC45 = EC44 * EC9
    if (data.kayttotarkoitus == 1) and (EC44 * EC9) > EC45:
        EE86 = EC45
    else:
        EE86 = EC44 * EC9
    EG86 = EE86 / EC49
    EE95 = Fun_Tilojen_nettolammitys(data)
    EC23 = Lammitys[data.lkv_lammitys].sahko #=VLOOKUP(C14;Aloitustaulukot!A113:H125;5;FALSE)
    EG95 = EE95 / EC23
    TC73 = EG95 / EG86
    if(TC73 > 0.5):
        TC74 = 0.92 # (VLOOKUP(TC73;AC365:TD368;2;TRUE))
    else:
        TC74 = 0.5
    TC75 = 2.5 # AC320
    TC76 = 2.3 # AC322
    EC51 = Kluokat[data.kayttotarkoitus].lkv_putki_ominais
    EC49 = Kluokat[data.kayttotarkoitus].lkv_eriste
    EC74 = Kluokat[data.kayttotarkoitus].kuorma # sisäinen lämpökuorma/m2
    EC87 = LKV_table[1].ominaisarvo[data.lkv_kiertoeriste] * EC51 * EC49
    EC9 = data.pinta_ala
    EE87 = EC87 / 1000 * EC9 * 8760
    if (data.lkv_tila > 0):
        if (data.lkvputken_eristys == 1): # "40mm" 
            EC47 = LKV_table[data.lkv_tila].havio40
        elif  (data.lkvputken_eristys == 2): # "1000mm"
            EC47 = LKV_table[data.lkv_tila].havio100
        else:
            EC47 = 0
        EE88 = EC47
    else:
        EE88 = 0
    TC79 = EC74 * ((1/TC75)+((EG86 / TC76 ))+(1- TC74 ) * ( EG95 + EG86))
    # vika kodissa ((0/TC75)+
    if(data.lkv_lammitys == 7): # data.lkv_lammitys = 7
        EC118 = TC79
    else:
        EC118 = EG86 + EE87 + EE88
    if(data.lkv_kierto): # LKV kierto
        EF103 = 200 * 0.0005 * 1000
        EC119 = EF103 * 24 * (365 / 1000) # EC104
    else:
        EC119 = 0
    LKV_tulos = EC118 + EC119
    return round(LKV_tulos,1)

@register.filter
def LKV_energia(data):
    EC44 = Kluokat[data.kayttotarkoitus].lkv
    EC9 = data.pinta_ala
    if data.lkv_kiertoeriste == 0:
        EC87 = 40
    elif data.lkv_kiertoeriste == 1:
        EC87 = 10
    elif data.lkv_kiertoeriste == 2:
        EC87 = 6
    elif data.lkv_kiertoeriste == 3:
        EC87 = 15
    elif data.lkv_kiertoeriste == 4:
        EC87 = 8
    elif data.lkv_kiertoeriste == 5:
        EC87 = 5
    else:
        EC87 = 0

    if (data.kayttotarkoitus == 1) & (EC44*EC9 > 4200):
        EC45 = 4200
    else:
        EC45 = EC44 * EC9
    if (data.kayttotarkoitus == 1) and (EC44 * EC9) > EC45:
        EE86 = EC45
    else:
        EE86 = EC44 * EC9
    EE87 =EC87 / 1000 * EC9 * 8760
    if data.lkvputken_eristys == 1:
        EC47 = LKV_h[data.lkv_tila].m40
    elif data.lkvputken_eristys == 2:
        EC47 = LKV_h[data.lkv_tila].m100
    else:
        EC47 = 0
    if data.lkv_tila > 1:
        EE88 = EC47
    else:
        EE88 = 0 # Qlkv varasto
    Tulos = EE86 + EE87 + EE88
    return round(Tulos,2)

@register.filter
def LKV_siirtoenergia(data):
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
def IV_energia(data):
    Qiv = 0
    EC39 = data.h_pv / 24
    EC40 = data.pv_vko / 7
    EC31 = Kluokat[data.kayttotarkoitus].u_ilma * data.pinta_ala
    EC30 = Uarvot[data.rakennusvuosi].Lto_h
    EC63 = data.sisalampo
    EC38 = deltaT
    EC37 = Tsp
    # FOR kk TÄSTÄ ETEENPÄIN
    for kk in range(1,13):
        AC94 = KkData[kk].tunnit
        EF3 = säätaulu[kk].A[data.alue]
        TC5 = EF3 + EC30 * (EC63 - EF3)
        if TC5 >= EC37 - EC38:
            TE5 = EC37 - EC38
        else:
            TE5 = TC5
        if  KkData[kk].lto:
            TF5 = TE5
        else:
            TF5 = EF3
        TG5 = TF5 + 0.5
        if TG5 > EC37:
            TH5 = TG5
        else:
            TH5 = EC37
        if KkData[kk].lto:
            TC20 = EC39 * EC40 * 1.2 * (EC31/1000) * (TH5 - EC38 - TF5) * AC94
#            print("EC39:",EC39 , "EC40:", round(EC40,2) ,"TH5:",TH5, "EC31:", EC31 , "EC38:", EC38 ,"TC5:", round(TC5,2))
        else:
            TC20 = 0
        Qiv += TC20
    return round(Qiv,2)

@register.filter
def Tila_lammitys2(data):
    tila2_lammitys = 0
#    H_A = 24 * 365 # tuntia vuodessa
#    TC36 = Kluokat[data.kayttotarkoitus].ihmiset * data.pinta_ala
#    EC72 = data.pv_vko/7 # Viikoittainen käytniaikasuhde
#    EC71 = data.h_pv/24 # Vuorokautinen kyyntiaikasuhde
#    EC78 = Kluokat[data.kayttotarkoitus].kuorma # Ihmisten läsnäoloaste
#    EC9 = data.pinta_ala
#    EC67 = Kluokat[data.kayttotarkoitus].ominais_C
    EC63 = data.sisalampo
#    EC20 = data.varaavatulisija
#    EC21 = data.ilmalampopumppu
    EC39 = data.h_pv/24
    EC40 = data.pv_vko/7
    EC32 = Kluokat[data.kayttotarkoitus].virta * data.pinta_ala
    EC37 = Tsp
#    EE95 = 0
    for kk in range(1,13):
        AC94 = KkData[kk].tunnit # Kuukauden tunnit
        EF3 = säätaulu[kk].A[data.alue]
        TO20 = (EC39 * EC40 * 1.2 * 1000 * ( EC32 / 1000 ) * ( EC63 - EC37 ) * AC94 ) / 1000
        EC60 = data.ovet_ala # Ovet pinta-ala
        ED60 = Uarvot[data.rakennusvuosi].U[6] # Ovet Uarvo
        TI20 = (EC60 * ED60 * (EC63 - EF3) * AC94)/1000  # Oviem vuoto
        EC59 = data.ikkuna_ala # Ikkuna pinta_ala
        ED59 = Uarvot[data.rakennusvuosi].U[5] # Ikkuna Uarvo
        TH20 = (EC59 * ED59 * (EC63 - EF3) * AC94)/1000 # Ikkunoden vuoto
        AC206 = säätaulu[kk].maa_t # Alapohjan maalämpötila
        EC58 = data.pinta_ala # Pinta_ala
        EE58 = EC58 / 4 # Pinta_ala / 4 
        ED58 = Uarvot[data.rakennusvuosi].U[1] # Ala-pohja U-arvo
        TG20 = ( EE58 * ED58 * (EC63 - AC206 ) * AC94)/1000 # Alapohjan vuoto
        EC57 = data.yläpohja_ala # Yläpohja pinta-ala
        ED57 = Uarvot[data.rakennusvuosi].U[4] # Yläpohja U-arvo
        TF20 = (EC57 * ED57 * (EC63 - EF3) * AC94)/1000 # Yläpohjan vuoto
        EC56 = data.seinä_ala # Ulkoseinä pinta-ala
        ED56 = Uarvot[data.rakennusvuosi].U[0] # Ulkoseinä U-arvo
        TE20 = (ED56 * EC56 * (EC63 - EF3) * AC94)/1000 # Ulkoseinät vuoto
        TJ20 = (TI20 + TH20 + TG20 + TF20 + TE20) * 0.1 # Kylmäsillat
        EC65 = Uarvot[data.rakennusvuosi].vuoto # Rakennuksen ilmanvaihtoluku
        EC10 = data.pinta_ala * data.kerrosmaara
        EC62 = EC10 * huonekorkeus # tilavuus m3
        EC61 = EC56 + EC57 + EC58 + EC59 + EC60 # vaippa
        if (data.rakennusvuosi < 10):
            EF65 = EC65 / EC61 * EC62
        else:
            EF65 = EC65 
        if (data.kerrosmaara == 1): # 1 krs
            EC66 = 35
        elif (data.kerrosmaara == 2): # 2 krs
            EC66 = 24
        elif (data.kerrosmaara == 3): # 3 krs
            EC66 = 20
        elif (data.kerrosmaara == 4): # 4 krs
            EC66 = 20
        else:   # muut kerrokset
            EC66 = 15
        TM19 = (EF65 * EC61)/(3600 * EC66)
        TL20 = (1.2 * 1000 * TM19 * (EC63 - EF3) * AC94)/1000 # Qvuoto
        TQ20 = TO20 + TJ20 + TI20 + TH20 + TG20 + TF20 + TE20 + TL20
        tila2_lammitys += TQ20 
    return round(tila2_lammitys,2)


@register.filter
def Tilojen_nettolammitys(data): #EE95
    tila_lammitys = Fun_Tilojen_nettolammitys(data)
    return round(tila_lammitys,2)

@register.filter #EE93
def Tilojen_lammitys(data):
    try:
        TQ32 = 0
        EC60 = data.ovet_ala # Ovet pinta-ala
        ED60 = Uarvot[data.rakennusvuosi].U[6] # Ovet Uarvo
        EC59 = data.ikkuna_ala # Ikkuna pinta_ala
        ED59 = Uarvot[data.rakennusvuosi].U[5] # Ikkuna Uarvo
        EC58 = data.pinta_ala # Pinta_ala
        ED58 = Uarvot[data.rakennusvuosi].U[1] # Ala-pohja U-arvo
        EC57 = data.yläpohja_ala # Yläpohja pinta-ala
        ED57 = Uarvot[data.rakennusvuosi].U[4] # Yläpohja U-arvo
        EC56 = data.seinä_ala # Ulkoseinä pinta-ala
        ED56 = Uarvot[data.rakennusvuosi].U[0] # Ulkoseinä U-arvo
        EC65 = Uarvot[data.rakennusvuosi].vuoto # Rakennuksen ilmanvaihtoluku
        EC63 = data.sisalampo
        EC37 = Tsp
        EC39 = data.h_pv/24
        EC40 = data.pv_vko/7
        EC32 = Kluokat[data.kayttotarkoitus].virta * data.pinta_ala
        if(data.iv_tapa == 1):
            EE33 = Uarvot[data.rakennusvuosi].iv_paino
        elif(data.iv_tapa == 2):
            EE33 = Uarvot[data.rakennusvuosi].iv_poisto
        elif(data.iv_tapa == 3):
            EE33 = Uarvot[data.rakennusvuosi].iv_tulopoisto
        else:
            EE33 = 0
        if (data.kerrosmaara == 1): # 1 krs
            EC66 = 35
        elif (data.kerrosmaara == 2): # 2 krs
            EC66 = 24
        elif (data.kerrosmaara == 3): # 3 krs
            EC66 = 20
        elif (data.kerrosmaara == 4): # 4 krs
            EC66 = 20
        else:   # muut kerrokset
            EC66 = 15
        EC61 = EC56 + EC57 + EC58 + EC59 + EC60 # vaippa
        EC10 = data.pinta_ala * data.kerrosmaara
        EC62 = EC10 * huonekorkeus # tilavuus m3
        if (data.rakennusvuosi < 10):
            EF65 = (EC65 / EC61) * EC62
        else:
            EF65 = EC65 
        TK32 = 0
        TL32 = 0
        TO32 = 0
        for kk in range(1,13):
            AC94 = KkData[kk].tunnit # Kuukauden tunnit
            EF3 = säätaulu[kk].A[data.alue]
            AC206 = säätaulu[kk].maa_t # Alapohjan maalämpötila
            TE32 =( EC56 * ED56 * (EC63 - EF3) * AC94) / 1000 # Ulkoseinä johtuminen
            TF32 =( EC57 * ED57 * (EC63 - EF3) * AC94) / 1000 # Yläpohja johtuminen
            TG32 =( EC58 * ED58 * (EC63 - AC206) * AC94) / 1000 # Alapohja johtuminen
            TH32 =( EC59 * ED59 * (EC63 - EF3) * AC94) / 1000 # Ikkunan johtuminen
            TI32 =( EC60 * ED60 * (EC63 - EF3) * AC94) /1000 # Ovet johtuminen
            TJ32 = (TE32 + TF32 + TG32 + TH32 + TI32) * 0.1 #Kylmäsillat
            TK32 += TE32 + TF32 + TG32 + TH32 + TI32 + TJ32 
            TM19 = (EF65 * EC61) / (3600* EC66) 
            TL32 += (1.2 * 1000 * TM19 * ( EC63 - EF3) * AC94) / 1000
            if(data.iv_tapa == 3):
                TO32 += (EC39 * EC40 * 1.2 * 1000 * (EC32 / 1000) * (EC63 - EC37) * AC94) / 1000 #koneellinen tulopoisto
            else:
                TO32 += (EC39 * EC40 * 1.2 * 1000 * (EE33 / 1000) * (EC63 - EF3) * AC94) / 1000 #korvausilma
        TQ32 = TK32 + TL32 + TO32
        EE93 = TQ32
    except:
        return "Error"
    return round(EE93,1)


@register.filter #EE94
def Lampokuormat(data):
    EC60 = data.ovet_ala # Ovet pinta-ala
    ED60 = Uarvot[data.rakennusvuosi].U[6] # Ovet Uarvo
    EC59 = data.ikkuna_ala # Ikkuna pinta_ala
    ED59 = Uarvot[data.rakennusvuosi].U[5] # Ikkuna Uarvo
    EC58 = data.pinta_ala # Pinta_ala
    ED58 = Uarvot[data.rakennusvuosi].U[1] # Ala-pohja U-arvo
    EC57 = data.yläpohja_ala # Yläpohja pinta-ala
    ED57 = Uarvot[data.rakennusvuosi].U[4] # Yläpohja U-arvo
    EC56 = data.seinä_ala # Ulkoseinä pinta-ala
    ED56 = Uarvot[data.rakennusvuosi].U[0] # Ulkoseinä U-arvo
    EC65 = Uarvot[data.rakennusvuosi].vuoto # Rakennuksen ilmanvaihtoluku
    EC61 = EC56 + EC57 + EC58 + EC59 + EC60 # vaippa
#    AC93 = Uarvot[data.rakennusvuosi].vuoto
    EC9 = data.pinta_ala
    EC63 = data.sisalampo
    EC37 = Tsp
    EC39 = data.h_pv/24
    EC40 = data.pv_vko/7
    EC72 = data.pv_vko/7 # Viikoittainen käytniaikasuhde
    EC71 = data.h_pv/24 # Vuorokautinen kyyntiaikasuhde
    EC67 = Kluokat[data.kayttotarkoitus].ominais_C
    EC32 = Kluokat[data.kayttotarkoitus].virta * data.pinta_ala
    EC73 = Kluokat[data.kayttotarkoitus].laitteet # kuluttajalaite teho
    EC75 = Kluokat[data.kayttotarkoitus].valaistus # valaistuksen ominaisteho
    EC76 = Kluokat[data.kayttotarkoitus].valaistus #Valaistus käyttöaste
    EC78 = Kluokat[data.kayttotarkoitus].kuorma # Ihmisten läsnäoloaste
    EC77 = Kluokat[data.kayttotarkoitus].ihmiset # Ihmisten lämpökuorma
    EC51 = Kluokat[data.kayttotarkoitus].lkv_putki_ominais
    EC49 = Kluokat[data.kayttotarkoitus].lkv_eriste
    if data.lkv_kiertoeriste == 0:
        EC87 = 40
    elif data.lkv_kiertoeriste == 1:
        EC87 = 10
    elif data.lkv_kiertoeriste == 2:
        EC87 = 6
    elif data.lkv_kiertoeriste == 3:
        EC87 = 15
    elif data.lkv_kiertoeriste == 4:
        EC87 = 8
    elif data.lkv_kiertoeriste == 5:
        EC87 = 5
    else:
        EC87 = 0
    if (data.kerrosmaara == 1): # 1 krs
        EC66 = 35
    elif (data.kerrosmaara == 2): # 2 krs
        EC66 = 24
    elif (data.kerrosmaara == 3): # 3 krs
        EC66 = 20
    elif (data.kerrosmaara == 4): # 4 krs
        EC66 = 20
    else:   # muut kerrokset
        EC66 = 15
    EC8 =  data.kerrosmaara
    EC62 = data.pinta_ala * huonekorkeus * EC8
    if (data.rakennusvuosi < 10):
        EF65 = EC65 / EC61 * EC62
    else:
        EF65 = EC65 
    EE94_kk = 0
    for kk in range(1,13):
        AC94 = KkData[kk].tunnit # Kuukauden tunnit
        EF3 = säätaulu[kk].A[data.alue]
        AC206 = säätaulu[kk].maa_t # Alapohjan maalämpötila
        TO20 = (EC39 * EC40 * 1.2 * 1000 * ( EC32 / 1000 ) * ( EC63 - EC37 ) * AC94 ) / 1000
        TM19 = (EF65 * EC61) / (3600* EC66) 
        TE20 = ( EC56 * ED56 * (EC63 - EF3) * AC94) / 1000 # Ulkoseinä johtuminen
        TF20 = ( EC57 * ED57 * (EC63 - EF3) * AC94) / 1000 # Yläpohja johtuminen
        TG20 = ( EC58 * ED58 * (EC63 - AC206) * AC94) / 1000 # Alapohja johtuminen
        TH20 = ( EC59 * ED59 * (EC63 - EF3) * AC94) / 1000 # Ikkunan johtuminen
        TI20 = ( EC60 * ED60 * (EC63 - EF3) * AC94) /1000 # Ovet johtuminen
        TJ20 = (TE20 + TF20 + TG20 + TH20 + TI20) * 0.1 #Kylmäsillat
        TL20 = (1.2 * 1000 * TM19 * ( EC63 - EF3) * AC94) / 1000
        TQ20 = TO20 + TJ20 + TI20 + TH20 + TG20 + TF20 + TE20 + TL20
        TC36 = EC77 * EC9
        TC38 = (TC36 /1000) * EC72 * EC71 * EC78 * AC94
        EE83 = EC73 * EC9
        EC84 = EC76 * EC9
        if (EC71 * EC72 == 1):
            EC79 = 1 # 100%; 
        else :
            EC79 = EC71 * EC72
        EE84 = EC84 / 1000 * EC79 * EC76 * 8760
        TD38 = EE83 / 8760 * AC94 # Lämpökuorma käyttölaitteet
        TE38 = EE84 / 8760 * AC94 # Lämpökuorma valaistus
        if(data.lkv_tila > 0):
            if (data.lkvputken_eristys == 1): # "40mm" 
                EC47 = LKV_table[data.lkv_tila].havio40
            elif  (data.lkvputken_eristys == 2): # "1000mm"
                EC47 = LKV_table[data.lkv_tila].havio100
            else:
                EC47 = 0
            EE88 = EC47
        else:
            EE88 = 0
        TF38 = EE88 / 8760 * AC94 * 0.5 # klerroin 50%
        EC87_data = EC87 * EC51 * EC49
        EE87 = EC87_data / 1000* EC9 * 8760
        TG38 = EE87 / 8760 * AC94 * 0.5 #kerroin 50%
        AD223 = Solar[kk].az0 # az0 el45
        AE223 = Solar[kk].az90 # az90 el45
        AF223 = Solar[kk].az180 # az180 el45
        AG223 = Solar[kk].az270 # ad270 el45
        AC263 = Solar[kk].az0_lapi # läpäisy pohjinen
        AE263 = Solar[kk].az90_lapi # Läpäisy itä
        AG263 = Solar[kk].az180_lapi # Läpäisy etelä
        AI263 = Solar[kk].az270_lapi # läpäisy länsi
        EE59 = data.ikkuna_ala /4 # pohjoinen ikkunat m2
        EF59 = data.ikkuna_ala /4 # itä ikkuna m2
        EG59 = data.ikkuna_ala /4 # etelä ikkuna m2
        EH59 = data.ikkuna_ala /4 # länsi ikkuna m2
        AC244 = Solar[kk].az0_varj # varjostus pohjoinen 
        AE244 = Solar[kk].az90_varj # varjostus itä
        AG244 = Solar[kk].az180_varj # varjostus etelä
        AI244 = Solar[kk].az270_varj # varjostus länsi
        EC55 = AD223 * AC263 * EE59 * 0.5 * AC244 # aurinkokuorma pohjoinen / kk
        ED55 = AE223 * AE263 * EF59 * 0.5 * AE244 # aurinkokuorma itä / kk
        EE55 = AF223 * AG263 * EG59 * 0.5 * AG244 # aurinkokuorma etelä / kk
        EF55 = AG223 * AI263 * EH59 * 0.5 * AI244 # aurinkokuorma länsi / kk
        TH38 = EC55 + ED55 + EE55 + EF55
        KuormaLampo = (TC38 + TD38 + TE38 + TF38 + TG38 + TH38)
        TO38 = KuormaLampo / TQ20
        TJ38 = (TQ20 * 1000) / ((EC63-EF3) * AC94)
        TL38 = EC9 * EC67
        TN38 = TL38 / TJ38
        TP38 = 1+(TN38/15)
        TQ38 = (1 - pow(TO38,TP38))/(1 - pow(TO38,(TP38+1)))
        TR38 =TQ38 * (TC38 + TD38 + TE38 + TF38 + TG38 + TH38)
        EE94_kk += TQ20 - TR38
    EE94 = EE94_kk
    return (round(EE94,1))

@register.filter
def Osto_yht(data):
    EC76 = Kluokat[data.kayttotarkoitus].valaistus #Valaistus käyttöaste
    EC73 = Kluokat[data.kayttotarkoitus].laitteet # kuluttajalaite teho
    EC74 = Kluokat[data.kayttotarkoitus].kuorma #sisäinen lämpökuorma /m2
    EC75 = Kluokat[data.kayttotarkoitus].valaistus # valaistuksen ominaisteho
    EC9 = data.pinta_ala
    EC39 = data.h_pv/24
    EC72_v = data.val_pv_vko/7 # Viikoittainen käytniaikasuhde
    EC71_v = data.val_h_pv/24 # Vuorokautinen kyyntiaikasuhde
    EC72_k = data.kul_pv_vko/7 # Viikoittainen käytniaikasuhde
    EC71_k = data.kul_h_pv/24 # Vuorokautinen kyyntiaikasuhde
    EC31 = Kluokat[data.kayttotarkoitus].u_ilma * data.pinta_ala
    EC30 = Uarvot[data.rakennusvuosi].Lto_h
    EC63 = data.sisalampo
    EC37 = Tsp
    EC38 = deltaT
    EC40 = data.pv_vko/7

    EC114 = 0 # Tuottojärjestelmät
    EC115 = 0 # Apulaiteet
    EG95 = 1
    EG86 = 1
    TC73 = EG95 / EG86
    if(TC73>0.5):
        TC74 = 0.97
    else:
        TC74 = 0.5
    TC75 = 0
    TC76 = 0
    EG95 = 0
    EE87 = 0
    EE88 = 0
    TC79 = TC74 #* ((0 / TC75) + ((EG86 / TC76))+(1 - TC74) * (EG95 + EG86))
    EC13 = 0 # Polttoainevalinta ToDo
    if(EC13=="maalämpö,ym."):
        EC103 =TC79
    else:
        EC103 = EG86 + EE87+ EE88
    EC118 = EC103 # LKV tuotanto
    EF103 = 200 * 0.0005 * 1000
    if(data.lkv_kierto): # EC50="kyllä"
        EC104 = EF103 * 24 * (365 / 1000)
    else:
        EC104 = 0
    EC119 = EC104 # LKV apulaitteet
    TC32 = 0
    for kk in range(1,13):
        kk_tulos = 0
#        AC93 = KkData[kk].tunnit
        EF3 = säätaulu[kk].A[data.alue]
        TC5 = EF3 + EC30 * (EC63 - EF3)
        if TC5 >= EC37 - EC38:
            TE5 = EC37 - EC38
        else:
            TE5 = TC5
        if  KkData[kk].lto:
            TF5 = TE5
        else:
            TF5 = EF3
        TG5 = TF5 + 0.5
        if TG5 > EC37:
            TH5 = TG5
        else:
            TH5 = EC37
        AC94 = KkData[kk].tunnit # Kuukauden tunnit
        if(KkData[kk].lto): #LTO päälä
            kk_tulos = EC39 * EC40 * 1.2 * (EC31 / 1000) * (TH5 - EC38 - TF5 ) * AC94
        else:
            kk_tulos = 0
        TC32 += kk_tulos # Tuloilman lämmitys

    if(data.iv_tapa == 3):
        EC122 = 0
    else:
        EC122 = TC32
    EC123 = 0
    if (data.iv_tapa == 1): #SFP
        EC34 = Uarvot[data.rakennusvuosi].iv_paino
    elif (data.iv_tapa == 2):
        EC34 = Uarvot[data.rakennusvuosi].iv_poisto
    else:
        EC34 = Uarvot[data.rakennusvuosi].iv_tulopoisto
    EC126 =EC34 * (EC31 / 1000) * EC39 * 8760 # =EE85 IV laitteet
    EC83 = EC73 * EC9
    if (EC71_k * EC72_k == 1):
        EC79_k = 1 # 100%; 
    else:
        EC79_k = EC71_k * EC72_k
    EC129 = EC83 / 1000 * EC79_k * EC74 * 8760 # =EE83 Kuluttajalaitteet
    EC84 = EC75 * EC9 
    if (EC71_v * EC72_v == 1):
        EC79_v = 1 # 100%; 
    else:
        EC79_v = EC71_v * EC72_v
    EC130 = EC84 / 1000 * EC79_v * EC76 * 8760 # =EE84 Valaistus
    EC111 = EC114 + EC115 + EC118 + EC119 + EC122 + EC123 + EC126 + EC129 + EC130
    return round(EC111,1)

@register.filter
def Osto_Tilat(data): # EC114
    TC78 = Fun_TC78(data)
    EC98 = 0
    if (data.kayttotarkoitus == 1):
        EC25 = Elahde[data.lkv_lammitys].Vuosihyoty1 #2-sarake
    else:
        EC25 = Elahde[data.lkv_lammitys].Vuosihyoty2 # 4-sarake
    if(data.kayttotarkoitus == 1):
       #  Lookup sarake 2
       Testi=1
    else:
       # Lookup sarake 4
       Testi=2
    EC13 = 0
    if(EC13=="Maalämpö, ym."):  #polttoainevalinta
       EC100 = TC78; 
    else:
       EC100 = EC98 / EC25
    EC114 = EC100
    return round(EC114,1)


@register.filter
def LKV_varastointi(data):
    LKV_varast = 0
    EC46 = data.lkv_tila
 
    if(EC46>0):
        if (data.lkvputken_eristys == 1): # "40mm" 
            EC47 = LKV_table[data.lkv_tila].havio40
        elif  (data.lkvputken_eristys == 2): # "1000mm"
            EC47 = LKV_table[data.lkv_tila].havio100
        else:
            EC47 = 0
        LKV_varast = EC47
    else:
        LKV_varast = 0
    return round(LKV_varast,1)

@register.filter
def IV_lammitys(data): #EE89
    IV_lammitys = 0
    TC32_kk = 0
    EC39 = data.h_pv/24 # Vuorokausi käyntisuhde
    EC40 = data.pv_vko/7 # Viikko käyntisuhde
    EC9 = data.pinta_ala * data.kerrosmaara #kokonaisala
    EC31 = Kluokat[data.kayttotarkoitus].u_ilma * EC9 # ulkoilmavirta/käyttötarkoitus * kokonaisala
    EC37 = Tsp
    EC38 = deltaT
    EC30 = Uarvot[data.rakennusvuosi].Lto_h
    EC63 = data.sisalampo
    for kk in range(1,13):
        kk_tulos = 0
        EF3 = säätaulu[kk].A[data.alue]
        TC5 = EF3 + EC30 * (EC63 - EF3)
        if TC5 >= EC37 - EC38:
            TE5 = EC37 - EC38
        else:
            TE5 = TC5
        if  KkData[kk].lto:
            TF5 = TE5
        else:
            TF5 = EF3
        TG5 = TF5 + 0.5
        if TG5 > EC37:
            TH5 = TG5
        else:
            TH5 = EC37
        AC94 = KkData[kk].tunnit # Kuukauden tunnit
        if(KkData[kk].lto): #LTO päälä
            kk_tulos = EC39 * EC40 * 1.2 * (EC31 / 1000) * (TH5 - EC38 - TF5 ) * AC94
        else:
            kk_tulos = 0
        TC32_kk += kk_tulos
    TC32 = TC32_kk
    if(data.iv_tapa < 3): # koneelinen tulopoisto
        IV_lammitys = 0
    else:
        IV_lammitys = TC32
    return round(IV_lammitys,1)

def Fun_valasitus(data):
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
    return EE84
    
def Fun_laitteet(data):
    Kuluttaja_teho = Kluokat[data.kayttotarkoitus].laitteet * data.pinta_ala * data.kerrosmaara
    EC71 = data.kul_h_pv / 24 # vuorokausi käyttösuhde
    EC72 = data.kul_pv_vko / 7 # viikoittainen käyttösuhde
    if (EC71 * EC72 == 1): # käyttöasteen suhde
        EC79 = 1
    else:
        EC79 = EC71 * EC72
    EC74 = Kluokat[data.kayttotarkoitus].kuorma
    EE83 = (Kuluttaja_teho / 1000) * EC79 * EC74 * 8760
    return EE83

@register.filter
def Valaistus(data):
    EE84 = Fun_valasitus(data)
    return round(EE84,0)

@register.filter
def Laitteet(data):
    EE83 = Fun_laitteet(data)
    return round(EE83,0)

@register.filter
def Val_Lait(data):
    EE83 = Fun_laitteet(data)
    EE84 = Fun_valasitus(data)
    Tulos = EE83 + EE84
    return round(Tulos,0)

@register.filter
def IV_laitteet(data):
    EC9 = data.pinta_ala * data.kerrosmaara #kokonaisala
    EC31 = Kluokat[data.kayttotarkoitus].u_ilma * EC9 # ulkoilmavirta/käyttötarkoitus * kokonaisala
    if (data.iv_tapa == 1): #SFP
        EC34 = Uarvot[data.rakennusvuosi].iv_paino
    elif (data.iv_tapa == 2):
        EC34 = Uarvot[data.rakennusvuosi].iv_poisto
    else:
        EC34 = Uarvot[data.rakennusvuosi].iv_tulopoisto
    EC39 = data.h_pv/24 # Vuorokausi käyntisuhde
    EE85 = EC34 * (EC31 / 1000) * EC39 * 8760
    return round(EE85,0)

@register.filter
def Tuloilma_lammitys(data):
    EC30 = Uarvot[data.rakennusvuosi].Lto_h
    EC9 = data.pinta_ala * data.kerrosmaara #kokonaisala
    EC31 = Kluokat[data.kayttotarkoitus].u_ilma * EC9 # ulkoilmavirta/käyttötarkoitus * kokonaisala
    EC39 = data.h_pv/24 # Vuorokausi käyntisuhde
    EC40 = data.pv_vko/7 # Viikko käyntisuhde
    EC38 = deltaT
    EC37 = Tsp
    EC63 = data.sisalampo
    TC32 = 0
    for kk in range(1,13):
        kk_tulos = 0
        EF3 = säätaulu[kk].A[data.alue]
        TC5 = EF3 + EC30 * (EC63 - EF3)
        if TC5 >= EC37 - EC38:
            TE5 = EC37 - EC38
        else:
            TE5 = TC5
        if  KkData[kk].lto:
            TF5 = TE5
        else:
            TF5 = EF3
        TG5 = TF5 + 0.5
        if TG5 > EC37:
            TH5 = TG5
        else:
            TH5 = EC37
        AC94 = KkData[kk].tunnit # Kuukauden tunnit
        if(KkData[kk].lto): #LTO päälä
            kk_tulos = EC39 * EC40 * 1.2 * (EC31 / 1000) * (TH5 - EC38 - TF5 ) * AC94
        else:
            kk_tulos = 0
        TC32 += kk_tulos # Tuloilman lämmitys
    if(data.iv_tapa < 3):
        EE89 = TC32 
    else: 
        EE89 = 0
    return round(EE89,1)


@register.filter
def LKV_kierto(kk,data):
    Lampokuormat_F38 = 0.5 # 50%
    if data.lkv_kierto==False:
        Qlkv_C7 = 0
    else:
        Qlkv_C7 = LKV_table[data.kayttotarkoitus].D05 * Kluokat[data.kayttotarkoitus].lkv_putki_ominais * (8760/1000) * LKV_table[data.kayttotarkoitus].tilavuus

    LKV_Kierto = (KkData[kk].tunnit/8760) * Qlkv_C7 * Lampokuormat_F38

    return LKV_Kierto 

@register.filter
def Vaippa_johtuminen(data): #EE90
    Vaippa_joht =0
    TK32 = 0
    EC63 = data.sisalampo
    EC56 = data.seinä_ala # Ulkoseinä pinta-ala
    ED56 = Uarvot[data.rakennusvuosi].U[0] # Ulkoseinä U-arvo
    EC57 = data.yläpohja_ala # Yläpohja pinta-ala
    ED57 = Uarvot[data.rakennusvuosi].U[4] # Yläpohja U-arvo
    EC58 = data.pinta_ala # Pinta_ala = Alapohja
    ED58 = Uarvot[data.rakennusvuosi].U[1] # Ala-pohja U-arvo
    EC59 = data.ikkuna_ala # Ikkuna pinta_ala
    ED59 = Uarvot[data.rakennusvuosi].U[5] # Ikkuna Uarvo
    ED60 = Uarvot[data.rakennusvuosi].U[6] # Ovet Uarvo
    EC60 = data.ovet_ala # Ovet pinta-ala
    for kk in range(1,13):
        AC94 = KkData[kk].tunnit # Kuukauden tunnit
        EF3 = säätaulu[kk].A[data.alue]
        AC206 = säätaulu[kk].maa_t # Alapohjan maalämpötila
        TE32 =( EC56 * ED56 * (EC63 - EF3) * AC94) / 1000 # Ulkoseinä johtuminen
        TF32 =( EC57 * ED57 * (EC63 - EF3) * AC94) / 1000 # Yläpohja johtuminen
        TG32 =( EC58 * ED58 * (EC63 - AC206) * AC94) / 1000 # Alapohja johtuminen
        TH32 =( EC59 * ED59 * (EC63 - EF3) * AC94) / 1000 # Ikkunan johtuminen
        TI32 =( EC60 * ED60 * (EC63 - EF3) * AC94) /1000 # Ovet johtuminen
        TJ32 = (TE32 + TF32 + TG32 + TH32 + TI32) * 0.1 #Kylmäsill
        TK32 += TE32 + TF32 + TG32 + TH32 + TI32 + TJ32
    Vaippa_joht = TK32
    return round(Vaippa_joht,1)

@register.filter
def Vuotoilma_lammitys(data): #EE91
    EC63 = data.sisalampo
    EC10 = data.pinta_ala * data.kerrosmaara
    EC62 = EC10 * huonekorkeus # tilavuus m3
    EC65 = Uarvot[data.rakennusvuosi].vuoto # Rakennuksen ilmanvaihtoluku
    EC56 = data.seinä_ala # Ulkoseinä pinta-ala
    EC57 = data.yläpohja_ala # Yläpohja pinta-ala
    EC58 = data.pinta_ala # Pinta_ala = Alapohja
    EC59 = data.ikkuna_ala # Ikkuna pinta_ala
    EC60 = data.ovet_ala # Ovet pinta-ala
    EC61 = EC56 + EC57 + EC58 + EC59 + EC60 # vaippa
    if (data.kerrosmaara == 1): # 1 krs
        EC66 = 35
    elif (data.kerrosmaara == 2): # 2 krs
        EC66 = 24
    elif (data.kerrosmaara == 3): # 3 krs
        EC66 = 20
    elif (data.kerrosmaara == 4): # 4 krs
        EC66 = 20
    else:   # muut kerrokset
        EC66 = 15
    if (data.rakennusvuosi < 10):
        EF65 = EC65 / EC61 * EC62
    else:
        EF65 = EC65 
    TL32 = 0
    for kk in range (1,13):
        AC94 = KkData[kk].tunnit # Kuukauden tunnit
        EF3 = säätaulu[kk].A[data.alue]
        TM19 = (EF65 * EC61) / (3600* EC66) 
        TL32 += (1.2 * 1000 * TM19 * ( EC63 - EF3) * AC94) / 1000
    I_vuoto_lammitys = TL32
    return round(I_vuoto_lammitys,1)

@register.filter #EE92
def Tuloilma_lammitys(data):
    EE92 = 0
    EC63 = data.sisalampo
    EC32 = Kluokat[data.kayttotarkoitus].virta * data.pinta_ala
    EC39 = data.h_pv/24 # Vuorokausi käyntisuhde
    EC40 = data.pv_vko/7 # Viikko käyntisuhde
    EC37 = Tsp
    if(data.iv_tapa == 1):
        EE33 = Uarvot[data.rakennusvuosi].iv_paino
    elif(data.iv_tapa == 2):
        EE33 = Uarvot[data.rakennusvuosi].iv_poisto
    elif(data.iv_tapa == 3):
        EE33 = Uarvot[data.rakennusvuosi].iv_tulopoisto
    else:
        EE33 = 0
    for kk in range(1,13):
        AC94 = KkData[kk].tunnit # Kuukauden tunnit
        EF3 = säätaulu[kk].A[data.alue]
        if(data.iv_tapa == 3):
            TO32 = (EC39 * EC40 * 1.2 * 1000 * (EC32 / 1000) * (EC63 - EC37) * AC94) / 1000 #koneellinen tulopoisto
        else:
            TO32 = (EC39 * EC40 * 1.2 * 1000 * (EE33 / 1000) * (EC63 - EF3) * AC94) / 1000 #korvausilma
        EE92 += TO32
    return round(EE92,1)


@register.filter
def Vaippa_vuoto(kk,data):
    if data.lkv_kierto==False:
        Qlkv_C7 = 0
    else:
        Qlkv_C7 = LKV_table[data.kayttotarkoitus].D05 * Kluokat[data.kayttotarkoitus].lkv_putki_ominais * (8760/1000) * LKV_table[data.kayttotarkoitus].tilavuus

    if data.iv_tapa in [2,3]:
        Alku_B71 = Kluokat[data.kayttotarkoitus].virta  * data.pinta_ala
    else:
        Alku_B71 = 0

    if data.lto == True:
        Alku_B69 = Uarvot[data.rakennusvuosi].Lto_h
    else:
        Alku_B69 = 0

    Qiv_E3 = KkData[kk].k_lampo[data.alue] + Alku_B69 * (Kluokat[data.kayttotarkoitus].l_raja - KkData[kk].k_lampo[data.alue])

    if Qiv_E3 >= (Alku_B75 - 0.5):
        Qiv_G3 = Alku_B75 - 0.5
    else:
        Qiv_G3 = Qiv_E3

    if KkData[kk].lto == True:
        Qiv_H3 = Qiv_G3
    else:
        Qiv_H3 = KkData[kk].k_lampo[data.alue]

    if Qiv_H3 < Alku_B75:
        TSP = Alku_B75
    else:
        TSP = Qiv_H3 + 0.5

    if data.iv_tapa == 1:
        QivtuloC2 = ((Kluokat[data.kayttotarkoitus].pvm_h /24) * (Kluokat[data.kayttotarkoitus].vko_p /7) *1.2*1000 * ((Kluokat[data.kayttotarkoitus].virta  * data.pinta_ala - Alku_B71)/1000) * (Kluokat[data.kayttotarkoitus].l_raja-KkData[kk].k_lampo[data.alue]) * KkData[kk].tunnit)/1000
    else:
        QivtuloC2 = ((Kluokat[data.kayttotarkoitus].pvm_h /24) * (Kluokat[data.kayttotarkoitus].vko_p /7) *1.2*1000 * (Alku_B71/1000) * (Kluokat[data.kayttotarkoitus].l_raja-TSP) * KkData[kk].tunnit)/1000

    if data.rakennusvuosi > 6:
        Alku_B39 = 4  
    else: 
        Alku_B39 = 6 # "(VLOOKUP(B9;Alkutaulukot!B2:P72;2;FALSE)"
                
    Alku_C49 =  math.sqrt(data.pinta_ala) * E143 * data.kerrosmaara * 4 + (2 * data.pinta_ala) # Ukoseina pinta-ala # Ulkovaippa
    Alku_F45 = data.pinta_ala * E143 * data.kerrosmaara

    Alku_E39 = Alku_B39 / Alku_C49 * Alku_F45
    
    if data.kerrosmaara==1:
        Alku_B40 = 35
    elif data.kerrosmaara==2:
        Alku_B40 = 24
    elif data.kerrosmaara==3:
        Alku_B40 = 20
    elif data.kerrosmaara==4: 
        Alku_B40 = 20
    else:
        Alku_B40 = 15

    QvuotoC3 =(Alku_E39 * Alku_C49 )/ (3600 * Alku_B40)

    Alku_B_37 = Kluokat[data.kayttotarkoitus].l_raja

    Qvuoto_C7 =(1.2 * 1000 * QvuotoC3 * (Alku_B_37 - KkData[kk].k_lampo[data.alue] ) * KkData[kk].tunnit ) / 1000

    return Qvuoto_C7

def EnergiaTuotto(data):
    Energiatuotto = 0
    Q_Vuosituotto = 0
    for kk in range(1,13):
        E143 = 2.8 # seinan korkeus
        Alku_B75 = 18 # TSP
        Lampokuormat_F38 = 0.5 # 50%

#    C4 = Ihmislammitys(kk,data)
#    C23 = LKVvarastointi(kk,data)
#    Kuluttajalaitteetjne_E11 = Laitteet(kk, data) + Valaistus(kk,data)
#    LKV_Lampokuorma = LKV_kierto(kk,data)
#    F53 = Aurinkosateily(kk,data)

## NÄITÄ TARVITAAN VIELÄ MYÖHEMMISSÄ LASKUISSA: ####
        if data.lkv_kierto==False:
            Qlkv_C7 = 0
        else:
            Qlkv_C7 = LKV_table[data.kayttotarkoitus].D05 * Kluokat[data.kayttotarkoitus].lkv_putki_ominais * (8760/1000) * LKV_table[data.kayttotarkoitus].tilavuus

        if data.iv_tapa in [2,3]:
            Alku_B71 = Kluokat[data.kayttotarkoitus].virta  * data.pinta_ala
        else:
            Alku_B71 = 0
#   AH77 = Kluokat[data.kayttotarkoitus].virta  * data.pinta_ala - Alku_B71
#   AB37 = Kluokat[data.kayttotarkoitus].l_raja

        if data.lto == True:
            Alku_B69 = Uarvot[data.rakennusvuosi].Lto_h
        else:
            Alku_B69 = 0

        Qiv_E3 = KkData[kk].k_lampo[data.alue] + Alku_B69 * (Kluokat[data.kayttotarkoitus].l_raja - KkData[kk].k_lampo[data.alue])

        if Qiv_E3 >= (Alku_B75 - 0.5):
            Qiv_G3 = Alku_B75 - 0.5
        else:
            Qiv_G3 = Qiv_E3

        if (KkData[kk].lto):
            Qiv_H3 = Qiv_G3
        else:
            Qiv_H3 = KkData[kk].k_lampo[data.alue]

        if Qiv_H3 < Alku_B75:
            TSP = Alku_B75
        else:
            TSP = Qiv_H3 + 0.5

        if data.iv_tapa == 1:
            QivtuloC2 = ((data.h_pv /24) * (data.pv_vko /7) *1.2*1000 * ((Kluokat[data.kayttotarkoitus].virta  * data.pinta_ala - Alku_B71)/1000) * (Kluokat[data.kayttotarkoitus].l_raja-KkData[kk].k_lampo[data.alue]) * KkData[kk].tunnit)/1000
        else:
            QivtuloC2 = ((data.h_pv /24) * (data.pv_vko /7) *1.2*1000 * (Alku_B71/1000) * (Kluokat[data.kayttotarkoitus].l_raja - TSP) * KkData[kk].tunnit)/1000


        Alku_B44 = Uarvot[data.rakennusvuosi].U[1] # Uarvo seinat
        Alku_C44 = math.sqrt(data.pinta_ala) * E143 * data.kerrosmaara * 4 - ((math.sqrt(data.pinta_ala) * E143 * data.kerrosmaara * 4) * 0.15) # Ukoseina pinta-ala
        Alku_B45 = Uarvot[data.rakennusvuosi].U[4] #U_arvo Ylapohja
        Alku_C45 = data.pinta_ala / data.kerrosmaara #Ylapohja pinta_ala

        Qjoht_C22 =(Alku_B44 * Alku_C44 * (Kluokat[data.kayttotarkoitus].l_raja - KkData[kk].k_lampo[data.alue])* KkData[kk].tunnit) / 1000 # Ulkovaippa
        Qjoht_D22 =(Alku_B45 * Alku_C45 * (Kluokat[data.kayttotarkoitus].l_raja - KkData[kk].k_lampo[data.alue])* KkData[kk].tunnit) / 1000 # Ylapohja

        Qjoht_M6 = KkData[kk].maapohja # maapohjan lampotila
        Alku_B46 = Uarvot[data.rakennusvuosi].U[2] #U-arvo maapohja
        Alku_B47 = Uarvot[data.rakennusvuosi].U[6] #U-arvo ikkunat
        Alku_C47 = Alku_C44 * 0.15 #Ikkuna pinta-ala 15% ulkoseinasta
        Alku_B48 = Uarvot[data.rakennusvuosi].U[5] #U-arvo ovet
        Alku_C48 = 0.8 * 2 * data.kerrosmaara * 4 #Ulko-ovet pinta-ala oletus 5 ovea / kerros

        Qjoht_E22 =(Alku_B46 * data.pinta_ala * (Kluokat[data.kayttotarkoitus].l_raja - Qjoht_M6 )* KkData[kk].tunnit ) / 1000   # Alapohja
        Qjoht_F22 =(Alku_B47 * Alku_C47 * (Kluokat[data.kayttotarkoitus].l_raja - KkData[kk].k_lampo[data.alue])* KkData[kk].tunnit) / 1000  # Ovet
        Qjoht_G22 =(Alku_B48* Alku_C48 * (Kluokat[data.kayttotarkoitus].l_raja - KkData[kk].k_lampo[data.alue]) * KkData[kk].tunnit) / 1000  #


        Qjoht_H22 = Qjoht_C22 + Qjoht_D22 + Qjoht_E22 + Qjoht_F22 + Qjoht_G22 # "Ulkovaippa"

        Qjoht_I22 = 0.1 * Qjoht_H22  # "kylmasillat" = 10% Ulkovaipan johtuminen

        Qjoht_B22 = Qjoht_H22 + Qjoht_I22

        QivtuloC19 = QivtuloC2 + Vaippa_vuoto(kk,data) + Qjoht_B22
        C38 = (KkData[kk].tunnit/8760) * Qlkv_C7 * Lampokuormat_F38

        Lampokuormat_O22 =(Ihmislammitys(kk,data) + LKVvarastointi(kk,data) + Laitteet(kk, data) + Valaistus(kk,data) + C38 + Aurinkosateily(kk,data)) / QivtuloC19

        Alku_B41 = Kluokat[data.kayttotarkoitus].ominais_C

        Lampokuormat_K19 = Alku_B41
        Lampokuormat_K20 = data.pinta_ala * Lampokuormat_K19

        if data.iv_tapa == 2:
            Qivtulo_C2 = ((Kluokat[data.kayttotarkoitus].pvm_h /24) * (Kluokat[data.kayttotarkoitus].vko_p /7) * 1.2 * 1000 * ((Kluokat[data.kayttotarkoitus].virta  * data.pinta_ala - Alku_B71) / 1000) * (Kluokat[data.kayttotarkoitus].l_raja - KkData[kk].k_lampo[data.alue]) * KkData[kk].tunnit)/1000
        else:
            Qivtulo_C2 = ((Kluokat[data.kayttotarkoitus].pvm_h /24) * (Kluokat[data.kayttotarkoitus].vko_p /7) * 1.2 * 1000 * (Alku_B71 / 1000) * (Kluokat[data.kayttotarkoitus].l_raja - TSP) * KkData[kk].tunnit)/1000

        #print("AlkuB77:", Alku_B77 ,"AlkuB78:", Alku_B78 ,"AlkuB71:", Alku_B71 , "AlkuB37:",Alku_B37 ,"QivJ3:", TSP, "KkData:",KkData[kk].k_lampo[data.alue],  KkData[kk].tunnit)

        Qivtulo_C19 = Qivtulo_C2 + Vaippa_vuoto(kk,data) + Qjoht_B22
        #print("QivC19:", Qivtulo_C19 ,"QivC2:", Qivtulo_C2 , "QivC7:",Qvuoto_C7 , Qjoht_B22)

        Lampokuormat_K6 =(1000 * Qivtulo_C19)/(( Kluokat[data.kayttotarkoitus].l_raja - KkData[kk].k_lampo[data.alue]) * KkData[kk].tunnit)
        #print("QivC19:", Qivtulo_C19, "AlkuB37:", Alku_B37, "KkData_klampo:", KkData[kk].k_lampo[data.alue], "tunnit:", KkData[kk].tunnit)

        Lampokuormat_K22 = Lampokuormat_K20 / Lampokuormat_K6
        #print("K20:", Lampokuormat_K20, "K6:", Lampokuormat_K6)
        Lampokuormat_P22 = 1 + (Lampokuormat_K22 / 15)
        #print("K22:",round(Lampokuormat_K22,2), "K20:",round(Lampokuormat_K20,2), "K6:",round(Lampokuormat_K6,2))

        Lampokuormat_Q22 =(1 - pow(Lampokuormat_O22,Lampokuormat_P22)) / (1 - pow(Lampokuormat_O22,(Lampokuormat_P22 + 1)))

        Energiatuotto = (Ihmislammitys(kk,data) + LKVvarastointi(kk,data) + Aurinkosateily(kk,data) + Laitteet(kk, data) + Valaistus(kk,data) + LKV_kierto(kk,data)) * Lampokuormat_Q22
        Q_Vuosituotto += Energiatuotto
    return round(Q_Vuosituotto,1)
