from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views
from .views import register, edit_profile, profile


urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('registration/', register, name='registration'),
    path('edit/', edit_profile, name='edit_profile'),
    path('password/', views.PasswordChangeView.as_view(template_name='registration/change_password.html'), name='change_password'),
    path('profile/', profile, name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
