from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    """
    Login form
    """

    username = forms.CharField(required=True,
                               widget=forms.TextInput
                               (attrs=
                                {'placeholder': "Nom d'utilisateur",
                                 'class': "form-control form-control-user"
                                 }))

    password = forms.CharField(strip=False,
                               widget=forms.PasswordInput
                               (attrs=
                                {'autocomplete': 'current-password',
                                 'class': "form-control form-control-user",
                                 'placeholder': "Mot de passe"}))


class UserRegistrationForm(forms.ModelForm):
    """
    Subscription form
    """

    class Meta:
        model = User
        fields = ('username',)

    username = forms.CharField(label='',

                               widget=forms.TextInput
                               (attrs=
                                {'placeholder': "Nom d'utilisateur",
                                 'class': "form-control form-control-user"}))

    password = forms.CharField(label='',
                               strip=False,
                               widget=forms.PasswordInput
                               (attrs=
                                {'placeholder': "Mot de passe",
                                 'class': "form-control form-control-user"}))
    password2 = forms.CharField(label='',
                                widget=forms.PasswordInput
                                (attrs=
                                 {'placeholder': "Répétez votre mot de passe",
                                  'class': "form-control form-control-user"}))

    def clean_password2(self):
        """
        Check if password are identical ; if its not, clean
        """

        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Les mots de passes ne sont pas identiques.')
        return cd['password2']
