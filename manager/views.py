from django.urls import reverse_lazy
from django.views import generic

from manager.forms import TaskCreationForm
from manager.models import Task


class TaskListView(generic.ListView):
    """View function for the home page of the site."""
    model = Task
    queryset = Task.objects.prefetch_related("tags")
    paginate_by = 5
    template_name = "task/index.html"


class TaskCreateView(generic.CreateView):
    form_class = TaskCreationForm
    success_url = reverse_lazy("manager:task-list")


class TaskUpdateView(generic.UpdateView):
    form_class = TaskCreationForm
    success_url = reverse_lazy("manager:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("manager:task-list")
