from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.http import require_POST

from .forms import TaskForm
from .models import Task


def task_list(request):
    tasks = Task.objects.all()
    query = request.GET.get("q", "").strip()
    status = request.GET.get("status", "all")
    priority = request.GET.get("priority", "all")

    if query:
        tasks = tasks.filter(Q(title__icontains=query) | Q(description__icontains=query))
    if status in {choice.value for choice in Task.Status}:
        tasks = tasks.filter(status=status)
    if priority in {choice.value for choice in Task.Priority}:
        tasks = tasks.filter(priority=priority)

    today = timezone.localdate()
    context = {
        "tasks": tasks,
        "query": query,
        "active_status": status,
        "active_priority": priority,
        "total_count": Task.objects.count(),
        "open_count": Task.objects.exclude(status=Task.Status.DONE).count(),
        "completed_count": Task.objects.filter(status=Task.Status.DONE).count(),
        "overdue_count": Task.objects.filter(
            due_date__lt=today,
        ).exclude(status=Task.Status.DONE).count(),
        "today": today,
        "status_choices": Task.Status.choices,
        "priority_choices": Task.Priority.choices,
    }
    return render(request, "tasks/task_list.html", context)


def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            messages.success(request, f'"{task.title}" was added to your list.')
            return redirect("task_list")
    else:
        form = TaskForm()
    return render(
        request,
        "tasks/task_form.html",
        {"form": form, "page_title": "Add a new task", "submit_label": "Add task"},
    )


def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, f'"{task.title}" was updated.')
            return redirect("task_list")
    else:
        form = TaskForm(instance=task)
    return render(
        request,
        "tasks/task_form.html",
        {
            "form": form,
            "task": task,
            "page_title": "Edit task",
            "submit_label": "Save changes",
        },
    )


@require_POST
def task_toggle(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.status = Task.Status.TODO if task.status == Task.Status.DONE else Task.Status.DONE
    task.save(update_fields=["status", "updated_at"])
    message = f'"{task.title}" marked as completed.' if task.status == Task.Status.DONE else f'"{task.title}" moved back to your list.'
    messages.success(request, message)
    return redirect(request.POST.get("next") or "task_list")


@require_POST
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    title = task.title
    task.delete()
    messages.success(request, f'"{title}" was deleted.')
    return redirect(request.POST.get("next") or "task_list")