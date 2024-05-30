from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('players/', views.players, name='players'),
    path('contact/', views.contactus, name='players'),
    path('emp', views.emp, name='employees'),
    path('show', views.show, name='show'),
    path('delete/<id>/', views.delete, name='delete'),
    path('edit/<id>', views.edit, name='edit'),
    path('update/<id>', views.update, name='update'),
]