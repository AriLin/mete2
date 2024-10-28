from dataclasses import dataclass

@dataclass
class Sääalue:
    kk: str
    A: []

säätaulu = []

säätaulu.append(Sääalue("keskiarvo", [6.96, 5.33, 4.1771, 1.533]))
säätaulu.append(Sääalue("tammikuu", [-2.04, -4.92, -7.875, -11]))
säätaulu.append(Sääalue("helmikuu", [-1.5, -3.76, -5.725, -10.5]))
säätaulu.append(Sääalue("maaliskuu", [3.1, -0.78, -2.425, -3.6]))
säätaulu.append(Sääalue("huhtikuu", [3.52, 1.56, 1.1, -0.15]))
säätaulu.append(Sääalue("toukokuu", [9.36, 9.3, 8.35, 6.16]))
säätaulu.append(Sääalue("kesäkuu", [16.6, 16.24, 15.525, 13.65]))
säätaulu.append(Sääalue("heinäkuu", [17.6, 17.36, 17.525, 16.05]))
säätaulu.append(Sääalue("elokuu", [18.32, 17.66, 16.775, 14.45]))
säätaulu.append(Sääalue("syyskuu", [9.22, 8.66, 8.45, 6.65]))
säätaulu.append(Sääalue("lokakuu", [6.36, 6.36, 5.25, 2.05]))
säätaulu.append(Sääalue("marraskuu", [3.14, 0.8, -1.375, -4.9]))
säätaulu.append(Sääalue("joulukuu", [-2.7, -4.58, -5.45, -10.45]))

#print (säätaulu[0].kk,"Alue3:",säätaulu[0].A[1])

# Static values for calculations
u_ulkoseinä = 0.17
u_yläpohja = 0.09
u_alapohja = 0.16
u_ikkuna = 1.0
u_ovi = 1.0
u_muu = 1.0
u_ksilta = 1.0




def laske_sahko(lahtoarvot):
    # lahtoarvot = user.profile
    return(1234)

def laske_lampo(lahtoarvot):
    # lahtoarvot = user.profile
    return(1234)

def laske_vesi(lahtoarvot):
    # lahtoarvot = user.profile
    return(1234)

def laske_Q_ulkoseina(lahtoarvot):
    # lahtoarvot = user.profile
    if lahtoarvot.seinä_ala == 0:
        m_ukoseina = lahtoarvot.pinta_ala * 1.08
    else:
        m_ukoseina = lahtoarvot.seinä_ala

    t_ulko = säätaulu[0].A[lahtoarvot.alue]
    q_ulkoseina = u_ulkoseinä * m_ukoseina * (21 -t_ulko) *8760
    print(q_ulkoseina)
