from django import forms
from .models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class UserAdminCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('full_name', 'email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('full_name', 'email', 'password', 'active', 'admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

class RegisterForm(forms.Form):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    username = forms.CharField(label='E-mail', widget=forms.EmailInput(
        attrs={
            'class':'form-control form-custom',
            'placeholder':'E-mail' 
        }
    ))

    fullname = forms.CharField(label='Full Name', widget=forms.TextInput(
        attrs={
            'class':'form-control form-custom',
            'placeholder':'Full name' 
        }
    ))

    bio = forms.CharField(label='Bio', max_length=1000, widget=forms.TextInput(
        attrs={
            'class':'form-control form-custom',
            'placeholder':'Bio' 
        }
    ))

    phone = forms.CharField(label='Phone Number', min_length=8, widget=forms.TextInput(
        attrs={
            'class':'form-control form-custom',
            'placeholder':'Phone Number' 
        }
    ))

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={
            'class':'form-control form-custom',
            'placeholder':'Password' 
        }
    ))

    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(
        attrs={
            'class':'form-control form-custom',
            'placeholder':'Re-type Password' 
        }
    ))

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

class LoginForm(forms.Form):
    """Form for user login. Includes username for login and password
    for login. Also created function to test password length"""

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control form-custom',
            'placeholder':'Email'
        }
    ))

    password = forms.CharField(min_length=8, widget=forms.PasswordInput(
        attrs={
            'class':'form-control form-custom',
            'placeholder':'Password'
        }
    ))

    def checkPassword(self):
        password = self.cleaned_data.get('password')
        if(len(password)<8):
            return False
        return True

        