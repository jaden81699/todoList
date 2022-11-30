from django import forms
from django.forms import ModelForm

from todoList.models import List


class listForm(ModelForm):
    class Meta:
        model = List
        fields = '__all__'
        labels = {'task': 'Task Name:', 'time_task_created': 'Created:'}
        widgets = {
            # does not currently take "class" and "placeholder" from here instead it takes values from html
            'task': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Add a new task'})
        }
