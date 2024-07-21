from .models import Task, Comment

from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["name", "text", "value"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите комментарий'
            })
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["autor", "comment"]
        widgets = {
            "autor": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }),
            "comment": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите комментарий'
            })
        }

