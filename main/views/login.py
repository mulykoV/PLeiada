from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def login_page(request):

    error = None

    if request.method == 'POST':
        email    = request.POST.get('email', '').strip().lower()
        password = request.POST.get('password', '')

        if not email or not password:
            error = 'Будь ласка, заповніть усі поля'
        else:
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('main:feed')
            else:
                error = 'Невірна поштова адреса або слово-пароль'

    return render(request, 'main/login.html', {'error': error})