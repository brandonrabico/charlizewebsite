from django.urls import path,include
from django.contrib.auth.views import LoginView, LogoutView
from .views import client_dashboard, SignupView, appointment_list

urlpatterns = [
    path('dashboard/', client_dashboard, name='dashboard'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('list/', appointment_list, name='appointment_list'),
]

