from django import forms


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput,
    )
    confirm_password = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput,
    )
