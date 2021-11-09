from django.urls import path

from . import views


urlpatterns = [
    path('all', views.room_list, name='room_list'),
    path('<str:slug>/', views.RoomDetail.as_view(), name='room_detail'),
]
