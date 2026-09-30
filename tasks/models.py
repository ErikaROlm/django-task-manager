from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=160)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["completed", "-created_at"]
        verbose_name = "task"
        verbose_name_plural = "tasks"

    def __str__(self):
        return self.title