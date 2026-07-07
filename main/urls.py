from django.contrib import admin
from django.urls import path
from main.views import (
    home_page,
    login_page,
    register_page,
    main_feed,
    user_dashboard,
    transaction_history,
)
from main.views.feed import create_post, toggle_like

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('feed/', main_feed, name='feed'),
    path('dashboard/', user_dashboard, name='dashboard'),
    path('transactions/', transaction_history, name='transactions'),
    path('create-post/', create_post, name='create_post'),
    path('like/<int:post_id>/', toggle_like, name='toggle_like'),
]