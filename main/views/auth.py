from django.http import HttpResponse
def login_page(request): return HttpResponse("Вхід")
def register_page(request): return HttpResponse("Реєстрація")