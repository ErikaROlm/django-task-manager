from datetime import date, timedelta

from django.test import TestCase
from django.urls import reverse

from .models import Task


class TaskFlowTests(TestCase):
    def setUp(self):
        self.task = Task.objects.create(
            title="Review the launch notes",
            description="Check the final copy before sharing.",
            priority=Task.Priority.HIGH,
            due_date=date.today() + timedelta(days=1),
        )

    def test_dashboard_lists_tasks_and_filters_by_search(self):
        response = self.client.get(reverse("task_list"), {"q": "launch"})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Review the launch notes")
        self.assertNotContains(response, "No tasks match")

    def test_create_task(self):
        response = self.client.post(
            reverse("task_create"),
            {
                "title": "Plan the weekly review",
                "description": "Bring the open questions.",
                "status": Task.Status.TODO,
                "priority": Task.Priority.MEDIUM,
                "due_date": "",
            },
        )

        self.assertRedirects(response, reverse("task_list"))
        self.assertTrue(Task.objects.filter(title="Plan the weekly review").exists())

    def test_toggle_marks_task_completed(self):
        response = self.client.post(reverse("task_toggle", args=[self.task.pk]))

        self.assertRedirects(response, reverse("task_list"))
        self.task.refresh_from_db()
        self.assertEqual(self.task.status, Task.Status.DONE)

    def test_delete_removes_task(self):
        response = self.client.post(reverse("task_delete", args=[self.task.pk]))

        self.assertRedirects(response, reverse("task_list"))
        self.assertFalse(Task.objects.filter(pk=self.task.pk).exists())