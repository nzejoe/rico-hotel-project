from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('account/register/', views.register, name='register'),
    path('account/account_login/', views.account_login, name='account_login'),
    path('account/account_logout/', views.account_logout, name='account_logout'),
    path('account/register_complete/', views.register_complete, name='register_complete'),
]
