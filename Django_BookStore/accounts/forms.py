# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'age', 'email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove help_text for fields
        for field_name in self.fields:
            self.fields[field_name].help_text = ''


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ('username', 'age', 'email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove help_text for fields
        for field_name in self.fields:
            self.fields[field_name].help_text = ''
