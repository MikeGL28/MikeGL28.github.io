from django.contrib.auth import login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserLoginForm
from django.contrib import messages
from .models import URL
from rest_framework.viewsets import ModelViewSet
from .serializers import URLSerializer


@login_required(login_url='login')
def home(request):
    form = URL.objects.all()
    return render(request, 'urlapp/home.html', {'form': form})


class URLViewSet(ModelViewSet):
    queryset = URL.objects.all()
    serializer_class = URLSerializer


def post_detail(request, pk):
    return render(request, 'home.html', {
        'route': get_object_or_404(URL, pk=id)
    })


def add_url(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        full_url = request.POST.get('full_url')
        obj = URL.create(full_url, title)
        return render(request, 'urlapp/add_url.html', {
            'title': title,
            'full_url': full_url,
            'short_url': f'{request.get_host()}/{obj.short_url}'
        })
    return render(request, 'urlapp/add_url.html')


def route_to_url(request, key):
    try:
        obj = URL.objects.get(short_url=key)
        return redirect(obj.full_url)
    except:
        return redirect(home)


def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались!')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации!')
    else:
        form = UserRegisterForm()
    return render(request, 'urlapp/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'urlapp/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')
