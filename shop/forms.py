from django.forms import ModelForm
from django.contrib.auth.models import User

class UserRegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserLoginForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
