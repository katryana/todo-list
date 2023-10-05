from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from manager.forms import TaskCreationForm
from manager.models import Task


class TaskListView(generic.ListView):
    """View function for the home page of the site."""
    model = Task
    queryset = Task.objects.prefetch_related("tags")
    paginate_by = 5
    template_name = "manager/index.html"


class TaskCreateView(generic.CreateView):
    form_class = TaskCreationForm
    success_url = reverse_lazy("manager:task-list")
    template_name = "manager/task_form.html"
    queryset = Task.objects.prefetch_related("tags")


class TaskUpdateView(generic.UpdateView):
    form_class = TaskCreationForm
    success_url = reverse_lazy("manager:task-list")
    template_name = "manager/task_form.html"
    queryset = Task.objects.prefetch_related("tags")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("manager:task-list")


def task_complete_undo(request, pk: int, act: str):
    task = Task.objects.get(id=pk)
    if act == "undo":
        task.is_done = False
    elif act == "complete":
        task.is_done = True
    task.save()
    return HttpResponseRedirect(reverse("manager:task-list"))
