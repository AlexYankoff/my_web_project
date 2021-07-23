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
        #exclude = ('student',)
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'some-class',
                }
            ),
        }


class HomeworkEditForm(HomeworkForm):
    def save(self, commit=True):
        db_homework = Homework.objects.get(pk=self.instance.id)
        if commit:
            image_path = join(settings.MEDIA_ROOT, str(db_homework.image))
            os.remove(image_path)
        return super().save(commit)

    class Meta:
        model = Homework
        fields = '__all__'
        widgets = {
            'type': forms.TextInput(
                attrs={
                    'readonly': 'readonly',
                }
            )
        }
