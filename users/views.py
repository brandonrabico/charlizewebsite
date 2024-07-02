from django.shortcuts import render, redirect, reverse
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from appointment.models import Appointment

@login_required
def client_dashboard(request):
    appointments = Appointment.objects.all()
    context = {'appointments': appointments}
    return render(request, 'dashboard.html', context)
    
class SignupView(CreateView):
    template_name = 'registration/signup.html'
    form_class = SignUpForm

    def get_success_url(self):
        return reverse('login')
    
def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointment_list.html', {'appointments': appointments})