from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from Account.models import *


class UserRegistration(UserCreationForm):
    class Meta:
        model = ExtendedUser
        # fields = ('username', 'email', 'password1', 'password2',)
        fields = '__all__'