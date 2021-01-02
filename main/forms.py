from .models import Task
from django.forms import ModelForm, Textarea


class Taskform(ModelForm):
    class Meta:
        model = Task
        fields = ['task']
        widgets = {"task": Textarea(attrs={
            'class': 'form-control',
            'placeholder' : 'Ждем отзыва)'

            })
        }