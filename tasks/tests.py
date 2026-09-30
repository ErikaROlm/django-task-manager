from django.test import TestCase
from django.urls import reverse

from .models import Task


class TaskFlowTests(TestCase):
    def setUp(self):
        self.task = Task.objects.create(
            title="Review the launch notes",
            description="Check the final copy before sharing.",
        )

    def test_dashboard_lists_tasks_and_filters_by_search(self):
        response = self.client.get(reverse("task_list"), {"q": "launch"})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Review the launch notes")

    def test_create_task(self):
        response = self.client.post(
            reverse("task_create"),
            {
                "title": "Plan the weekly review",
                "description": "Bring the open questions.",
            },
        )

        self.assertRedirects(response, reverse("task_list"))
        self.assertTrue(Task.objects.filter(title="Plan the weekly review").exists())

    def test_edit_task(self):
        response = self.client.post(
            reverse("task_update", args=[self.task.pk]),
            {
                "title": "Review the final launch notes",
                "description": "Check the final copy and links.",
            },
        )

        self.assertRedirects(response, reverse("task_list"))
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, "Review the final launch notes")

    def test_toggle_marks_task_completed(self):
        response = self.client.post(reverse("task_toggle", args=[self.task.pk]))

        self.assertRedirects(response, reverse("task_list"))
        self.task.refresh_from_db()
        self.assertTrue(self.task.completed)

    def test_delete_removes_task(self):
        response = self.client.post(reverse("task_delete", args=[self.task.pk]))

        self.assertRedirects(response, reverse("task_list"))
        self.assertFalse(Task.objects.filter(pk=self.task.pk).exists())