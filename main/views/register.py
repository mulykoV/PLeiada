from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib import messages


def register_page(request):

    error = None

    if request.method == 'POST':
        name     = request.POST.get('name', '').strip()
        email    = request.POST.get('email', '').strip().lower()
        password = request.POST.get('password', '')

        if not name or not email or not password:
            error = 'Будь ласка, заповніть усі поля'
        elif len(password) < 6:
            error = 'Слово-пароль має бути не коротше 6 символів'
        elif User.objects.filter(username=email).exists():
            error = 'Ця поштова адреса вже використовується'
        else:
            user = User.objects.create_user(
                username=email,
                email=email,
                password=password,
                first_name=name,
            )
            login(request, user)
            return redirect('main:feed')

    return render(request, 'main/register.html', {'error': error})