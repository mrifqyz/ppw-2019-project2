from django.forms import ModelForm
from django import forms
from .models import Danusan

class DanusanForm(ModelForm):
	class Meta:
		model = Danusan
		fields = ['name', 'price', 'image']
		widgets = {
			'name': forms.TextInput(attrs={
				'class': 'form-control'}),
			'price': forms.TextInput(attrs={
				'type' : 'number',
				'class': 'form-control'}),
            'image': forms.TextInput(attrs={
                'class': 'form-control'})
		}
