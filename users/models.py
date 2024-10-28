import enum
from django.db import models
from django_choices_field import IntegerChoicesField
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from PIL import Image



class Aurinko(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
#    katto_ala = models.FloatField(default = 0.0, help_text = 'Rakennuksen katon pinta-ala')
#    maara = models.IntegerField(default = 1, help_text ='Käytettävien paneleiden määrä')
#    teho = models.IntegerField(default = 240, help_text ='Paneleiden yhteisteho (W)')
# uudet kentät    
    korjauskerroin = models.FloatField(default = 1, help_text ='Suoraan aurinkoa kohti = 1, Pois auringosta = 0', verbose_name="")
    paneeli_teho = models.FloatField(default = 0.35, help_text = 'Yhden paneelin huipputeho kWp', verbose_name="")
    paneelin_ala = models.FloatField(default = 1.7, help_text = 'Yhden paneelin pinta-ala m2', verbose_name="")
    tavoite_teho = models.FloatField(default = 8.0, help_text = 'Paneeliston haluttu huipputeho kW', verbose_name="")
    myyntihinta = models.IntegerField(default = 5, help_text = 'Aurinkosähkön myyntihinta verkkoon snt/kWh', verbose_name="")
    tukiprosentti = models.FloatField(default = 0, help_text = 'Investointitukiprosentti %', verbose_name="")
    lainamaara = models.IntegerField(default = 12000, help_text ='Investointilainan määrä €', verbose_name="")
    lainaprosentti = models.FloatField(default = 2.0, help_text ='Lainaprosentti %', verbose_name="")
    huoltokulut = models.IntegerField(default = 50, help_text = 'Vuosittainen hoito/huolto kustannnus €', verbose_name="")
    tammi = models.FloatField(default = 5000, help_text ='Tammikuun sähkönkulutus kWh', verbose_name="")
    helmi = models.FloatField(default = 4000, help_text ='Helmikuun sähkönkulutus kWh', verbose_name="")
    maalis = models.FloatField(default = 3000, help_text ='Maaliskuun sähkönkulutus kWh', verbose_name="")
    huhti = models.FloatField(default = 3000, help_text ='Huhtikuun sähkönkulutus kWh', verbose_name="")
    touko = models.FloatField(default = 2000, help_text ='Toukokuun sähkönkulutus kWh', verbose_name="")
    kesa = models.FloatField(default = 1000, help_text ='Kesäkuun sähkönkulutus kWh', verbose_name="")
    heina = models.FloatField(default = 1000, help_text ='Heinäkuun sähkönkulutus kWh', verbose_name="")
    elo = models.FloatField(default = 2000, help_text ='Elokuun sähkönkulutus kWh', verbose_name="")
    syys = models.FloatField(default = 2000, help_text ='Syyskuun sähkönkulutus kWh', verbose_name="")
    loka = models.FloatField(default = 3000, help_text ='Lokakuun sähkönkulutus kWh', verbose_name="")
    marras = models.FloatField(default = 4000, help_text ='Marraskuun sähkönkulutus kWh', verbose_name="")
    joulu = models.FloatField(default = 5000, help_text ='Joulukuun sähkönkulutus kWh', verbose_name="")

    def __str__(self) -> str:
        return super().__str__()

class Pumppu(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ilp_maara = models.IntegerField(default = 1, help_text ='Käytettävien ILP määrä', verbose_name="")
    ilp_teho = models.IntegerField(default = 1, help_text ='ILP teho (W)', verbose_name="")
    ilp_kulutuskWh = models.FloatField(default = 1000.1, help_text ='Kiinteistön vuosikulutus', verbose_name="")
    ilp_pinta_ala = models.FloatField(default = 120.1, help_text = 'ILP Lämmitettävä pinta-ala', verbose_name="")
    ilp_vuosituotto = models.FloatField(default = 1000.2, help_text ='ILP Energiamerkinnän vuositutotto', verbose_name="")
    ilp_scop = models.FloatField(default = 2.8, help_text = 'ILP Energiamerkinnän SCOP', verbose_name="")
    ilp_hankintatuki = models.BooleanField(default = False, help_text = 'Hankintatuki käytettävissä', verbose_name="")
    ilp_tukiprosentti = models.FloatField(default = 15.0, help_text = 'Hankintatuki %', verbose_name="")
    ilp_lainamaara = models.FloatField(default = 1000.0, help_text = 'Käytety lainamäärä', verbose_name="")
    ilp_laina_aika = models.IntegerField(default = 5, help_text = 'Lainan maksuaika vuosia', verbose_name="")
    ilp_lainakorko = models.FloatField(default = 2.0, help_text = 'Lainan korko %', verbose_name="")
    ilp_huolto = models.FloatField(default = 50.0, help_text = 'Vuosittaiset huoltokustannukset', verbose_name="")

    vilp_maara = models.IntegerField(default = 1, help_text ='Käytettävien VLP määrä', verbose_name="")
    vilp_teho = models.IntegerField(default = 1, help_text ='VILP:n yhteisteho (W)', verbose_name="")
    mlp_maara = models.IntegerField(default = 1, help_text ='MLP kaivojen määrä', verbose_name="")
    mlp_teho = models.IntegerField(default = 1, help_text ='MLP:n yhteisteho (W)', verbose_name="")

    def __str__(self) -> str:
        return super().__str__()

class Valaisin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    maara = models.IntegerField(default = 1, help_text ='Käytettävien valaisimien määrä', verbose_name="")
    teho = models.IntegerField(default = 240, help_text ='Valaisimien käyttämä teho (W)', verbose_name="")

    def __str__(self) -> str:
        return super().__str__()

class Profile(models.Model):
    class MeteAreas(models.IntegerChoices):
        Area1 = 1, "Alue 1"
        Area2 = 2, "Alue 2"
        Area3 = 3, "Alue 3"
        Area4 = 4, "Alue 4"

    class MeteHeating(models.IntegerChoices):
        KAUKOLÄMPÖ = 1, "Kaukolämpö"
        SÄHKÖ = 2, "Sähkö"
        MAALÄMPÖ = 3, "Maalämpö"
        ÖJY = 4, "Öjy"
        IVLP = 5, "IVLP + sähkö"
        PILP = 6, "PILP + sähkö"
        PELLETTI = 7, "Pelletti"
        ÖPILP = 8,"IVLP + Öljy"

    class Kayttotarkoitus(models.IntegerChoices):
        LUOKKA1 = 1, "Pientalo"
        LUOKKA2 = 2, "Kerrostalo"
        LUOKKA3 = 3, "Toimisto"
        LUOKKA4 = 4, "Liiketila"
        LUOKKA5 = 5, "Majoitus"
        LUOKKA6 = 6, "Opetus"
        LUOKKA7 = 7, "Liikunta"
        LUOKKA8 = 8, "Sairaala"

    class Rakennuslupavuosi(models.IntegerChoices):
        RLVUOSI1 = 1, "-1969"
        RLVUOSI2 = 2, "1969-1976"
        RLVUOSI3 = 3, "1976-1978"
        RLVUOSI4 = 4, "1978-1985"
        RLVUOSI5 = 5, "1985-10/2003"
        RLVUOSI6 = 6, "10/2003-2008"
        RLVUOSI7 = 7, "2008-2010"
        RLVUOSI8 = 8, "2010-2012"
        RLVUOSI9 = 9, "2012-2018"
        RLVUOSI10 = 10, "2018-"

    class Lammontuotto(models.IntegerChoices):
        LTUOTTO1 = 1, "Öljylämpökattila"
        LTUOTTO2 = 2, "Kaasulämpökattila"
        LTUOTTO3 = 3, "Öljykondenssikattila"
        LTUOTTO4 = 4, "Kaasukondenssikattila"
        LTUOTTO5 = 5, "Pellettikattila"
        LTUOTTO6 = 6, "Puukattila"
        LTUOTTO7 = 7, "Sähkölämpökattila"
        LTUOTTO8 = 8, "Kaukolämpö"
        LTUOTTO9 = 9, "Sähkölämmitys"

    class Lammonjako(models.IntegerChoices):
        LJAKO1 = 1, "Vesipatteri 45/35"
        LJAKO2 = 2, "Vesipatteri 70/40"
        LJAKO3 = 3, "Vesipatteri 90/70"
        LJAKO4 = 4, "Vesipatteri 70/40 jakotukilla"
        LJAKO5 = 5, "Vesipatteri 45/35 jakotukilla"
        LJAKO6 = 6, "Lattia vesilammitys 40/30"
        LJAKO7 = 7, "Kattolämmitys (sähkö)"
        LJAKO8 = 8, "Ikkunalämmitys (sähkö)"
        LJAKO9 = 9, "ILmanvaihtolämmitys"
        LJAKO10 = 10, "Sähköpatterit"
        LJAKO11 = 11, "Lattialämmitys (sähkö)"
        LJAKO12 = 12, "Muut lämmitystavat"
        
    class Lkv_heat(models.IntegerChoices):
        LKV_HEAT1 = 1, "Öljylämpökattila"
        LKV_HEAT2 = 2, "Kaasulämpökattila"
        LKV_HEAT3 = 3, "Öljykondenssikattila"
        LKV_HEAT4 = 4, "Kaasukondenssikattila"
        LKV_HEAT5 = 5, "Pellettikattila"
        LKV_HEAT6 = 6, "Puukattila"
        LKV_HEAT7 = 7, "Sähkölämpökattila"
        LKV_HEAT8 = 8, "Kaukolämpö"
        LKV_HEAT9 = 9, "Sähkölämmitys"

    class Ilmanvaitotapa(models.IntegerChoices):
        IV_TAPA1 = 1, "Painovoimainen"
        IV_TAPA2 = 2, "Koneellinen poisto"
        IV_TAPA3 = 3, "Koneellinen tulo-poisto"

    class Lp_tyyppi(models.IntegerChoices):
        LP_TAPA1 = 1, "MLP"
        LP_TAPA2 = 2, "IVLP"
        LP_TAPA3 = 3, "PILP"

    class LKV_Kiertoeriste(models.IntegerChoices):
        KERISTE0 = 0, "Ei tietoa"
        KERISTE1 = 1, "0.5 D"
        KERISTE2 = 2, "1.5 D"
        KERISTE3 = 3, "Suojaputki"
        KERISTE4 = 4, "Suojaputki + 0.5 D"
        KERISTE5 = 5, "Suojaputki + 1.5 D"
    
    class Putkieriste(models.IntegerChoices):
        ERISTE1 = 1, "40mm"
        ERISTE2 = 2, "100mm"
        ERISTE3 = 3, "muu paksuus"
    
    class LKV_tilavuus(models.IntegerChoices):
        LKV_0 = 0, "0 l"
        LKV_1 = 1, "50 l"
        LKV_2 = 2, "100 l"
        LKV_3 = 3, "150 l"
        LKV_4 = 4, "200 l"
        LKV_5 = 5, "300 l"
        LKV_6 = 6, "500 l"
        LKV_7 = 7, "1000 l"
        LKV_8 = 8, "2000 l"
        LKV_9 = 9, "4000 l"

    class H_PV(models.IntegerChoices):
        Hpv1 = 1, "1h/pv"
        Hpv2 = 2, "2h/pv"
        Hpv3 = 3, "3h/pv"
        Hpv4 = 4, "4h/pv"
        Hpv5 = 5, "5h/pv"
        Hpv6 = 6, "6h/pv"
        Hpv7 = 7, "7h/pv"
        Hpv8 = 8, "8h/pv"
        Hpv9 = 9, "9h/pv"
        Hpv10 = 10, "10h/pv"
        Hpv11 = 11, "11h/pv"
        Hpv12 = 12, "12h/pv"
        Hpv13 = 13, "13h/pv"
        Hpv14 = 14, "14h/pv"
        Hpv15 = 15, "15h/pv"
        Hpv16 = 16, "16h/pv"
        Hpv17 = 17, "17h/pv"
        Hpv18 = 18, "18h/pv"
        Hpv19 = 19, "19h/pv"
        Hpv20 = 20, "20h/pv"
        Hpv21 = 21, "21h/pv"
        Hpv22 = 22, "22h/pv"
        Hpv23 = 23, "23h/pv"
        Hpv24 = 24, "24h/pv"

    class P_VKO(models.IntegerChoices):
        Pvko1 = 1, "1pv/vko"
        Pvko2 = 2, "2pv/vko"
        Pvko3 = 3, "3pv/vko"
        Pvko4 = 4, "4pv/vko"
        Pvko5 = 5, "5pv/vko"
        Pvko6 = 6, "6pv/vko"
        Pvko7 = 7, "7pv/vko"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
# user = models.BooleanField(default ='1')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    alue = IntegerChoicesField(choices_enum = MeteAreas, default = 1, help_text = 'Kiinteistön alueellinen sijainti <a href="https://www.hamk.fi/">HAKU</a>', verbose_name="")  #possible values 1= area1, 2 =area2, 3 = area 3&4
#    aluetuki = models.BooleanField(default = False, help_text = 'Tukimuoto käytettävissä?') #Possible values: True = aluetuki saatavilla, False = ei aluetukea
    kayttotarkoitus = IntegerChoicesField(choices_enum = Kayttotarkoitus, default = 1, help_text = 'Kiinteistön käyttötarkoitus', verbose_name="")
    rakennusvuosi = IntegerChoicesField(choices_enum = Rakennuslupavuosi, default = 1, help_text = 'Vuosi jolloin rakennuslupa tullut vireille', verbose_name="")
    lammontuotto = IntegerChoicesField(choices_enum = Lammontuotto, default = 1, help_text = 'Kiinteistön lämmöntuottojärjestelmä', verbose_name="") 
    lammonjako = IntegerChoicesField(choices_enum = Lammonjako, default = 1, help_text = 'Kiinteistön lämmönjako tapa', verbose_name="") 
    varaavatulisija = models.BooleanField(default = False, help_text='Varaava tulisija käytettävissä', verbose_name="")
    tulisija_lkm = models.IntegerField(default = 0, help_text='Varaavien tulisijojen määrä', verbose_name="")
    kerrosmaara = models.IntegerField(default = 1, help_text = 'Kiinteistön kerrosten määrä', verbose_name="")
    sisalampo = models.FloatField(default = 20.0, help_text = 'Sisälämpötila 0.5 asteen tarkkuudella', verbose_name="")
    lampopumppu = models.BooleanField(default = False, help_text='Lämpöpumppu käytettävissä', verbose_name="")
    lampopumppu_kpl = models.IntegerField(default = 1, help_text = 'Lämpöpumppujen  määrä', verbose_name="")
    pumpputyyppi = IntegerChoicesField(choices_enum= Lp_tyyppi, default=1, help_text='Lämpöpumpun toimintatapa', verbose_name="")
    ilmalampopumppu = models.BooleanField(default = False, help_text='Ilmalämpöpumppu käytettävissä', verbose_name="")
    lkv_lammitys = IntegerChoicesField(choices_enum= Lkv_heat, default=1, help_text='Lämpimän käyttöveden lämmitysratkaisu', verbose_name="")
    lkv_kierto = models.BooleanField(default = True, help_text='Lämpimän käyttöveden kierto', verbose_name="")
    lkv_kiertoeriste = IntegerChoicesField(choices_enum= LKV_Kiertoeriste, default= 1, help_text='Lkv kiertojohdon eriste', verbose_name="")
    lkv_tila = IntegerChoicesField(choices_enum= LKV_tilavuus, default= 4, help_text='Lkv varaajan tilavuus', verbose_name="")
    iv_tapa = IntegerChoicesField(choices_enum= Ilmanvaitotapa, default=1, help_text='Ilmanvaihdon toteutustapa', verbose_name="")
    lto = models.BooleanField(default = True, help_text='Poistoilman lämmöntalteeotto käytössä', verbose_name="")
    lkvputken_eristys = IntegerChoicesField(choices_enum= Putkieriste, default=1, help_text='LKV varaajan eristepaksuus', verbose_name="")
    sahkokWh = models.FloatField(default = 0.0, help_text = 'Vuotuinen sähköenergian kulutus', verbose_name="")
    lampokWh = models.FloatField(default = 0.0, help_text = 'Vuotuinen lämmitysenergian kulutus', verbose_name="")
    vesikWh = models.FloatField(default = 0.0, help_text = 'Vuotuinen vedenlämmityksenergian kulutus', verbose_name="")
#    lammitystapa = IntegerChoicesField(choices_enum = MeteHeating, default = 2, help_text = 'Rakennuksen pääasiallinen lämmitysmuoto') #Possible values : 1= Sähkö, 2= kaukolämpö, 3= öljy&kaasu, 4=uusiutuva
    pinta_ala = models.FloatField(default = 10.0, help_text = 'Rakennuksen alapohjan pinta-ala', verbose_name="")
    seinä_ala = models.FloatField(default = 0.0, help_text = 'Rakennuksen ulkoseinien pinta-ala', verbose_name="")
    ikkuna_ala = models.FloatField(default = 0.0, help_text = 'Rakennuksen ikkunoiden pinta-ala', verbose_name="")
    ovet_ala = models.FloatField(default = 0.0, help_text = 'Rakennuksen ulko-ovien pinta-ala', verbose_name="")
    yläpohja_ala = models.FloatField(default = 0.0, help_text = 'Rakennuksen yläpohjan pinta-ala', verbose_name="")
    pv_vko = IntegerChoicesField(choices_enum= P_VKO, default=5, help_text='Ilmanvaihto käytössä päivää/viikossa', verbose_name="")
    h_pv = IntegerChoicesField(choices_enum= H_PV, default=8, help_text='Ilmanvaihto käytössä tuntia/päivässä', verbose_name="")
    kul_pv_vko = IntegerChoicesField(choices_enum= P_VKO, default=5, help_text='Kuluttajalaitteet käytössä päivää/viikossa', verbose_name="")
    kul_h_pv = IntegerChoicesField(choices_enum= H_PV, default=8, help_text='Kuluttajalaittet käytössä tuntia/päivässä', verbose_name="")
    val_pv_vko = IntegerChoicesField(choices_enum= P_VKO, default=5, help_text='Valaistus käytössä päivää/viikossa', verbose_name="")
    val_h_pv = IntegerChoicesField(choices_enum= H_PV, default=8, help_text='Valaistus käytössä tuntia/päivässä', verbose_name="")

#    asukkaita = models.IntegerField(default = 4, help_text = 'Asukkaiden määrä')
    date_modified = models.DateTimeField(auto_now = True, verbose_name="")


    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


