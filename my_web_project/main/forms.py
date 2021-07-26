import os
from os.path import join

from django import forms
from django.conf import settings

from my_web_project.common.forms import BootstrapFormMixin
from my_web_project.main.models import Homework


class HomeworkForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Homework
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'some-class',
                }
            ),
        }


class HomeworkEditForm(HomeworkForm):

    class Meta:
        model = Homework
        fields = '__all__'
        # ne raboti readonly?
        widgets = {
            'type': forms.TextInput(
                attrs={
                    'readonly': 'readonly',
                }
            )
        }
