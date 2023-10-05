from django import forms

from manager.models import Task


class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
