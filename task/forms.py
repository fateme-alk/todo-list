from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "priority", "status"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter the title of task",
                }
            ),
            "priority": forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),
            "status": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }
