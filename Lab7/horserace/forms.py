from django import forms
from horserace import models
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class UserAuthForm(forms.Form):
    username = forms.CharField(label='', min_length=5, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Логин'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))

    def clean(self):
        cleaned_data = super(UserAuthForm, self).clean()
        if not self.errors:
            user = authenticate(username=cleaned_data['username'], password=cleaned_data['password'])
            if user is None:
                raise forms.ValidationError('Логин или пароль неправильные')
            self.user = user
        else:
            print(self.errors)
        return cleaned_data

    def get_user(self):
        return self.user or None


class UserRegForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email', 'username', 'last_name', 'first_name', 'password']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Логин'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}),
            }
        labels ={
            'email': _(''),
            'username': _(''),
            'password': _(''),
            'last_name': _(''),
            'first_name': _(''),
        }
        help_texts = {
            'username': _('')
        }

    password_check = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Повторите пароль'}),
        min_length=8,
        label=u''
    )

    def clean_username(self):
        username = self.cleaned_data.get('username', '')

        try:
            u = User.objects.get(username=username)
            raise forms.ValidationError(u'Пользователь с таким логином уже существует')
        except User.DoesNotExist:
            return username

    def clean(self):
        p1 = self.cleaned_data.get('password', '')
        p2 = self.cleaned_data.get('password_check', '')
        if p1 != p2:
            raise forms.ValidationError(u'Введённые пароли не совпадают')

    def save(self):
        data = self.cleaned_data
        user = User()
        user.username = data['username']
        user.set_password(data['password'])
        user.email = data['email']
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.is_active = True
        user.is_superuser = False
        user.save()
        return user