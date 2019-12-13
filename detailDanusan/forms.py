from django import forms
from .models import ReviewModel
from django.forms import ModelForm, TextInput, Textarea

class ReviewForm(forms.Form):
    nama = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control form-custom',
            'placeholder':'Nama Kamu'
        }
    ))

    review = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control form-custom',
            'placeholder':'Review Danusan'
        }
    ))