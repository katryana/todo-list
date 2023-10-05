from django.urls import path

from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, task_complete_undo

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("cars/<int:pk>/<str:act>/", task_complete_undo, name="toggle-task-complete"),
]

app_name = "manager"
