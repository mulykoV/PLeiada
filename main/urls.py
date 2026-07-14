from django.urls import path
from main.views import (
    home_page,
    login_page,
    register_page,
    main_feed,
    user_dashboard,
    transaction_history
)

app_name = 'main'

urlpatterns = [
    path('', home_page, name='base'),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('feed/', main_feed, name='feed'),
    path('dashboard/', user_dashboard, name='dashboard'),
    path('transactions/', transaction_history, name='transactions'),
]