import math
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, MeteProfileUpdateForm, MeteAsuntoUpdateForm, LKVUpdateForm, KayttoUpdateForm
from .calculations import laske_lampo, laske_sahko, laske_vesi


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
#        mete_form = MeteProfileUpdateForm(request.POST)
        if form.is_valid():
#            print("POST valid register")
            form.save()
#            mete_form.save()
            print("POST save register")
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
#            print("POST redirect register")
#            print(username)
            return redirect('login', {'user':username})
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def meteProfile(request):
    if request.method == 'POST':
        mete_form = MeteProfileUpdateForm(request.POST, instance= request.user.profile)
        if request.POST.get("Cancel") == "CANC":
            messages.warning(request, f'Muutokset peruutettu!')                
            return redirect('def-calc')

        if mete_form.is_valid():
            if (request.POST.get('action') == "Energy") and (request.user.profile.pinta_ala > 0) :
                # NO REAL VALUES !!! -> REAL CALCULATION ToDo
                request.user.profile.sahkokWh = round(laske_sahko(request.user.profile) * 1,2)
                request.user.profile.lampokWh = round(laske_lampo(request.user.profile) * 1,2)
                request.user.profile.vesikWh = round(laske_vesi(request.user.profile) * 1,2)
                mete_form.save()
                messages.success(request, f'Your Mete apartment energy data has been estimated!')
            else:
                mete_form.save()
                messages.success(request, f'Mete base  values updated!')
                return redirect('def-calc')

    mete_form = MeteProfileUpdateForm(instance=request.user.profile)
    context = {
        'mete_form': mete_form
    }
    return render(request, 'users/mete_profile.html', context)    

@login_required
def LKVProfile(request):
    if request.method == 'POST':
        mete_form = LKVUpdateForm(request.POST, instance= request.user.profile)
        if mete_form.is_valid():
            mete_form.save()
            messages.success(request, f'LKV  values updated!')
            return redirect('def-calc_lkv')

    form = LKVUpdateForm(instance=request.user.profile)
    context = {
        'form': form,
        'mete' : mete_form
    }
    return render(request, 'blog/edit_calc1_lkv.html', context)    

@login_required
def KayttoProfile(request):
    if request.method == 'POST':
        mete_form = KayttoUpdateForm(request.POST, instance= request.user.profile)
        if mete_form.is_valid():
            mete_form.save()
            messages.success(request, f'Käyttö values updated!')
            return redirect('def-calc_kayt')

    form = KayttoUpdateForm(instance=request.user.profile)
    context = {
        'form': form,
        'mete' : mete_form
    }
    return render(request, 'blog/edit-calc1_kayt.html', context)    

@login_required
def meteAsunto(request):
    if request.POST.get("Cancel") == "CANC":
        messages.warning(request, f'Muutokset peruutettu!')                
        return redirect('def-calc_rak')
    elif request.method == 'POST':
        mete_form = MeteAsuntoUpdateForm(request.POST, instance= request.user.profile)
        if mete_form.is_valid():
            request.user.profile.pinta_ala = abs(request.user.profile.pinta_ala) # work arround for negative values
            if request.POST.get("action") == "Energy":
                # NO REAL VALUES !!! -> REAL CALCULATION ToDo
                request.user.profile.sahkokWh = laske_sahko(request.user.profile) * 1
                request.user.profile.lampokWh = laske_lampo(request.user.profile) * 1
                request.user.profile.vesikWh = laske_vesi(request.user.profile) * 1
                mete_form.save()
                messages.success(request, f'Your Mete apartment energy data has been estimated!')
                return redirect('def-calc_rak')
            if request.POST.get("action") == "Apartment":
                request.user.profile.seinä_ala = round((math.sqrt(request.user.profile.pinta_ala) * 2.8 * request.user.profile.kerrosmaara * 4) - ((math.sqrt(request.user.profile.pinta_ala)*2.8*request.user.profile.kerrosmaara*4)*0.15)-((math.sqrt(request.user.profile.pinta_ala)*2.8*request.user.profile.kerrosmaara*4)*0.05),2)
                request.user.profile.ikkuna_ala = round((math.sqrt(request.user.profile.pinta_ala) * 2.8 * request.user.profile.kerrosmaara * 4) * 0.15 ,2)
                request.user.profile.ovet_ala = round((math.sqrt(request.user.profile.pinta_ala) * 2.8 * request.user.profile.kerrosmaara * 4 ) * 0.05 ,2)
                request.user.profile.yläpohja_ala = request.user.profile.pinta_ala
               # request.user.profile.yläpohja_ala = round(request.user.profile.pinta_ala / request.user.profile.kerrosmaara ,2)
                if request.user.profile.pinta_ala == 0:
                    Nolla_arvoja = True
                else:
                    Nolla_arvoja = False
                mete_form.save()
                if Nolla_arvoja:
                    messages.warning(request,f'Zero values detected!')
                else:
                    messages.success(request, f'Your Mete apartment data has been estimated!')
                return redirect('def-calc_rak')
            mete_form.save()
            messages.success(request, f'Your Mete apartment data has been updated!')
            return redirect('def-calc_rak')
    else:
        mete_form = MeteAsuntoUpdateForm(instance=request.user.profile)
    context = {
        'mete_form': mete_form
    }
    return render(request, 'users/mete_asunto.html', context)    


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)