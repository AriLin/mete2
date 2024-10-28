from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
from users.models import Aurinko,Pumppu,Valaisin
from .forms import AurinkoForm,PumppuForm,ValaisinForm
from users.forms import MeteProfileUpdateForm, LKVUpdateForm, IVUpdateForm, LamUpdateForm, KayttoUpdateForm


def home(request):
    context = {
        'posts': Post.objects.all(), 
        'title': 'Etusivu'
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'Yleistä'
        }

    return render(request, 'blog/about.html', context)

@login_required
def calc(request):
    return render(request, 'blog/calc1.html', {'title': 'Energialaskuri'})

@login_required
def calc_lam(request):
    return render(request, 'blog/calc_lam.html', {'title': 'Lämmitys'})

@login_required
def calc_lam_edit(request):
    if request.POST.get("Cancel") == "CANC":
        messages.warning(request, f'Muutokset peruutettu!')                
        return redirect('def-calc_lam')
    
    if request.method == 'POST':
        mete_form = LamUpdateForm(request.POST, instance= request.user.profile)
        if mete_form.is_valid():
            mete_form.save()
            messages.success(request, f'Lämmitys values updated!')
            return redirect('def-calc_lam')

    form = LamUpdateForm(instance=request.user.profile)
    context = {
        'form': form,
        'title': 'Lämmitys'
    }
    return render(request, 'blog/edit-calc1_lam.html', context)

@login_required
def calc_iv(request):
    return render(request, 'blog/calc_iv.html', {'title': 'Ilmanvaihto'})

@login_required
def calc_iv_edit(request):
    if request.POST.get("Cancel") == "CANC":
        messages.warning(request, f'Muutokset peruutettu!')                
        return redirect('def-calc_iv')
    
    if request.method == 'POST':
        mete_form = IVUpdateForm(request.POST, instance= request.user.profile)
        if mete_form.is_valid():
            mete_form.save()
            messages.success(request, f'IV  values updated!')
            return redirect('def-calc_iv')

    form = IVUpdateForm(instance=request.user.profile)
    context = {
        'form': form
    }
    return render(request, 'blog/edit-calc1_iv.html', context)    


@login_required
def calc_lkv(request):
    return render(request, 'blog/calc_lkv.html', {'title': 'Lämmin käyttövesi'})

@login_required
def calc_lkv_edit(request):
    if request.POST.get("Cancel") == "CANC":
        messages.warning(request, f'Muutokset peruutettu!')                
        return redirect('def-calc_lkv')
    
    if request.method == 'POST':
        mete_form = LKVUpdateForm(request.POST, instance= request.user.profile)
        if mete_form.is_valid():
            mete_form.save()
            messages.success(request, f'LKV  values updated!')
            return redirect('def-calc_lkv')

    form = LKVUpdateForm(instance=request.user.profile)
    context = {
        'form': form, 
        'title': 'Lämmin käyttövesi'
    }
    return render(request, 'blog/edit-calc1_lkv.html', context)    

@login_required
def calc_rak(request):
    return render(request, 'blog/calc_rak.html', {'title': 'Rakenteet'})

@login_required
def calc_kayt(request):
    return render(request, 'blog/calc_kayt.html', {'title': 'Käyttöajat'})

@login_required
def calc_kayt_edit(request):
    if request.POST.get("Cancel") == "CANC":
        messages.warning(request, f'Muutokset peruutettu!')                
        return redirect('def-calc_kayt')
    
    if request.method == 'POST':
        mete_form = KayttoUpdateForm(request.POST, instance= request.user.profile)
        if mete_form.is_valid():
            mete_form.save()
            messages.success(request, f'Käyttö values updated!')
            return redirect('def-calc_kayt')

    form = KayttoUpdateForm(instance=request.user.profile)
    context = {
        'form': form, 
        'title': 'Lämmin käyttövesi'
    }
    return render(request, 'blog/edit-calc1_kayt.html', context)    

@login_required
def calc_yht(request):
    return render(request, 'blog/calc_yht.html', {'title': 'Yhteensä'})

@login_required
def asunto(request):
    return render(request, 'users/mete_asunto.html', {'title': 'Rakennustiedot'})


@login_required
def aurinko_data(request):
#    print('REQUEST:', request.POST.get("Cancel"))
    if request.POST.get("Cancel") == "CANC":
        messages.warning(request, f'Muutokset peruutettu!')                
        return redirect('def-calc2')

    if (request.path == '/calc2/edit/' and not request.method == "POST") :
        form = AurinkoForm(instance= request.user.aurinko )
        context = {
            'form': form, 
            'title': 'Edit-Aurinkolaskuri'
        }
        return  render(request, 'blog/edit-calc2.html', context)

    if request.method == "POST":
        form = AurinkoForm(request.POST, instance= request.user.aurinko )
        if form.is_valid():
            form.save()
            try:
                messages.success(request, f'Muutoksia ei talletettu!')
            except:
                print('except haara')
                messages.warning(request, f'Muutoksia ei talletettu - tarkista arvot!')                
        return redirect('def-calc2')
    
    form = AurinkoForm(instance=request.user.aurinko)
    mete = MeteProfileUpdateForm(instance=request.user)
    
    context = {
        'form': form, 
        'mete': mete,
        'title': 'Aurinkolaskuri'
    }
    return render(request, 'blog/calc2.html', context)


@login_required
def pumppu_data(request):
    if request.POST.get("Cancel") == "CANC":
        messages.warning(request, f'Muutokset peruutettu!')                
        return redirect('def-calc3')

    if (request.path == '/calc3/edit/' and not request.method == "POST") :
        form = PumppuForm(instance= request.user.pumppu )
        context = {
            'form': form, 
            'title': 'Pumppulaskuri'
        }
        return  render(request, 'blog/edit-calc3.html', context)

    if request.method == "POST":
        form = PumppuForm(request.POST, instance= request.user.pumppu )
        if form.is_valid():
            form.save()
            try:
                messages.success(request, f'Muutokset talletettu!')
            except:
                print('except haara')
                messages.warning(request, f'Tietoja ei talletettu - tarkista arvot!')                
        return redirect('def-calc3')
    
    form = PumppuForm(instance=request.user.pumppu)
    mete = MeteProfileUpdateForm(instance=request.user)
    context = {
        'form': form, 
        'mete': mete,
        'title': 'Pumppulaskuri'
    }
    return render(request, 'blog/calc3.html', context)

@login_required
def valaisin_data(request):
    if request.POST.get("Cancel") == "CANC":
        messages.warning(request, f'Muutokset peruutettu!')                
        return redirect('def-calc4')

    if (request.path == '/calc4/edit/' and not request.method == "POST") :
        form = ValaisinForm(instance= request.user.valaisin )
        context = {
            'form': form, 
            'title': 'Valaisinlaskuri'
        }
        return  render(request, 'blog/edit-calc4.html', context)

    if request.method == "POST":
        form = ValaisinForm(request.POST, instance= request.user.valaisin )
        if form.is_valid():
            form.save()
            try:
                messages.success(request, f'Tiedot talleteetiin onnistuneesti!')
            except:
                print('except haara')
                messages.warning(request, f'Tietoja ei talletettu - tarkista arvot!')                
        return redirect('def-calc4')
    
    form = ValaisinForm(instance=request.user.valaisin)
    mete = MeteProfileUpdateForm(instance=request.user)
    context = {
        'form': form, 
        'mete': mete,
        'title': 'Pumppulaskuri'
    }
    return render(request, 'blog/calc4.html', context)

