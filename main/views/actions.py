from django.http import HttpResponse

def transaction_history(request):
    return HttpResponse("<h1>Історія — незабаром</h1>")