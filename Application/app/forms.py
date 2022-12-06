"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class BmiForm(forms.Form):
    height = forms.FloatField(
        label='請輸入身高(m)', 
        widget=forms.NumberInput(attrs={'class':'form-control'}),
        error_messages={'required': '請輸入身高'})
    weight = forms.CharField(
        label='請輸入體重(kg)', 
        widget=forms.TextInput(attrs={'class':'form-control'}),
        error_messages={'required': '請輸入體重'})