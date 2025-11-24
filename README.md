# Base project

Base template project containing different kind of services for a complete local Django developing.

## Apps

In this project accounts app is included extending Django's default app.

## Services included

- Postgres v17 psycopg2-binary >= 2.9
- Redis >= 7.1
- Django >= 5.2
- Celery == 5.5.3
- Celery Beat
- Celery Flower >= 2.0
- db-web-ui sosedoff/pgweb:0.14.3
- Mailpit (local email service) axllent/mailpit

## Addresses

User interface links to access to different services:

- Django backend: [http://localhost:8000/admin]()
- Celery flower: [http://localhost:5555]()
- DB UI: [http://localhost:5051]()
- Django backend: [http://localhost:8000/admin]()
- Mailpit: [http://localhost:8025]()

## TO-DO list

Add a Makefile for easy run and management.

Add and configure these libraries:

- Django cache with redis (django-redis)
- DRF API REST (djangorestframework)
- DRF spectacular (drf-spectacular)
- DRF JWT (djangorestframework-simplejwt)

After adding these libs, fork this project and convert it to a cookiecutter template.