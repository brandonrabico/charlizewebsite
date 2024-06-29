from django.shortcuts import render, redirect, reverse
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm

@login_required
def client_dashboard(request):
    return render(request, 'users/dashboard.html')
    
class SignupView(CreateView):
    template_name = 'registration/signup.html'
    form_class = SignUpForm

    def get_success_url(self):
        return reverse('login')