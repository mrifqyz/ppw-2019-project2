from django import forms
from .models import ReviewModel
from django.forms import ModelForm, TextInput, Textarea

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