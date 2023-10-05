from django import forms

from manager.models import Task, Tag


class TaskCreationForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}, format="%Y-%m-%dT%H:%M"),
        initial="%Y-%m-%dT%H:%M"
    )

    class Meta:
        model = Task
        fields = "__all__"


class TagCreationForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"
