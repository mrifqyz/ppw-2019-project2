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
    # class Meta:
    #     model = Danusan
    #     fields = ['name', 'price', 'image']
    #     widgets = {
    #         'name': forms.TextInput(attrs={
    #             'class': 'form-control form-custom my-1',
    #             'placeholder': 'Nama Danusan'}),
    #         'price': forms.TextInput(attrs={
    #             'type': 'number',
    #             'class': 'form-control form-custom my-1',
    #             'placeholder': 'Harga Danusan'}),
    #         'image': forms.TextInput(attrs={
    #             'class': 'form-control form-custom my-1',
    #             'placeholder': 'Link Gambar Danusan'})
    #     }


# class DanusanForm(forms.Form):
#     nama = forms.CharField(widget=forms.TextInput(
#         attrs={
#             'class': 'form-control form-custom my-1',
#             'placeholder': 'Nama Danusan'
#         }
#     ))

#     harga = forms.CharField(widget=forms.NumberInput(
#         attrs={
#             'type': 'number',
#             'class': 'form-control form-custom my-1',
#             'placeholder': 'Hargas Danusan'
#         }
#     ))

#     image = forms.CharField(widget=forms.TextInput(
#         attrs={
#             'class': 'form-control form-custom my-1',
#             'placeholder': 'Link Gambar Danusan'
#         }
#     ))


