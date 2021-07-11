from django import forms

from my_web_project.main.models import Comment, Homework


class BootstrapFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_fields()

    def _init_bootstrap_fields(self):
        for (_, field) in self.fields.items():
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = ''
            field.widget.attrs['class'] += ' form-control'


class CommentForm(forms.ModelForm):
    homework_pk = forms.IntegerField(
        widget=forms.HiddenInput()
    )

    class Meta:
        model = Comment
        fields = ('comment', 'homework_pk')

    def save(self, commit=True):
        homework_pk = self.cleaned_data['homework_pk']
        homework = Homework.objects.get(pk=homework_pk)
        comment = Comment(
            comment=self.cleaned_data['comment'],
            homework=homework,
        )

        if commit:
            comment.save()

        return comment
