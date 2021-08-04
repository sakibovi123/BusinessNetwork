from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm


from Account.models import *


class UserRegistration(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')


class UserExtendedInfo(ModelForm):
    class Meta:
        model = ExtendedUser
        fields = ('country', 'city', 'sex', 'birthdate', 'profile_picture')