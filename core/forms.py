from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Utilisateur

class RegistrationForm(UserCreationForm):
    phone = forms.CharField(max_length=20, required=False)
    adresse = forms.CharField(widget=forms.Textarea, required=False)
    date_naissance = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2100)), required=False)
    bio = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Utilisateur
        fields = ('username', 'phone', 'adresse', 'date_naissance', 'bio', 'password1', 'password2')
