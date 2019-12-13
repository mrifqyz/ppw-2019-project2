from django.forms import ModelForm, Form
from django import forms
from .models import Danusan


class DanusanForm(ModelForm):
    class Meta:
        model = Danusan
        fields = ['name', 'price', 'image']
        widgets = {
		    'name': forms.TextInput(attrs={
		    'class': 'form-control',
		    'id': 'name'}),
		    'price': forms.TextInput(attrs={
		    'type' : 'number',
		    'class': 'form-control',
		    'id': 'price'}),
            'image': forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'image'}),
            
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewModel
        fields = ['Nama','Review']
        widgets = {
            'Nama': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Nama kamu siapa?', 
                'cols': 100, 
                'rows': 1}),
            'Review': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Tulis ulasan kamu disini..', 
                'cols': 500, 
                'rows': 50}),
        }

