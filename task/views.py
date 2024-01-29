# Create your views here.
from django.shortcuts import redirect, render

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


def update_task(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {"form": form}
    return render(request, "task/update_task.html", context=context)


def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == "POST":
        task.delete()
        return redirect("/")
    context = {"task": task}
    return render(request, "task/delete_task.html", context=context)
