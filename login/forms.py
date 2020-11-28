from django.forms import ModelForm
from .models import UserData

class UserForm(ModelForm):
    class Meta:
        model = UserData
        fields = ['user_name', 'password', 'phone_number', 'email', 'home', 'professional']