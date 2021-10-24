from django.urls import path

from . import views


urlpatterns = [
    path('bookings/', views.my_bookings, name='my_bookings'),
    path('book/<slug:slug>/', views.book_room, name='book_room'),
]
