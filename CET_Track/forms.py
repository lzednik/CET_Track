__author__ = 'Lada'

from django.forms import forms
from models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('supervisor','office')
