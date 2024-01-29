# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import TaskForm
from .models import Task


class TaskListView(ListView):
    model = Task
    context_object_name = "tasks"


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdateTaskView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "task/update_task.html"
    success_url = "/"


class DeleteTaskView(DeleteView):
    model = Task
    template_name = "task/delete_task.html"
    success_url = "/"
