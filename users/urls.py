from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('', views.registration, name='registration'),
    path('profile/<str:username>/', views.UserProfileView.as_view(), name='profile'),
    path('profile/<str:username>/edit/', views.ProfileUpdateView.as_view(), name='profile_edit'),
]