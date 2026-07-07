from django.http import HttpResponse

def user_dashboard(request):
    return HttpResponse("<h1>Бюро — незабаром</h1>")