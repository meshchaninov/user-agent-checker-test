from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views
from .views import register, edit_profile, profile, profile_username, password_change_done


urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('registration/', register, name='registration'),
    path('edit/', edit_profile, name='edit_profile'),
    path('change-password/', views.PasswordChangeView.as_view(template_name='registration/change_password.html'), name='password_change'),
    path('profile/', profile, name='profile'),
    path('profile/<username>', profile_username, name='profile_username'),
    path('password-change-done', password_change_done, name='password_change_done')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
