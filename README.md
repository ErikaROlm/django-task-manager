# Focusboard — Django Task Manager

Focusboard is a small Django task manager built from the `Task_manager` starter repository. It gives you a focused personal workspace for capturing tasks, setting priority and due dates, tracking progress, searching, filtering, and cleaning up completed work.

## Run locally

```bash
python manage.py migrate
python manage.py runserver
```

The app uses SQLite for local persistence and does not require a separate database service.

## Features

- Create and edit tasks with descriptions, status, priority, and due dates
- Toggle tasks between open and completed
- Search by title or description
- Filter by status and priority
- Overdue task tracking and lightweight progress summary
- Django admin at `/admin/`