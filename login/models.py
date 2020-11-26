from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator
# Create your models here.
class UserData(models.Model):
    UserName = models.CharField(max_length = 15, blank = False, validators = [
        RegexValidator(regex='^[a-zA-Z0-9]*$', message = 'Username must be alphanumeric', code = 'invalid_username')
    ])
    PhoneNumber = models.CharField(max_length = 10, blank = False, validators = [
        RegexValidator(regex='^[0-9]*$', message = 'Please enter a valid phone number', code = 'invalid_phonenumber')
    ])
    Password = models.CharField(max_length=15, blank = False, validators = [
        MinLengthValidator(8)
    ])
    Email = models.EmailField()


