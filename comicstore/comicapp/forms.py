from django import forms
from .models import Available

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Available
        fields = ['email']

