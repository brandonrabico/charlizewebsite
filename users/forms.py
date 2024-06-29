from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser



class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'phone_number', 'email')
        