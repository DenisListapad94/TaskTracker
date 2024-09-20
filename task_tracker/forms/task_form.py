from django import forms

from task_tracker.models import Task


# class TaskForm(forms.Form):
#     title = forms.CharField(label="title",max_length=64)
#     description = forms.CharField(label="description", max_length=256)


class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description","photo"]
        widgets = {
            "description": forms.Textarea(attrs={
                "height": 20,
                "width": 10
            })
        }
