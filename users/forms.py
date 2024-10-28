from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class MeteProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['alue','rakennusvuosi', 'kayttotarkoitus','lammontuotto', 'lammonjako','varaavatulisija','tulisija_lkm','kerrosmaara','lampopumppu','ilmalampopumppu','lkv_lammitys','lkv_kierto', 'lkv_tila', 'iv_tapa', 'lto', 'lkvputken_eristys','lkv_kiertoeriste','sahkokWh','lampokWh','vesikWh','pinta_ala', 'sahkokWh', 'lampokWh', 'vesikWh','sisalampo', 'pv_vko', 'h_pv']

class LKVUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['lkv_lammitys','lkv_kierto', 'lkv_tila', 'lkvputken_eristys', 'lkv_kiertoeriste']

class LamUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['varaavatulisija','tulisija_lkm','ilmalampopumppu','lampopumppu','lammontuotto','lammonjako','lampopumppu_kpl','pumpputyyppi','sisalampo']

class IVUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['iv_tapa','lto', 'pv_vko', 'h_pv']

class KayttoUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['kul_pv_vko', 'kul_h_pv', 'val_pv_vko', 'val_h_pv']

class MeteAsuntoUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['pinta_ala','seinä_ala','ikkuna_ala', 'ovet_ala', 'yläpohja_ala','kayttotarkoitus', 'rakennusvuosi', 'kerrosmaara']
