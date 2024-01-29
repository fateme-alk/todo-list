# Create your views here.
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView

from .forms import TaskForm
from .models import Task


def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    context = {"tasks": tasks, "form": form}
    return render(request, "task/index.html", context=context)


class UpdateTaskView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "task/update_task.html"
    success_url = "/"


class DeleteTaskView(DeleteView):
    model = Task
    template_name = "task/delete_task.html"
    success_url = reverse_lazy("task_list")
