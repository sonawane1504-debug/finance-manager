from dataclasses import fields
from django import forms
from django.forms import widgets
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['title', 'amount', 'type']
        #We add 'widgets' to make it look good with Bootstrap later
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'What did you spend on?'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Amount'}),
            'type': forms.Select(attrs={'class': 'form-control'})
        }