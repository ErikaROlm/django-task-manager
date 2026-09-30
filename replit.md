# Focusboard

A Django task manager for capturing, prioritizing, and completing personal work.

## Run & Operate

- `python manage.py migrate` — apply Django migrations
- `python manage.py runserver` — run the task manager locally
- `python manage.py test` — run the task manager test suite
- `python manage.py check` — validate the Django configuration

## Stack

- Django 5.2 on Python 3.11
- Server-rendered Django templates
- SQLite for local persistence
- CSS written in `static/css/style.css`

## Where things live

- `task_manager/` — Django project settings and root URLs
- `tasks/` — task model, forms, views, admin, and migrations
- `templates/` — page templates
- `static/css/style.css` — visual system and responsive layout

## Architecture decisions

- Use SQLite so the starter repository runs without provisioning an external service.
- Use Django templates and standard POST forms for CRUD actions, keeping persistence server-side and easy to extend.
- Keep the first version single-user and account-free; authentication can be added when the product needs shared workspaces.

## Product

Focusboard provides a personal task list with progress summary, search, status and priority filters, due-date awareness, and quick edit/complete/delete actions.

## User preferences

No additional user preferences recorded.

## Gotchas

- Run `python manage.py migrate` before the first launch.

## Pointers

- See the `pnpm-workspace` skill for workspace structure, TypeScript setup, and package details
