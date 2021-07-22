from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from my_web_project.main.models import Student, Teacher


class StudentRegisterForm(forms.ModelForm):
    class Meta:
        model = Student
        #fields = '__all__'
        exclude = ('user',)


class TeacherRegisterForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        exclude = ('user',)


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class LoginForm(forms.Form):
    user = None
    username = forms.CharField(max_length=30,)

    password = forms.CharField(
        max_length=15,
        widget=forms.PasswordInput(),
    )

    def clean(self):
        self.user = authenticate(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
        )

        if not self.user:
            raise ValidationError('Incorrect username and/or passworord ')

    def save(self):
        return self.user
