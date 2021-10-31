from django.urls import path

from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.account_login, name='login'),
    path('logout/', views.account_logout, name='logout'),
    path('account_verification/<uidb64>/<token>/', views.account_verification, name='account_verification'),
    path('register_complete/', views.register_complete, name='register_complete'),
    path('password_reset/', views.password_reset, name='password_reset'),
    path('password_reset_confirm/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
    path('password_reset_complete/', views.password_reset_complete, name='password_reset_complete'),
    path('password_reset_done/', views.password_reset_done, name='password_reset_done'),
]
