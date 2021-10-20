from django.urls import path

from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.account_login, name='login'),
    path('logout/', views.account_logout, name='logout'),
    path('register_complete/', views.register_complete, name='register_complete'),
]
