from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from catalog.forms import StyleFormMixin
from users.models import User
from django.utils.crypto import get_random_string

class UserRegisterForm(UserCreationForm, StyleFormMixin):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        if not user.verification_key:
            user.verification_key = get_random_string(length=19)
        if commit:
            user.save()
        return user

class UserProfileForm(UserChangeForm, StyleFormMixin):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'avatar', 'country')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()
