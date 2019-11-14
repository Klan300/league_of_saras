from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={'class': "input-lg"}),
    )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': "input-lg"}))