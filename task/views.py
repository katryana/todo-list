from django.views import generic

from task.models import Task


class TaskListView(generic.ListView):
    """View function for the home page of the site."""
    model = Task
    queryset = Task.objects.prefetch_related("tags")
    paginate_by = 5
    template_name = "task/index.html"
