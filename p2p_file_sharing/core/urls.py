from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),  # Login page
    path('upload/', views.upload_file, name='upload_file'),  # File upload page
    path('files/', views.file_list, name='file_list'),
    path('download/<int:file_id>/', views.download_file, name='download_file'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout
]
