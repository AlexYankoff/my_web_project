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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['score'].disabled = True
        self.fields['status'].disabled = True

class HomeworkEditForm(HomeworkForm):
    class Meta:
        model = Homework
        fields = '__all__'



class HomeworkCheckForm(HomeworkForm):
    class Meta:
        model = Homework
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['score'].disabled = False
        self.fields['status'].disabled = False


