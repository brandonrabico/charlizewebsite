from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import client_dashboard, SignupView

urlpatterns = [
    path('dashboard/', client_dashboard, name='dashboard'),
    path('signup/', SignupView.as_view(), name='signup'),
]

