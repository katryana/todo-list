from django import forms

from manager.models import Task, Tag


class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"


class TagCreationForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"
