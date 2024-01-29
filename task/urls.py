from django.urls import path

from .views import DeleteTaskView, TaskCreateView, TaskListView, UpdateTaskView

urlpatterns = [
    path("", TaskListView.as_view(), name="list"),
    path("create/", TaskCreateView.as_view(), name="create"),
    path("update_task/<int:pk>/", UpdateTaskView.as_view(), name="update"),
    path("delete_task/<int:pk>/", DeleteTaskView.as_view(), name="delete"),
]
