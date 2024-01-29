from django.urls import path

from . import views
from .views import DeleteTaskView, UpdateTaskView

urlpatterns = [
    path("", views.index, name="index"),
    path("update_task/<int:pk>/", UpdateTaskView.as_view(), name="update"),
    path("delete_task/<int:pk>/", DeleteTaskView.as_view(), name="delete"),
]
