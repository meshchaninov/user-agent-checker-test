from django.urls import path
from django.contrib.auth import views
from .views import register, edit_profile


urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('registration/', register, name='registration'),
    path('edit/', edit_profile, name='edit_profile'),
]
