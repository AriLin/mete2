from dataclasses import dataclass
from django import template
register = template.Library()


@dataclass
class U_arvot:
    yy: str
    U: list
    Lto_h: float
    vuoto: int
    ilp_max: int
    iv_paino: int
    iv_poisto: float
    iv_tulopoisto: float

Uarvot = []
# rakennusluvitettu,[ulkoseinä,maanpinta,ryömintä,ulkoilma,yläpohja,ovi,ikkuna,], LTO hyotysuhde
Uarvot.append(U_arvot("alustus",[0,0,0,0,0,0,0],0,6,6000,0,1.5,2.5))
Uarvot.append(U_arvot("<-1969",[0.81,0.45,0.47,0.35,0.45,2.2,2.8],0,6,6000,0,1.5,2.5))
Uarvot.append(U_arvot("1969-1976",[0.81,0.45,0.47,0.35,0.45,2.2,2.8],0,6,6000,0,1.5,2.5))
Uarvot.append(U_arvot("1976-1978",[0.7,0.4,0.4,0.35,0.35,1.4,2.1],0,6,6000,0,1.5,2.5))
Uarvot.append(U_arvot("1978-1985",[0.35,0.4,0.4,0.29,0.29,1.4,2.1],0,6,6000,0,1.5,2.5))
Uarvot.append(U_arvot("1985-10/2003",[0.28,0.36,0.4,0.22,0.22,1.4,2.1],0.3,6,5000,0,1.5,2.5))
Uarvot.append(U_arvot("10/2003-2008",[0.25,0.25,0.2,0.16,0.16,1.4,1.4],0.3,4,3000,0,1.5,2.5))
Uarvot.append(U_arvot("2008-2010",[0.24,0.24,0.2,0.16,0.15,1.4,1.4],0.3,4,3000,0,1.5,2.5))
Uarvot.append(U_arvot("2010-2012",[0.17,0.16,0.17,0.09,0.09,1,1],0.45,4,3000,0,1.0,2.0))
Uarvot.append(U_arvot("2012-2018",[0.17,0.16,0.17,0.09,0.09,1,1],0.45,4,3000,0,1.0,2.0))
Uarvot.append(U_arvot("2018->",[0.17,0.16,0.17,0.09,0.09,1,1],0.55,4,3000,0,0.9,1.8))


@dataclass
class K_Luokat:
    luokka: str
    pvm_h: int
    vko_p: int
    kuorma: float
    valaistus: int
    laitteet: int
    ihmiset: int
    v_kaytto: float
    lkv: int
    virta: float 
    l_raja: int # lämmitysraja
    j_raja: int # jäähdytysraja
    u_ilma: int # Ulkoilmavirta

    lkv_kierto: float
    lkv_eieriste: float
    lkv_suoja: float
    lkv_eriste: float
    lkv_eriste_plus: float
    lkv_putki_ominais: float
    ominais_C:  int # Crak.omin


Kluokat = []
Kluokat.append(K_Luokat("Käyttötarkoitus",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0))
Kluokat.append(K_Luokat("Pientalo",24,7,0.6,6,3,2,0.1,35,0.4,21,27,0.4,0.96,0.75,0.85,0.89,0.92,0.2,70))
Kluokat.append(K_Luokat("Kerrostalo",24,7,0.6,9,4,3,0.1,35,0.5,21,27,0.5,0.97,0.76,0.86,0.9,0.94,0.2,160))
Kluokat.append(K_Luokat("Toimisto",11,5,0.65,10,12,5,0,6,2,21,25,2,0.88,0.69,0.78,0.82,0.85,0.06,110))
Kluokat.append(K_Luokat("Liikerakennus",13,6,1.0,19,1,2,0,4,2,18,25,2,0.87,0.68,0.77,0.81,0.84,0.06,110))
Kluokat.append(K_Luokat("Majoitus",24,7,0.3,11,4,4,0,40,2,21,25,2,0.97,0.76,0.86,0.9,0.94,0.25,110))
Kluokat.append(K_Luokat("Opetus", 8,5,0.6,14,8,14,0,11,3,21,25,3,0.89,0.7,0.79,0.83,0.86,0.2,110))
Kluokat.append(K_Luokat("Liikunta",14,7,0.5,10,0,5,0,20,2,18,25,2,0.98,0.77,0.87,0.91,0.95,0.06,110))
Kluokat.append(K_Luokat("Sairaala",24,7,0.6,7,9,8,0,30,4,22,25,4,0.94,0.74,0.84,0.88,0.91,0.25,110))

