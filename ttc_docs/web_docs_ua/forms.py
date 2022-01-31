from django import forms
from web_docs.models import *


class ReviewsForm(forms.ModelForm):
    auth = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
        label="Ім'я", required=True
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
        label="email", required=True
    )
    message = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
        label="Повідомлення", required=True
    )

    class Meta:
        model = Reviews
        fields = ('auth', 'email', 'message')


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
        label="Ім'я", required=True
    )
    phone = forms.IntegerField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'номер без "+"'}),
        label="Телефон", required=True
    )
    message = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
        label="Повідомлення", required=True
    )

    class Meta:
        model = Contact
        fields = ('first_name', 'phone', 'message')