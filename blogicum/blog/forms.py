from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()


class UserForm(forms.UserForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