# Kuukausikohtaiset laskenta-arvot
@dataclass
class Kk_data:
    kuukausi: str
    lto: bool     #lto päällä
    j_lampo: bool #jälkilämmitys päällä
    tunnit: int   #tunteja kuukausdessa 
    k_lampo: list #kuukausittaine keskilämpötila alueittain
    maapohja: float #maapohja lämpö
    d_maapohja: int # Delta maapoja lämpö
    

KkData = []

KkData.append(Kk_data("Mitoitus",False,False,0,[0,-26,-29,-32,-38],0,0))
KkData.append(Kk_data("tammikuu",True,True,744,[0,-3.97,-3.97,-8,-13.06],10.57,0))
KkData.append(Kk_data("helmikuu",True,True,672,[0,-4.5,-4.5,-7.1,-12.62],9.57,-1))
KkData.append(Kk_data("maaliskuu",True,True,744,[0,-2.58,-2.58,-3.53,-6.88],8.57,-2))
KkData.append(Kk_data("huhtikuu",True,True,720,[0,4.5,4.5,2.42,-1.56],7.57,-3))
KkData.append(Kk_data("toukokuu",True,True,744,[0,10.76,10.76,8.84,5.4],7.57,-3))
KkData.append(Kk_data("kesäkuu",True,True,720,[0,14.23,14.23,13.39,13.03],8.57,-2))
KkData.append(Kk_data("heinäkuu",False,False,744,[0,17.3,17.3,15.76,14.36],10.57,0))
KkData.append(Kk_data("elokuu",False,False,744,[0,16.05,16.05,13.76,12.06],11.57,1))
KkData.append(Kk_data("syyskuu",True,True,720,[0,10.53,10.53,9.18,6.6],12.57,2))
KkData.append(Kk_data("lokakuu",True,True,744,[0,6.2,6.2,4.07,0.15],13.57,3))
KkData.append(Kk_data("marraskuu",True,True,720,[0,0.5,0.5,-1.76,-6.78],13.57,3))
KkData.append(Kk_data("joulukuu",True,True,744,[0,-2.19,-2.19,-5.92,-10.08],12.57,2))
KkData.append(Kk_data("yht",False,False,8760,[0,5.57,5.57,3.43,0.05],10.57,0))

@dataclass
class Lammitystapa:
    ratkaisu: str
    menovesi: int
    paluuvesi: int
    a_hyoty: float
    sahko: float
    lammonjako: str
    jako_nro: int
    
Lammitys = []

Lammitys.append(Lammitystapa("ratkaisu",0,0,0.0,0.0,"uunilammitys",0))
Lammitys.append(Lammitystapa("Vesiradiaattori 45/35",45,35,0.9,2.0,"vasikeskulämmitys",1))
Lammitys.append(Lammitystapa("Vesiradiaattori 70/40",70,40,0.9,2.0,"vasikeskulämmitys",1))
Lammitys.append(Lammitystapa("Vesiradiaattori 90/70",90,70,0.85,2.0,"vasikeskulämmitys",1))
Lammitys.append(Lammitystapa("Vesiradiaattori 70/40 jako",70,40,0.8,2.0,"vasikeskulämmitys",1))
Lammitys.append(Lammitystapa("Vesiradiaattori 45/35 jako",45,35,0.85,2.0,"vasikeskulämmitys",1))
Lammitys.append(Lammitystapa("Lattialämmitys 40/30 (vesi)",40,30,0.8,2.5,"vasikeskulämmitys",1))
Lammitys.append(Lammitystapa("Kattolämmitys (sähkö)",0,0,0.9,0.5,"suora sähkölämmitys",2))
Lammitys.append(Lammitystapa("Ikkunalämmitys (sähkö)",0,0,0.8,0.5,"suora sähkölämmitys",2))
Lammitys.append(Lammitystapa("Ilmanvaihtolämpö",0,0,0.9,0.5,"ilmakeskuslämmitys",3))
Lammitys.append(Lammitystapa("Lattialämmitys (sähkö)",0,0,0.9,0.5,"suora sähkölämmitys",2))
Lammitys.append(Lammitystapa("Muu lämmitys",0,0,0.8,0.5,"uunilammitys",0))

@dataclass
class LKV_data:
    tilavuus: int
    havio40: int
    havio100: int
    ominaisarvo: list # [kierto,D05,D15,suoja,S05,S15]

LKV_table = []

