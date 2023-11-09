from django.urls import path
from . import views 
urlpatterns = [
    path('', views.Home, name="Home"), 
    path('Room/', views.room, name="room"),
    path('Roomsss/<str:pk>/', views.RoomSpeci, name='room'),
    path('Room/create/', views.createRoom, name='createRoom'),
    path('Room/update/<str:pk>/', views.updateRoom, name='updateRoom'),
    path('Room/delete/<str:pk> /', views.deleteRoom, name='delete'),
]

