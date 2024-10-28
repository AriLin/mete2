from django import forms
from users.models import Aurinko, Pumppu, Valaisin

# Edit forms for Aurinko
class AurinkoForm(forms.ModelForm):
    class Meta:
        model = Aurinko
        fields = ['user','korjauskerroin','paneeli_teho', 'paneelin_ala', 'tavoite_teho', 'myyntihinta', 
                  'tukiprosentti', 'lainamaara', 'lainaprosentti','huoltokulut','tammi','helmi', 'maalis',
                  'huhti','touko','kesa','heina','elo', 'syys', 'loka', 'marras', 'joulu' ]

# Edit forms for Pumppu
class PumppuForm(forms.ModelForm):
    class Meta:
        model = Pumppu
        fields = ['user','ilp_maara','ilp_teho', 'ilp_kulutuskWh', 'ilp_pinta_ala', 'ilp_vuosituotto', 'ilp_scop',
                  'ilp_laina_aika', 'ilp_lainakorko', 'ilp_huolto', 'ilp_hankintatuki', 'ilp_tukiprosentti', 'ilp_lainamaara',
                  'vilp_maara','vilp_teho','mlp_maara','mlp_teho' ]

# Edit forms for Valaisin
class ValaisinForm(forms.ModelForm):
    class Meta:
        model = Valaisin
        fields = ['user','maara','teho']