LKV_table.append(LKV_data(0,0,0,[0,0,0,0,0,0]))
LKV_table.append(LKV_data(50,440,220,[40,10,6,15,8,5]))
LKV_table.append(LKV_data(100,640,320,[40,10,6,15,8,5]))
LKV_table.append(LKV_data(150,640,320,[40,10,6,15,8,5]))
LKV_table.append(LKV_data(200,830,420,[40,10,6,15,8,5]))
LKV_table.append(LKV_data(300,1300,650,[40,10,6,15,8,5]))
LKV_table.append(LKV_data(500,1700,850,[40,10,6,15,8,5]))
LKV_table.append(LKV_data(1000,2100,1100,[40,10,6,15,8,5]))
LKV_table.append(LKV_data(2000,3000,1500,[40,10,6,15,8,5]))
LKV_table.append(LKV_data(4000,4000,2000,[40,10,6,15,8,5]))

@dataclass
class Sääalue:
    kk: str
    A: list
    Mitoitus: list
    maa_t: float

säätaulu = []

säätaulu.append(Sääalue("keskiarvo", [0,6.968, 5.325, 4.1771, 1.533],[0,5.57,5.57,3.43,0.05],10.57))
säätaulu.append(Sääalue("tammikuu", [0,-3.97, -3.97, -8, -13.06],[0,-3.97,-3.97,-8,-13.06],10.57))
säätaulu.append(Sääalue("helmikuu", [0,-4.5, -4.5, -7.1, -12.62],[0,-4.5,-4.5,-7.1,-12.62],9.57))
säätaulu.append(Sääalue("maaliskuu", [0,-2.58, -2.58, -3.53, -6.88],[0,-2.58,-2.58,-3.53,-6.88],8.57))
säätaulu.append(Sääalue("huhtikuu", [0,4.5, 4.5, 2.42, -1.56],[0,4.5,4.5,2.42,-1.56],7.57))
säätaulu.append(Sääalue("toukokuu", [0,10.76, 10.76, 8.84, 5.4],[0,10.76,10.76,8.84,5.4],7.57))
säätaulu.append(Sääalue("kesäkuu", [0,14.32, 14.32, 13.39, 13.03],[0,14.23,14.23,13.39,13.03],8.57))
säätaulu.append(Sääalue("heinäkuu", [0,17.3, 17.3, 15.76, 14.36],[0,17.3,17.3,15.76,14.36],10.57))
säätaulu.append(Sääalue("elokuu", [0,16.05, 16.05, 13.76, 12.06],[0,16.05,16.05,13.76,12.06],11.57))
säätaulu.append(Sääalue("syyskuu", [0,10.53, 10.53, 9.18, 6.6],[0,10.53,10.53,9.18,6.6],12.57))
säätaulu.append(Sääalue("lokakuu", [0,6.2, 6.2, 4.07, 0.15],[0,6.2,6.2,4.07,0.15],13.57))
säätaulu.append(Sääalue("marraskuu", [0,0.5, 0.5, -1.76, -6.78],[0,0.5,0.5,-1.76,-6.78],13.57))
säätaulu.append(Sääalue("joulukuu", [0,-2.19, -2.19, -5.92, -10.08],[0,-2.19,-2.19,-5.92,-10.08],12.57))

# LKV lämpöhäviöt 
@dataclass
class Lkv_Havio:
    teksti: str
    tilavuus: int
    m40: int
    m100 : int

LKV_h = []
LKV_h.append(Lkv_Havio("0l",0,0,0))
LKV_h.append(Lkv_Havio("50l",50,440,220))
LKV_h.append(Lkv_Havio("100l",100,640,320))
LKV_h.append(Lkv_Havio("150l",150,830,420))
LKV_h.append(Lkv_Havio("200l",200,1000,500))
LKV_h.append(Lkv_Havio("300l",300,1300,650))
LKV_h.append(Lkv_Havio("500l",500,1700,850))
LKV_h.append(Lkv_Havio("1000l",1000,2100,1100))
LKV_h.append(Lkv_Havio("2000l",2000,3000,1500))
LKV_h.append(Lkv_Havio("3000l",3000,4000,2000))

#AURINKOSÄTEILY 
@dataclass
class Aurinko:
    kk: int
    ghi: float
    az0: float
    az90: float
    az180: float
    az270: float
    az0_varj: float
    az90_varj: float
    az180_varj: float
    az270_varj: float
    az0_lapi: float
    az90_lapi: float
    az180_lapi: float
    az270_lapi: float

