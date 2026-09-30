from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "status", "priority", "due_date"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "placeholder": "e.g. Prepare the project brief",
                    "autofocus": True,
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "placeholder": "Add a little context, notes, or the next step...",
                    "rows": 5,
                }
            ),
            "status": forms.Select(),
            "priority": forms.Select(),
            "due_date": forms.DateInput(
                format="%Y-%m-%d",
                attrs={"type": "date"},
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].label = "Task name"
        self.fields["description"].label = "Description"
        self.fields["status"].label = "Status"
        self.fields["priority"].label = "Priority"
        self.fields["due_date"].label = "Due date"
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"