Solar = []
Solar.append(Aurinko(0  ,975.20,486.70,914.20,1205.30,902.10,0.938,0.846,0.808,0.846,0.422,0.381,0.363,0.381))
Solar.append(Aurinko(1  ,7.9    ,5.3    ,7.5    ,17.1   ,7.9    ,0.98   ,0.86   ,0.75   ,0.86   ,0.441  ,0.387  ,0.338  ,0.387))
Solar.append(Aurinko(2  ,22.4   ,13.0   ,22.4   ,41.9   ,22.1   ,0.96   ,0.83   ,0.76   ,0.83   ,0.432  ,0.374  ,0.342  ,0.374))
Solar.append(Aurinko(3  ,69.2   ,27.9   ,66.3   ,114.2  ,71.4   ,0.96   ,0.83   ,0.8    ,0.83   ,0.432  ,0.374  ,0.36   ,0.374))
Solar.append(Aurinko(4  ,112.7  ,42.3   ,102.8  ,145.4  ,109.5  ,0.93   ,0.83   ,0.83   ,0.83   ,0.419  ,0.374  ,0.374  ,0.374))
Solar.append(Aurinko(5  ,165.5  ,81.0   ,154.3  ,182.1  ,147.9  ,0.93   ,0.85   ,0.9    ,0.85   ,0.419  ,0.383  ,0.405  ,0.383))
Solar.append(Aurinko(6  ,168.6  ,106.1  ,150.5  ,168.3  ,154.8  ,0.86   ,0.83   ,0.91   ,0.83   ,0.387  ,0.374  ,0.41   ,0.374))
Solar.append(Aurinko(7  ,175.1  ,100.3  ,163.0  ,181.5  ,157.5  ,0.9    ,0.85   ,0.91   ,0.85   ,0.405  ,0.383  ,0.41   ,0.383))
Solar.append(Aurinko(8  ,126.7  ,58.6   ,125.5  ,147.0  ,110.6  ,0.88   ,0.8    ,0.8    ,0.8    ,0.396  ,0.36   ,0.36   ,0.36))
Solar.append(Aurinko(9  ,81.2   ,28.0   ,76.6   ,119.3  ,76.6   ,0.95   ,0.83   ,0.81   ,0.83   ,0.428  ,0.374  ,0.365  ,0.374))
Solar.append(Aurinko(10 ,31.4   ,15.1   ,31.6   ,57.9   ,29.9   ,0.96   ,0.85   ,0.76   ,0.85   ,0.432  ,0.383  ,0.342  ,0.383))
Solar.append(Aurinko(11 ,10.1   ,6.2    ,9.8    ,19.6   ,9.6    ,0.96   ,0.86   ,0.73   ,0.86   ,0.432  ,0.387  ,0.329  ,0.387))
Solar.append(Aurinko(12 ,4.4    ,2.9    ,3.9    ,11.0   ,4.3    ,0.98   ,0.93   ,0.73   ,0.93   ,0.441  ,0.419  ,0.329  ,0.419))


# Energia hyötysuhde 

@dataclass
class Energialahde:
    teksti: str
    Vuosihyoty1: float
    Apulaite1: float
    Vuosihyoty2: float
    Apulaite2: float
    Polttoaine: str

Elahde = []

Elahde.append(Energialahde("Perus",0.0,0.0,0.0,0.0,"NA" ))
Elahde.append(Energialahde("Öljylämpökattila",0.81,0.99,0.9,0.24,"Kevyt pottoöljy" ))
Elahde.append(Energialahde("Kaasulämpökattila",0.81,0.59,0.9,0.11,"Kaasu" ))
Elahde.append(Energialahde("Öljykondenssikattila",0.87,1.07,0.95,0.25,"Kevyt polttoöljy" ))
Elahde.append(Energialahde("Kaasukondenssikattila",0.92,0.68,1.01,0.12,"Kaasu" ))
Elahde.append(Energialahde("Pellettikattila",0.75,0.77,0.84,0.13,"Puu" ))
Elahde.append(Energialahde("Puukattila",0.73,0.38,0.82,0.25,"Puu" ))
Elahde.append(Energialahde("Sähkölämpökattila",0.88,0.02,1.0,0.24,"Maalämpö, ym." ))
Elahde.append(Energialahde("Kaukolämpö",0.94,0.6,0.97,0.07,"Kauko tai- aluelämpö" ))
Elahde.append(Energialahde("Sähkölämmitys",1.0,0.0,1.0,0.0,"Sähkö" ))
                           
# Static values for calculations ToDo: MUUTA NÄMÄ HAETTAVAKSI TAULUKOSTA !!!!!
u_muu = 1.0
u_ksilta = 1.0

# Used global variables in calculations
q_alapohja = 0
q_ikkunat = 0
q_ovi = 0
q_yläpohja = 0
q_ulkoseina = 0
Tsp = 17
deltaT = 0.5 # deltaTpuhallus
LKV_korjaus = 0.5
huonekorkeus = 2.8
